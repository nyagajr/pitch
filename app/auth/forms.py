from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, BooleanField, SubmitField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError

class LoginForm(FlaskForm):
    email = StringField('Enter your email', validators=[Required(), Email()])
    password = PasswordField('Password',validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address', validators = [Required(), Email()])
    username = StringField('Enter your Username', validators=[Required()])
    password = PasswordField('Password Please', validators=[Required(), EqualTo('password_confirm', message='Password must match')])
    password_confirm = PasswordField('Confirm Passwords', validators=[Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self, data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('Account with that email exists')
    def validate_username(self, data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('Username already allocated')
