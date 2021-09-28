"""
LEFT AT: factories -> user, models



================================================================================
OCT 4-8 PLANS:
- 

SEPT 27-OCT 1 PLANS:
- test finished modules
- add validation methods to forms and models 

SEPT 20-24 PLANS:
- continue writing login tests
- try onting frontend tests

SEPT 13-17 PLANS:
- read about frontend testing
- write login tests

OCT 30 - SEPT 3 PLANS:
- login test cases outline

================================================================================

https://ue.instructure.com/courses/21282/files/3494368?module_item_id=634021

•	Pre-requisite:
1.	Testing working sheet should be compatible with the Operating system.
2.	Login page should appear.
3.	User Id and Password textboxes should be available with appropriate labels.
4.	Submit and Cancel buttons with appropriate captions should be available.

================================================================================

TC1.	Checking User Interface requirements.

TC2.	Textbox for UserId should:
		a. allow only alpha-numeric characters{a-z, A-Z, 0-9}
		b. not allow special characters like{'$','#','!','~','*',...} 
		c.  allow numeric characters like{0-9}

TC3.	Checking functionality of the Password textbox:
		a. Textbox for Password should accept more than six characters.
		b. Data should be displayed in encrypted format.

TC4.	Checking functionality of 'SUBMIT' button.

TC5.	Checking functionality of 'CANCEL' button.

================================================================================

"""



import pytest
from news_curation import create_app
from news_curation.extensions import db, bcrypt
from news_curation.user.forms import LoginForm
from news_curation.user.models import User

def save(obj):
	db.session.add(obj)
	db.session.commit()
	return obj

class TestLoginForm:
	"""Login, Form Test"""

	# IDEA: use webscraping techniques to test frontend
	# 		see: https://www.tutorialspoint.com/python_web_scraping/python_web_scraping_testing_with_scrapers.htm
	def test_login_elements_exist(self, testapp): 
		# FOR TESTING
		# 2.	Login page should appear.
		# 3.	User Id and Password textboxes should be available with appropriate labels.
		# 4.	Submit and Cancel buttons with appropriate captions should be available.
		response = testapp.get('/user/login')
		assert b'Username' in response
		assert b'Password' in response
		assert b'Forgot' in response
		assert b'Sign in' in response or \
				b'Log in' in response or \
				b'Login' in response

		# TODO here: apply frontend testing 

	@pytest.mark.skip(reason="nana-naniwhat interface requirements")
	def test_interface_requirements(self):
		"""TC1"""
		pass

	@pytest.mark.skip(reason="not available")
	def test_validate_success(self, user):
		"""Login successful"""
		save(user)
		form = LoginForm(username=user.username, password=user.password)
		user = User.query.filter_by(username=user.username).first()
		assert user
		assert bcrypt.check_password_hash(user.password, form.password)
		assert form.user == user
		# assert form.validate() is True
		# assert form.user == user

	@pytest.mark.skip(reason="not available")
	def test_validate_unknown_username(self, db):
		"""Unknown username"""
		form = LoginForm(username="unknown", password="example")
		# assert form.validate() is False
		# assert "Unknown username" in form.username.errors
		# assert form.user is None

	@pytest.mark.skip(reason="not available")
	def test_validate_invalid_password(self, user):
		"""Invalid password"""
		save(user)
		# form = LoginForm(username=user.username, password="wrongpassword")
		# assert form.validate() is False
		# assert "Invalid password" in form.password.errors


class TestLogginIn:
	"""Login, Functional Test"""

	@pytest.mark.skip(reason="not available")
	def test_user_id_input(self):
		"""TC2"""
		pass

	@pytest.mark.skip(reason="not available")
	def test_password(self):
		"""TC3"""
		pass

	@pytest.mark.skip(reason="not available")
	def test_buttons(self):
		"""TC4, TC5"""
		pass

	def test_can_log_in_returns_200(self, user, testapp):
		"""Login successful."""
		# Goes to login page
		res = testapp.get("/user/login")
		# Fills out login form in navbar
		form = res.forms["loginForm"]
		form["username"] = user.username
		form["password"] = "osmanthus!wine"
		# Submits
		res = form.submit().follow()
		assert res.status_code == 200

	@pytest.mark.skip(reason="not available")
	def test_sees_alert_on_log_out(self):
		"""Show alert on logout."""
		pass

	@pytest.mark.skip(reason="not available")
	def test_sees_error_message_if_password_is_incorrect(self):
		"""Show error if password is incorrect."""
		pass

	@pytest.mark.skip(reason="not available")
	def test_sees_error_message_if_username_doesnt_exist(self):
		"""Show error if username doesn't exist."""
		pass