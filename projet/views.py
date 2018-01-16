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

class ChangerMdpForm(FlaskForm):
	next = HiddenField()
	login = StringField('Login :', validators=[DataRequired()])
	password = PasswordField('Mot de passe actuel :', validators=[DataRequired()])
	newpassword = PasswordField('Nouveau mot de passe :', validators=[DataRequired()])

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
		title="Accueil de iMusic")

@app.route("/album/<numero_page>")
def afficherListeAlbum(numero_page):
	listeAlbum = get_albums_pour_page(numero_page)
	return render_template(
		"albums.html",
		title="Liste des albums",
		listeAlbum=listeAlbum)

@app.route("/album/informations/<num_album>")
def afficherInformationsAlbums(num_album):
	informations = get_album(num_album)
	artiste = getNomArt(informations.artiste_id)
	return render_template(
		"informations.html",
		title="Info",
		informations=informations, artiste=artiste)

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

@app.route("/changermdp/", methods=("POST","GET"))
def changermdp():
	f = ChangerMdpForm()
	if f.validate_on_submit():
		user = f.get_authenticated_user()
		if user:
			m = sha256()
			m.update(f.newpassword.data.encode())
			qq = m.hexdigest()
			user.login = f.login.data
			user.password = qq
			db.session.commit()
			return redirect(url_for('home'))
	return render_template("connexion.html", sujet = "Changer de mot de passe", form = f,title="Changer de mot de passe")

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

@app.route("/profil/<log>")
def profil(log):
	listeP = get_playlists(log)
	return render_template("profil.html",title="Profil", listeP = listeP)

@app.route("/profil/")
def profil_none():
	return render_template("profil.html", title="Profil", listeP=[])



@app.route("/profil/playlist/<idPlay>")
def afficherPlaylist(idPlay):
	listeR = get_musiques(idPlay)
	print("ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp")
	print(idPlay)
	print(listeR)
	return render_template("profil.html",title="Playlist", listeR = listeR)



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
