from flask_meld.component import Component
from flask import redirect, url_for, request, flash

from news_curation.user.forms import RegistrationForm as Form
from news_curation.extensions import bcrypt, db
from news_curation.user.models import User


class RegistrationForm(Component):
    form = Form()
    submitted = False

    def updated(self, field):
        self.validate(field)
        self.submitted = False

    def save(self):
        self.submitted = True
        if self.validate():
            form = self.form
            #generate hashed password for the password
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            
            user = User(
                    first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    username=form.username.data,
                    email=form.email.data,
                    password=hashed_password
                )
            db.session.add(user)
            db.session.commit()

            flash('Your account has been created!', 'success')
            return redirect(url_for('user.login'))
