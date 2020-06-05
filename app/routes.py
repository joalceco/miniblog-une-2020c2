from flask import render_template, flash, redirect, url_for
from app import app
from app import db
from app.forms import LoginForm, PostForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Post

@app.route("/")
@app.route("/index")
def index():
    if not current_user.is_authenticated:
        return redirect(url_for("login"))
    contacts = Post.query.filter_by(users_id = current_user.id).all()
    return render_template("index.html", contacts = contacts)


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

@app.route("/post/edit/<int:id>", methods=["POST"])
@login_required #Falto importar
def edit_post(id):
    post = Post.query.filter_by(id=id).first()
    if post:
        if current_user.id == post.users_id:
            pass
            # Editar
            form = PostForm()
            if form.validate_on_submit():
                post.first_name = form.first_name.data
                post.last_name = form.last_name.data
                post.phone = form.phone.data
                post.email = form.email.data
                post.note = form.note.data
                db.session.add(post)
                db.session.commit()
                return redirect(url_for("index"))
            form.first_name.data = post.first_name
            form.last_name.data = post.last_name
            form.phone.data = post.phone
            form.email.data = post.email
            form.note.data = post.note
            form.submit.value  = "Editar"
            return render_template("post.html", form=form, edit=True)
        else:
            flash("No tienes permisos para borrar este contacto")
    else:
        flash("El contacto no existe")
    return redirect(url_for("index"))

@app.route("/post/delete/<int:id>", methods=["POST"])
@login_required #Falto importar
def delete_post(id):
    post = Post.query.filter_by(id=id).first()
    if post:
        if current_user.id == post.users_id:
            db.session.delete(post)
            db.session.commit()
        else:
            flash("No tienes permisos para borrar este contacto")
    else:
        flash("El contacto no existe")
    return redirect(url_for("index"))

@app.route("/post", methods=["GET", "POST"])
@login_required #Falto importar
def post():
    #render formulario
    form = PostForm()
    if form.validate_on_submit():
        #si el verbo es post
        # insertar en base de datos
        p = Post()
        # p.add_new(form)
        p.first_name = form.first_name.data
        p.last_name = form.last_name.data
        p.phone = form.phone.data
        p.email = form.email.data
        p.note = form.note.data
        p.users_id = current_user.id
        db.session.add(p)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("post.html", form=form)

@app.route("/secreto")
@login_required #Falto importar
def secreto():
    return "Pagina secreta"

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))
