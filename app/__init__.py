from flask import Flask
from flask_bootstrap import Bootstrap
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

def create_app():
  app = Flask(__name__)
  GoogleMaps(app, key='AIzaSyA6e7JHTBzX_1hmLE_pz7kJdLc_pfWaVYk')
  Bootstrap(app)

  return app

app = create_app()
from app import routes