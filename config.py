import os.path

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUT = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dump.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True

