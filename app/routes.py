from app import app
from flask import render_template
from flask_googlemaps import Map

import json
import requests



@app.route("/")
def mapview():
    response = requests.get("https://raw.githubusercontent.com/mmcloughlin/starbucks/master/locations.json")
    loc_from_json = json.loads(response.text)

    icons = {
        'green': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
        'blue': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
        'yellow': 'http://maps.google.com/mapfiles/ms/icons/yellow-dot.png',
    }

    infobox_markup = "<img width='100px' height='100px' src='static/images/cat"

    locations = []
    for i in range(3):
        locations.append(
            {
                'icon': icons['green'],
                'lat': loc_from_json[i]['latitude'],
                'lng': loc_from_json[i]['longitude'],
                'infobox': infobox_markup + str(i + 1) + ".jpg' />"
            }
        )

    # creating a map in the view
    #route = Route("app/static/20180117_023924.tcx.xml")

    sndmap = Map(
        #route.trackpoints,
        identifier="catsmap",
        lat=locations[0]['lat'],
        lng=locations[0]['lng'],
        style="height:400px;width:500px;margin:0;",
        markers=[(loc['lat'], loc['lng'], loc['infobox'], loc['icon']) for loc in locations],
        fit_markers_to_bounds=True
    )
    return render_template('index.html', sndmap=sndmap, locations=locations)
