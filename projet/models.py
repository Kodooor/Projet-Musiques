from .app import db
from flask_login import UserMixin
from .app import login_manager

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

class User(db.Model, UserMixin):
	login = db.Column(db.String(50), primary_key=True)
	password = db.Column(db.String(50))

	def get_id(self):
		return self.login

class Musique(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	titre = db.Column(db.String(100))
	nom_de_fichier = db.Column(db.String(100))
	album_id = db.Column(db.Integer, db.ForeignKey("album.id"))
	album = db.relationship("Album", backref=db.backref("album", lazy="dynamic"))

class Playlist(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	titre = db.Column(db.String(100))
	user_login = db.Column(db.Integer, db.ForeignKey("user.login"))
	user = db.relationship("User", backref=db.backref("user", lazy="dynamic"))

class RelationPM(db.Model):
	musique_id = db.Column(db.Integer, db.ForeignKey("musique.id"), primary_key=True)
	musique = db.relationship("Musique", backref=db.backref("musique", lazy="dynamic"))
	playlist_id = db.Column(db.Integer, db.ForeignKey("playlist.id"), primary_key=True)
	playlist = db.relationship("Playlist", backref=db.backref("playlist", lazy="dynamic"))

# GESTION DES ALBUMS

def get_la_liste_album():
	return Album.query.all()

def get_album(id):
	return Album.query.get(id)

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

# GESTION DES PLAYLISTS
def get_playlists(login):
	listeU = User.query.all()
	listeP = Playlist.query.all()
	listeRep = []
	for u in listeU:
		if u.login == login:
			for p in listeP:
				if p.user_login == u.login :
					listeRep.append(p)
	return listeRep

def get_musiques(idP):
	listeR = RelationPM.query.all()
	listeM = Musique.query.all()
	listeRep = []
	for r in listeR:
		if r.playlist_id == idP:
			for m in listeM:
				if r.musique_id == m.id :
					listeRep.append(m)
	return listeRep


@login_manager.user_loader
def load_user(username):
	return User.query.get(username)

def get_user(login):
	return User.query.get(login)


# def get_artite_albums():
# 	artiste = Artiste.query.all()
# 	album = Album.query.all()
# 	for artiste in query :
# 	album = Artiste.filter_by(artiste_id=id)
# 	return
