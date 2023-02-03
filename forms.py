from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email

class UserRegistration(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(min=1, max=20)],)
    password = PasswordField("Password", validators=[InputRequired(),Length(min=6, max=60)],)
    email = StringField("Email Address", validators=[InputRequired(), Email(), Length(max=50)],)
    first_name = StringField("First Name", validators=[InputRequired(), Length(max=30)],)
    last_name = StringField("Last Name", validators=[InputRequired(), Length(max=30)],)

class UserLogin(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(min=1, max=20)],)
    password = PasswordField("Password", validators=[InputRequired(), Length(min=1, max=20)],)

class FeedbackForm(FlaskForm):
    title = StringField("Title", validators =[ InputRequired(), Length(max=100)],)
    content = StringField("Content", validators =[ InputRequired()],)

class DeleteForm(FlaskForm):
    """Delete form is blank"""