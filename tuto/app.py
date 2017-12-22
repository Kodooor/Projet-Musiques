from flask import Flask
app = Flask(__name__)
app.debug = True

from flask_script import Manager
manager = Manager(app)

app.config['BOOTSTRAP_SERVE_LOCAL'] = True
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)

import os.path

def mkpath(p):
	return os.path.normpath(
		os.path.join(
			os.path.dirname(__file__),
			p))
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + mkpath('../tuto.db')
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = "bbb225a3-bd0b-46f2-bf5a-9f1bc13d0c54" 
