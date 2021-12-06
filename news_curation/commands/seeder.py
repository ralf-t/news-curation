"""seeder commands"""

from flask import current_app

from news_curation.extensions import db, bcrypt
from news_curation.commands import with_appcontext, seeder_cli

from news_curation.user.models import User
from news_curation.post.models import Post
from news_curation.topic.models import Topic
from news_curation.comment.models import Comment

import click
import random
from os import environ, system
from faker import Faker

environ["FLASK_ENV"] = "seeder"

@seeder_cli.command("setup")
@with_appcontext
def setUp():
    choice = input("This will delete any existing database and rebuild from scratch. Press \"y\" to proceed. : ").lower()
    
    if choice == 'y':
        db.drop_all()
        print("DB dropped.")

        print("Creating DB...")
        db.create_all()

        print("Creating topics...")

        # create topics
        for i in range(10):
            # localize to lorem
            fake = Faker("la")
            
            topic = Topic()
            topic.topic = fake.word()
            
            db.session.add(topic)
            
        db.session.commit()

        # topics query
        topics = Topic.query.all()

        # create 5 user and their posts(with topics)
        print("Creating user and posts...")

        for i in range(5):
            fake = Faker()
            
            user = User()
            user.first_name = fake.first_name()
            user.last_name = fake.last_name()
            user.username = fake.user_name()
            user.email = fake.email()
            user.password = bcrypt.generate_password_hash("secret").decode("utf-8")

            # 2-5 posts for each user
            for i in range(random.randint(2,5)):
                # localize to lorem
                fake = Faker("la")

                post = Post()
                post.title = fake.paragraph(nb_sentences=2, variable_nb_sentences=True)
                post.content = fake.paragraph(nb_sentences=10, variable_nb_sentences=True)
                post.author = user

                # post will have 1-5 topics
                for j in range(random.randint(1,5)):
                    
                    # get a random topic via lambda function
                    random_topic = lambda : topics[random.randint(0, len(topics) - 1)]
                    
                    # fetch untila different topic can be assigned
                    topic_ = random_topic()
                    while (topic_ in post.topic):
                        topic_ = random_topic()
                    
                    post.topic.append(topic_)
                
                db.session.add(post)
            
            # user will have 3-5 topics of interest
            for i in range(random.randint(3,5)):
                user.topics_of_interest.append(random_topic())

        # commit here now to query users later
        db.session.commit()
        
        # posts query
        posts = Post.query.all()
        random_post = lambda : posts[random.randint(0, len(posts) - 1)]
        
        # save 2-5 posts
        for u in User.query.all():
            # can also save own post
            for i in range(random.randint(2,5)):
                post = random_post()
                u.saved_posts.append(post)
                
                # give a comment
                comment = Comment()
                comment.author = u
                comment.post = post
                comment.content = fake.paragraph(nb_sentences=2, variable_nb_sentences=True)
        
        # admin
        user = User(
			first_name = "admin",
			last_name = "admin",
			username = "admin",
			email = "admin@admin.com",
			password = bcrypt.generate_password_hash("secret").decode("utf-8")
		)

        db.session.add(user)

        # final commit
        db.session.commit()

        print("Setup done!")

    else:
        print("DB setup aborted!")


@seeder_cli.command("teardown")
@with_appcontext
def tearDown():
	try:
		# returns error if db is not created yet or if there is a missing/altered table
		User.query.all()
		Post.query.all()
		Topic.query.all()

		db.drop_all()

		click.echo("Database has been dropped.")

	except:
		click.echo("Database and tables might have been altered manually. If error persists, delete the database manually.")

	click.echo("Teardown done!")
