from app import app
from flask import render_template
from flask_googlemaps import Map

'''
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Pawel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
'''

@app.route("/")
def mapview():
    # creating a map in the view
    mymap = Map(
        identifier="view-side",
        lat=37.4419,
        lng=-122.1419,
        markers=[(37.4419, -122.1419)],
    )
    '''sndmap = Map(
        identifier="sndmap",
        lat=37.4419,
        lng=-122.1419,
        markers=[
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
             'lat': 37.4419,
             'lng': -122.1419,
             'infobox': "<b>Hello World</b>"
          },
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
             'lat': 37.4300,
             'lng': -122.1400,
             'infobox': "<b>Hello World from other place</b>"
          }
        ]
    )'''
    sndmap = Map(
        identifier="catsmap",
        lat=37.4419,
        lng=-122.1419,
        style="height:400px;width:500px;margin:0;",
        markers=[
            {
                'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
                'lat': 37.4419,
                'lng': -122.1419,
                'infobox': "<img width='100px' height='100px' src='static/images/cat1.jpg' />"
            },
            {
                'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
                'lat': 37.4300,
                'lng': -122.1400,
                'infobox': "<img width='100px' height='100px' src='static/images/cat2.jpg' />"
            },
            {
                'icon': 'http://maps.google.com/mapfiles/ms/icons/yellow-dot.png',
                'lat': 37.4500,
                'lng': -122.1350,
                'infobox': "<img width='100px' height='100px' src='static/images/cat3.jpg' />"
            }
        ]
    )
    return render_template('index.html', mymap=mymap, sndmap=sndmap)