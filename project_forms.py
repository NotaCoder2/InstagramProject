from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, FileField
from wtforms.validators import DataRequired, EqualTo


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Field should not be empty')])
    password = PasswordField('Password', validators=[DataRequired(message='Field should not be empty')])
    submit = SubmitField('Log in')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Field should not be empty')])
    password = PasswordField('Enter your password', [DataRequired(message='Field should not be empty'),
                                                EqualTo('confirm', message='Field should not be empty')])
    confirm = PasswordField('Confirm password', validators=[DataRequired(message='Field should not be empty')])
    submit = SubmitField('Register')


class UploadPhotoForm(FlaskForm):
    file = FileField('Download a photo', validators=[FileRequired(message='Field should not be empty')])
    descrypt = TextAreaField('Description')
    submit = SubmitField('Upload')


class ChangeInfoForm(FlaskForm):
    main_photo = FileField('Change the main photo')
    user_name = StringField('Change the username')
    password_hash = PasswordField('Enter your new password',
                                  validators=[EqualTo('confirm', message='Passwords should match')])
    confirm = PasswordField('Confirm password')
    submit = SubmitField('Save changes')
