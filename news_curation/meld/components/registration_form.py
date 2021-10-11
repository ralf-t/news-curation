from flask_meld.component import Component
from flask import redirect, url_for, request
from news_curation.user.forms import RegistrationForm as Form


class RegistrationForm(Component):
    form = Form()
    submitted = False

    def updated(self, field):
        self.validate(field)
        self.submitted = False

    def save(self):
        self.submitted = True
        if self.validate():
            return redirect(url_for("user.home"))
