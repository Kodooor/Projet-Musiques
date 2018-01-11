from .app import db

class Artiste(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nom = db.Column(db.String(100))


class Album(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	genre = db.Column(db.String(100))
	image = db.Column(db.String(100))
	titre = db.Column(db.String(100))
	dateSortie = db.Column(db.String(100))
	artiste_id = db.Column(db.Integer, db.ForeignKey("artiste.id"))
	artiste = db.relationship("Artiste", backref=db.backref("artiste", lazy="dynamic"))


def get_la_liste_album():
	return Album.query.all()

# from flask_login import UserMixin
#
# class User(db.Model, UserMixin):
# 	username = db.Column(db.String(50), primary_key=True)
# 	password = db.Column(db.String(64))
#
# 	def get_id(self):
# 		return self.username
