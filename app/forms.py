from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")

class SignUpForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    submit = SubmitField("Sign Up")

class PostForm(FlaskForm):
    first_name = StringField("Nombre", validators=[DataRequired()])
    last_name = StringField("Apellidos")
    phone = StringField("Telefono", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    note = StringField("body", validators=[DataRequired()])
    submit = SubmitField("Registrar")