from .app import manager, db
from .models import *
import yaml

@manager.command
def loaddb(filename):
	"""creates the tables and populates them with data."""
	db.create_all()
	album = yaml.load(open(filename))
	artiste = {}
	for a in album:
		ar = a["by"]
		if ar not in artiste:
			o = Artiste(nom=ar)
			db.session.add(o)
			artiste[ar] = o
	db.session.commit()

	for b in album:
		a = artiste[b["by"]]
		o = Album(genre = b["genre"],
			image = b["img"],
			titre = b["title"],
			dateSortie = b["releaseYear"],
			artiste_id = a.id)
		db.session.add(o)
	db.session.commit()
#
# @manager.command
# def syncdb():
# 	'''Creates all missing tables.'''
# 	db.create_all()
#
# @manager.command
# def newuser(username, password):
# 	'''adds a new user'''
# 	from .models import User
# 	from hashlib import sha256
# 	m = sha256()
# 	m.update(password.encode())
# 	u = User(username=username, password=m.hexdigest())
# 	db.session.add(u)
# 	db.session.commit()
#
# @manager.command
# def passwd(username, password):
# 	'''change the password of a user'''
# 	from .models import User
# 	from hashlib import sha256
# 	m = sha256()
#
