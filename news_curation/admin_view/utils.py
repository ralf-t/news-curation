from flask import flash, redirect, url_for
from flask_login import current_user
import flask_admin as f_admin
from flask_admin import expose
from flask_admin.contrib import sqla

class MyModelView(sqla.ModelView):

    def is_accessible(self):
        return current_user.is_authenticated and current_user.username == "admin"

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        flash("You are not an admin.","warning")
        return redirect(url_for('user.home'))

class MyAdminIndexView(f_admin.AdminIndexView):

    @expose('/')
    def index(self):
        if not (current_user.is_authenticated and current_user.username == "admin"):
            flash("You are not an admin.","warning")
            return redirect(url_for('user.home'))
        return super(MyAdminIndexView, self).index()