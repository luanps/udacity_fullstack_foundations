import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('USERNAME')
    MAIL_PASSWORD = os.environ.get('PASSWORD') 
    ADMINS = ['luann.porfirio@gmail.com']

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'nice_try'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
