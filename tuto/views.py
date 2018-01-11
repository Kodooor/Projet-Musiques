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
	listeAlbum = get_la_liste_album()
	print(listeAlbum)
	return render_template(
		"home.html",
		title="Hello World!",
		listeAlbum = listeAlbum)

@app.route("/album")
def get_albums_pour_page(numero):
    debut = int(numero) * 6
    fin = int(numero) * 6 + 6
    return Album.query.all()[debut:fin]

def get_nombre_de_page_album():
    albums = Album.query.all()
    nombre = math.ceil((len(albums)-1)/6)
    if nombre == 0:
        return 1
    return nombre

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
