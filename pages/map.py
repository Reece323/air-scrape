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

image_filename = '/Users/codyreece/Desktop/Repos/airbnb/air-scrape/assets/airbnb_logo.png'
image_filename2 = '/Users/codyreece/Desktop/Repos/airbnb/air-scrape/assets/air4.png'
airbnblogo = base64.b64encode(open(image_filename, 'rb').read())
airr4 = base64.b64encode(open(image_filename2, 'rb').read())


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

map=folium.Map(location=coords,zoom_start=11, zoom_control=False)
tile_layer = folium.TileLayer(
    tiles="https://{s}.basemaps.cartocdn.com/rastertiles/dark_all/{z}/{x}/{y}.png",
    attr='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
    max_zoom=19,
    name='darkmatter',
    control=False,
    opacity=0.7
)
tile_layer.add_to(map)

fg=folium.FeatureGroup(name="my map")


pop = dbc.Row([
            dbc.Row(html.Center(html.H5( name ))),
            html.Hr(),
            dbc.Row(html.Center(html.H5('$'+ str(price) +' /night'))),
            dbc.Row([html.H5('⭐' + str(rate))]),
            html.Img(src='data:image/png;base64,{}'.format(airr4.decode())),
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

listing_title = html.H1([html.Center(['AirBnB Listings Map'],
                                    style={
                                        'text-shadow':'1px 1px 3px rgba(255, 255, 255, 1)',
                                        'color':'rgba(255, 90, 95, 1)',
                                        'font-weight':'800'
                                        })]
                                    ,
                                    className='my-5')

map_view = html.Iframe(
                id='map',
                srcDoc=open('Bentonville.html', 'r').read(),
                width='450',
                height='850',
                className='iframo',
                )


layout = html.Div([
            dbc.Row([
                listing_title
            ]),
            dbc.Row([
                dbc.Col([
                    html.Hr(),
                    html.Hr(),
                    map_view
                ],
                className='logo2 mb-5'
                ),
                dbc.Col([
                    html.Center(html.H4('Placeholder text....')),
                    html.Hr(),
                    html.Center(html.H4('Placeholder text....')),
                    html.Hr(),
                    html.Center(html.H4('Placeholder text....'))
                ],
                className='my-5'
                )
            ],
            style= {'margin-left':'3rem','margin-right':'3rem','margin-bottom':'8rem'},
            className='cardsss',
            justify='start'
        )
    ]
    )
