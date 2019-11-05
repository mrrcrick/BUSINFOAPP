from flask import Flask
import os

app = Flask(__name__)
dbpath = os.path.join(os.getcwd(),'/database/tfl.db')
dbpath = 'database/tfl.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+dbpath
print ('***** '+dbpath)
from app import routes
