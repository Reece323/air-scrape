import dash

dash.register_page(__name__, path='/')

import folium
import pandas as pd
from components.mappings import *
import dash_bootstrap_components as dbc
from dash import html
from folium import plugins


photoss = df['photos'][0]
pics = [d['large'] for d in photoss if 'large' in d]
coords = [36.3729, -94.2086]
lat = list(df['locationlat'])
lon = list(df['locationlng'])
name = list(df['name'])
url = list(df['url'])
rate = list(df['reviewsModulelocalizedOverallRating'])
price = list(df['pricingrateamount'])

map=folium.Map(location=coords,zoom_start=11)
fg=folium.FeatureGroup(name="my map")

def map_listings():
    for lt, ln, nm, site, rater, prc in zip(lat, lon, name, url, rate, price):
        fg.add_child(
            folium.Marker(location=[lt, ln],
                          popup='<h5> <center> <b>' + nm + "</b> </center> </h5>\
                            <hr> <div> <b> <center> <h5> $" + str(prc) + "/night </h5> </center> </b> </div>\
                            <div> <center> <h5> <p>&#11088; "+str(rater)+" </h5> </center> </div>\
                            <center> <img width='150'src='https://github.com/Reece323/air-scrape/blob/main/assets/airbnb_logo.png?raw=true'/></center>\
                            <a href=" + site + ">\
                            <center> <b> <h5> Go to Listing </h5> </b> </center> </a>",
                          icon=folium.Icon(color='darkblue')
                          )
        )

    return map.add_child(fg), 

# print(map_listings())


listing_map = map_listings()
# listing_map.save('Bentonville.html')

title = html.H3(html.Center('AirBnB Listings Map'),className='my-5')

map_view = html.Iframe(
                id='map',
                srcDoc=open('Bentonville.html', 'r').read(),
                width='650',
                height='650',
                className='iframo',
                )


layout = html.Div([
            dbc.Row([
                title
            ]),
            dbc.Row([
                dbc.Col([
                    map_view
                ],
                className='logo2'
                ),
                dbc.Col([
                    html.H4(['More content here']),
                    html.H4(['More content here']),
                    html.H4(['More content here']),
                    html.H4(['More content here']),
                    html.H4(['More content here']),
                    html.H4(['More content here']),
                    html.H4(['More content here']),
                    html.H4(['More content here']),
                    html.H4(['More content here']),
                ],
                className='my-5'
                )
            ],
            justify='start'
        )
    ])
