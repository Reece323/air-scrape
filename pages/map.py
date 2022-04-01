import dash

dash.register_page(__name__, path='/')

import dash
import dash_bootstrap_components as dbc
import folium
import pandas as pd
# import html
# from app import app
from components.mappings import *
from dash import dcc, html
from folium import plugins
import base64
from base64 import b64encode

image_filename = '/Users/codyreece/Desktop/Repos/airbnb/air-scrape/Dash/assets/airbnb_logo.png'
encoded_image = base64.b64encode(open(image_filename, 'rb').read())


coords = [36.3729, -94.2086]
lat = list(df['locationlat'])
lon = list(df['locationlng'])
name = list(df['name'])
url = list(df['url'])
rate = list(df['reviewsModulelocalizedOverallRating'])
price = list(df['pricingrateamount'])
guests = list(df.numberOfGuests)
rooms = list(df.rooms)
beds = list(df.beds)
baths = list(df.baths)

map=folium.Map(location=coords,zoom_start=11)
fg=folium.FeatureGroup(name="my map")


pop = dbc.Row([
            dbc.Row(html.Center(html.H5( name ))),
            html.Hr(),
            dbc.Row(html.Center(html.H5('$'+ str(price) +' /night'))),
            dbc.Row([html.H5('⭐' + str(rate))]),
            html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode())),
            dbc.Row([html.A('Go to Listing', href='site')])
        ])







def map_listings():
    for lt, ln, nm, site, rater, prc, gsts, bds, bths, in zip(lat, lon, name, url, rate, price, guests, beds, baths):
        fg.add_child(
            folium.Marker(location=[lt, ln],
                          popup=pop,
                          icon=folium.Icon(color='darkblue')
                          )
        )

    return map.add_child(fg), 

# print(map_listings())


listing_map = map_listings()
# listing_map.save('Bentonville.html')

listing_title = html.H3(html.Center('AirBnB Listings Map'),className='my-5')

map_view = html.Iframe(
                id='map',
                srcDoc=open('Bentonville.html', 'r').read(),
                width='650',
                height='650',
                className='iframo',
                )


layout = html.Div([
            dbc.Row([
                listing_title
            ]),
            dbc.Row([
                dbc.Col([
                    map_view
                ],
                className='logo2'
                ),
                dbc.Col([
                    html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()))
                ],
                className='my-5'
                )
            ],
            justify='start'
        )
    ])
