from .app import app
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField
from wtforms.validators import DataRequired
from flask import url_for, redirect
from .app import db
from .models import *

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

@app.route("/album/details/<num_album>")
def afficherInformationsAlbums(num_album):
	informations = get_la_liste_album()
	return render_template(
		"informations.html",
		title="Informations album",
		informations=informations)


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
# class AuthorForm(FlaskForm):
# 	id = HiddenField('id')
# 	name = StringField('Nom', validators=[DataRequired()])
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
