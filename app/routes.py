from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user
from app.models import User

@app.route("/")
@app.route("/index")
def index():
    user = {"username":"Carlos"}
    return render_template("index.html", user=user)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        #POST
        #Iniciar sesión con base de datos
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("No se encontro el usuario o la contraseña esta incorrecta")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        flash("Iniciaste Sesión correctamente, Hola {}".format(form.username.data))
        return redirect("/index")
    return render_template("login.html", title="Login",form=form)


@app.route("/secreto")
@login_required #Falto importar
def secreto():
    return "Pagina secreta"

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))
