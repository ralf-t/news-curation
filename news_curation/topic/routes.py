from flask import render_template, url_for, flash, redirect, request, abort
from flask_login import login_required, current_user

from news_curation.extensions import db

from news_curation.topic import bp
from news_curation.topic.models import Topic


@bp.route("/update", methods=['GET', 'POST'])
@login_required
def update():

    topics = Topic.query

    # baka pwede na iremove search?

    if request.method == "POST":
        if request.form.get("update_topics"):
            
            # create dictionary of checked topics
            checked = request.form.to_dict()

            # remove uneccessary values
            checked.pop('csrf_token')
            checked.pop('update_topics')

            # add to topics of interest if not added yet
            for topic in checked:
                t = Topic.query.filter_by(topic=topic).first()
                
                if t not in current_user.topics_of_interest:
                    current_user.topics_of_interest.append(t)

            # remove topics from user if not checked
            user_topics = current_user.topics_of_interest.all()
            for topic in user_topics:
                if topic.topic not in checked:
                    current_user.topics_of_interest.remove(topic)
            
            try:
                db.session.commit()
                flash("Updated topics of interest.","success")
                return redirect(url_for("topic.update"))
            except:
                flash("An error occured while updating intereset.","success")
            
        elif request.form.get("search"):
            # filter results
            topics = topics.filter(Topic.topic.ilike('%'+ request.form["query"] +'%'))
    
    topics = topics.all()
    return render_template("topic/topics.html", topics=topics)
