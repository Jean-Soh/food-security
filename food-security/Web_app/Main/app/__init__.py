from flask import Flask
from app.middleware import PrefixMiddleware
from flask_bootstrap import Bootstrap5 

application = Flask(__name__)

bootstrap = Bootstrap5(application)
# set voc=False if you run on local computer
application.wsgi_app = PrefixMiddleware(application.wsgi_app, voc=False)

from app import routes