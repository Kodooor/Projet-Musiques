from .app import manager, db

@manager.command
def loaddb(filename):
	"""creates the tables and populates them with data."""
	db.create_all()

	import yaml
	books = yaml.load(open(filename))

	from .models import Author, Book

	authors = {}
	for b in books:
		a = b["author"]
		if a not in authors:
			o = Author(name=a)
			db.session.add(o)
			authors[a] = o
	db.session.commit()

	for b in books:
		a = authors[b["author"]]
		o = Book(price = b["price"],
			title = b["title"],
			url = b["url"],
			img = b["img"],
			author_id = a.id)
		db.session.add(o)
	db.session.commit()
@manager.command
def syncdb():
	'''Creates all missing tables.'''
	db.create_all()

@manager.command
def newuser(username, password):
	'''adds a new user'''
	from .models import User
	from hashlib import sha256
	m = sha256()
	m.update(password.encode())
	u = User(username=username, password=m.hexdigest())
	db.session.add(u)
	db.session.commit()

@manager.command
def passwd(username, password):
	'''change the password of a user'''
	from .models import User
	from hashlib import sha256
	m = sha256()
	
