from .app import app
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired
from flask import url_for, redirect, request
from .app import db
from .models import *
from hashlib import sha256
from flask_login import login_user, current_user, login_required, logout_user


class LoginForm(FlaskForm):
	next = HiddenField()
	login = StringField('Login :', validators=[DataRequired()])
	password = PasswordField('Mot de passe :', validators=[DataRequired()])

	def get_authenticated_user(self):
		user = User.query.get(self.login.data)
		if user is None:
			return None
		m = sha256()
		m.update(self.password.data.encode())
		qq = m.hexdigest()
		return user if qq == user.password else None

@app.route("/")
def home():
	return render_template(
		"home.html",
		title="Hello World!")

@app.route("/album/<numero_page>")
def afficherListeAlbum(numero_page):
	listeAlbum = get_albums_pour_page(numero_page)
	return render_template(
		"albums.html",
		title="Liste des albums",
		listeAlbum=listeAlbum)

@app.route("/artiste/<numero_page>")
def afficherListeArtiste(numero_page):
	listeArtiste = get_artiste_page(numero_page)
	return render_template("artiste.html",
		title="Liste des artistes",
		listeArtiste=listeArtiste)

@app.route("/artiste/infoArtiste/<art>")
def afficherInfoArtiste(art):
	listeAlb= get_artiste_albums(art)
	return render_template("info-artiste.html",
		title="Information",
		nomA=art,
		listeAlb=listeAlb)


@app.route("/creercompte/", methods=("POST","GET"))
def creercompte():
	f = LoginForm()
	if f.validate_on_submit():
		ur = get_user(f.login.data)
		if ur == None:
			m = sha256()
			m.update(f.password.data.encode())
			qq = m.hexdigest()
			u = User(login = f.login.data, password = qq)
			db.session.add(u)
		db.session.commit()
		login_user(u)
		return redirect(url_for('home'))
	return render_template("connexion.html",sujet = "Creation de compte", form = f,title="Creation de compte")

@app.route("/connexion/", methods=("POST", "GET"))
def connexion():
	f = LoginForm()
	if not f.is_submitted():
		f.next.data = request.args.get("next")
	elif f.validate_on_submit():
		user = f.get_authenticated_user()
		if user:
			login_user(user)
			next = f.next.data or url_for("home")
			return redirect(next)
	return render_template("connexion.html", sujet = "Connexion", form = f,title="Connexion")

@app.route("/deconnexion/")
def deconnexion():
	logout_user()
	return redirect(url_for('home'))

# import yaml, os.path
#
# data = yaml.load(
# 	open(
# 		os.path.join(
# 			os.path.dirname(os.path.dirname(__file__)),
# 			"data.yml")))
# @app.route("/books/")
# def books():
# 	return render_template(
# 		"books.html",
# 		books=data)
#

# 	@app.route("/edit/author/<int:id>")
# 	def edit_author(id):
# 		a = get_author(id)
# 		f = AuthorForm(id=a.id, name=a.name)
# 		return render_template(
# 			"edit-author.html",
# 			author=a, form=f)
#
# 	@app.route("/save/author/", methods=("POST",))
# 	def save_author():
# 		a = None
# 		f = AuthorForm()
# 		if f.validate_on_submit():
# 			id = int(f.id.data)
# 			a = get_author(id)
# 			a.name = f.name.data
# 			db.session.commit()
# 			return redirect(url_for('one_author', id=a.id))
# 		a = get_author(int(f.id.data))
# 		return render_template(
# 			"edit-author.html",
# 			author=a, form=f)
