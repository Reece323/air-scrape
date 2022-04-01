import dash

dash.register_page(__name__)

import dash_bootstrap_components as dbc
import dash_daq as daq
from components.pred_lists import *
from dash import dcc, html

# from pages.predictions import *


row1 = html.Div([
        dbc.Row(
            dbc.Col(
                html.Center(html.H5('Price per night estimator for AirBnB listings',
                className='mb-5 mt-2'
                ))
            )
        ),

        dbc.Row([
            dbc.Col([
                html.H6("Property Type", className='mb-1'),
                dcc.Dropdown(
                    id='property',
                    options=property_type,
                    className='mb-4',
                        ),
                    ]),
            dbc.Col([
                html.H6("Room Type", className='mb-1'),
                dcc.Dropdown(
                    id='room',
                    options=[
                        {'label': 'Entire Home/Apartment', 'value': 'Entire home/apt'},
                        {'label': 'Private Room', 'value': 'Private room'},
                        {'label': 'Shared room', 'value': 'Shared room'}
                    ],
                    className='mb-4',
                    ),
                ])
            ]
        ),

        dbc.Row([
                dbc.Col([
                        html.H6("Guests", className='mb-1'),
                        daq.NumericInput(
                            id='accomadates',
                            min=1,
                            max=16,
                            value=1,
                            className='mb-4',
                        )
                ],
                width=2
                ),
                dbc.Col([
                        html.H6("Bedrooms", className='mb-1'),
                        daq.NumericInput(
                            id='bedrooms',
                            min=0,
                            max=10,
                            value=1,
                            className='mb-4',
                        )
                    ],
                    width=2
                    ),
                dbc.Col([
                        html.H6("Beds", className='mb-1'),
                        daq.NumericInput(
                            id='beds',
                            min=0,
                            max=18,
                            value=1,
                            className='mb-4',
                        ),
                    ],
                    width=2
                    ),
                dbc.Col([
                        html.H6("Bathrooms", className='mb-1'),
                        dcc.Slider(
                            id='bathrooms',
                            min=0,
                            max=8,
                            step=0.5,
                            marks=bathroom_marks,
                            value=1,
                            className='mb-4',
                        )
                    ],
                    width=6
                    ),
        dbc.Row([
                dbc.Col([
                        html.H6("Bed Type", className='mb-1'),
                        dcc.Dropdown(
                            id='bedtype',
                            options=[
                                {'label': 'Real Bed', 'value': 'Real Bed'},
                                {'label': 'Futon', 'value': 'Futon'},
                                {'label': 'Pull-out Sofa', 'value': 'Pull-out Sofa'},
                                {'label': 'Airbed', 'value': 'Airbed'},
                                {'label': 'Couch', 'value': 'Couch'},
                            ],
                            className='mb-4',
                        )],
                ),
                dbc.Col([
                        html.H6("Cancellation Policy", className='mb-1'),
                        dcc.Dropdown(
                            id='cancellation',
                            options=[
                                {'label': 'Strict', 'value': 'strict'},
                                {'label': 'Flexible', 'value': 'flexible'},
                                {'label': 'Moderate', 'value': 'moderate'},
                                {'label': 'Super Strict 30', 'value': 'super_strict_30'},
                                {'label': 'Super Strict 60', 'value': 'super_strict_60'},
                            ],
                            className='mb-4',
                        )
                    ]),
            ]
        ),
        # 6th Row. Includes city
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H6("City", className='mb-1'),
                        dcc.Dropdown(
                            id='city',
                            options=[
                                {'label': 'Bentonville', 'value': 'Bentonville'},
                                {'label': 'Rogers', 'value': 'Rogers'},
                                {'label': 'Springdale', 'value': 'Springdale'},
                                {'label': 'Bella Vista', 'value': 'Bella Vista'},
                                {'label': 'Fayetteville', 'value': 'Fayetteville'}
                            ],
                            className='mb-4',
                        ),
                    ],
                ),
            ]
        ),
        # 7th Row. Includes host_identity_verified, instant_bookable, host_since_days
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H6("Verified Host", className='mb-1'),
                        dcc.Dropdown(
                            id='bookable',
                            options=[
                                {'label': 'True', 'value': 'True'},
                                {'label': 'False', 'value': 'False'},
                            ], className='mb-4',)
                    ]
                ),
                dbc.Col(
                    [
                        html.H6("Instantly Bookable", className='mb-1'),
                        dcc.Dropdown(
                            id='verified_host',
                            options=[
                                {'label': 'True', 'value': 'True'},
                                {'label': 'False', 'value': 'False'},
                            ], className='mb-4')
                    ]
                ),
            ]
        ),
        # 9th Row. Includes amenities
        dbc.Row([
                dbc.Col([
                        html.H6("Amenities", className='mb-1'),
                        dcc.Dropdown(
                            id='room',
                            options=amenity,
                            multi=True,
                            className='mb-4',
                        )
                    ]),
                ])
            ])
        ],
        className='cards'
        )

row2 = html.Div([
    dbc.Col(
        [
            # html.Br(),
            # html.Br(),
            # html.Br(),
            # html.H4('Price Estimation', className='mr-5'),
        ]
    ),
    dbc.Col([
        dbc.Button("Predict Price", id="example-button", className="mx-5 my-5"),
        html.Div(id='container-button-timestamp'),
        html.Span(id="example-output", style={"vertical-align": "middle"}),
    ])
])


layout = dbc.Row([
    row1,
    row2
    ],
    className='mx-5 my-5'
    )
