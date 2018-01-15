from .app import db

class Artiste(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nom = db.Column(db.String(100))

def __repr__(self):
        return '<Artiste %r>' % self.nom

class Album(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	genre = db.Column(db.String(100))
	image = db.Column(db.String(100))
	titre = db.Column(db.String(100))
	dateSortie = db.Column(db.String(100))
	artiste_id = db.Column(db.Integer, db.ForeignKey("artiste.id"))
	artiste = db.relationship("Artiste", backref=db.backref("artiste", lazy="dynamic"))

# GESTION DES ALBUMS

def get_la_liste_album():
	return Album.query.all()

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


# GESTION DES ARTISTES
def get_artiste():
	return Artiste.query.all()

def get_artiste_page(numero):
    debut = int(numero) * 6
    fin = int(numero) * 6 + 6
    return Artiste.query.all()[debut:fin]

def get_nombre_de_page_artiste():
    artiste = Artiste.query.all()
    nombre = math.ceil((len(artiste)-1)/6)
    if nombre == 0:
        return 1
    return nombre

def get_artiste_albums(art):
	listeA = Artiste.query.all()
	listeAl= Album.query.all()
	liste=[]
	for a in listeA :
			if a.nom == art:
				for b in listeAl:
					if b.artiste_id == a.id :
						liste.append(b)
	return liste





# def get_artite_albums():
# 	artiste = Artiste.query.all()
# 	album = Album.query.all()
# 	for artiste in query :
# 	album = Artiste.filter_by(artiste_id=id)
# 	return


# from flask_login import UserMixin
#
# class User(db.Model, UserMixin):
# 	username = db.Column(db.String(50), primary_key=True)
# 	password = db.Column(db.String(64))
#
# 	def get_id(self):
# 		return self.username
