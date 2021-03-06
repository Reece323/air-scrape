import dash
import plotly.express as px
dash.register_page(__name__)
df = px.data.iris()
from plotly import graph_objects as go
import dash_bootstrap_components as dbc
from dash import dcc, html

TEXT_STYLE = {
    'textAlign': 'center',
    'color': 'white'
}

CARD_TEXT_STYLE = {
    'textAlign': 'center',
    'color': 'white'
}

# the style arguments for the main content page.
CONTENT_STYLE = {
    'margin-left': '4rem',
    'margin-right': '4rem',
    'top': 0,
    'padding': '20px 10px'
}




content_first_row = dbc.Row([
    dbc.Col(
        dbc.Card(
            [

                dbc.CardBody(
                    [
                        html.H4(id='card_title_1', children=['Card Title 1'], className='card-title',
                                style=CARD_TEXT_STYLE),
                        html.P(id='card_text_1', children=['Sample text.'], style=CARD_TEXT_STYLE),
                    ]
                )
            ], className='cards'
        ),
        md=3
    ),
    dbc.Col(
        dbc.Card(
            [

                dbc.CardBody(
                    [
                        html.H4('Card Title 2', className='card-title', style=CARD_TEXT_STYLE),
                        html.P('Sample text.', style=CARD_TEXT_STYLE),
                    ]
                ),
            ], className='cards'

        ),
        md=3
    ),
    dbc.Col(
        dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H4('Card Title 3', className='card-title', style=CARD_TEXT_STYLE),
                        html.P('Sample text.', style=CARD_TEXT_STYLE),
                    ]
                ),
            ], className='cards'

        ),
        md=3
    ),
    dbc.Col(
        dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H4('Card Title 4', className='card-title', style=CARD_TEXT_STYLE),
                        html.P('Sample text.', style=CARD_TEXT_STYLE),
                    ]
                ),
            ], className='cards'
        ),
        md=3
    )
])


content_second_row = dbc.Row(
    [
        dbc.Col(
            dcc.Graph(
                id='graph_1',
                figure={
                    # 'data':df,
                    'layout': go.Layout(
                        paper_bgcolor='rgba(0,0,0,.6)',
                        plot_bgcolor='rgba(0,0,0,.8)'
                        )
                    }
                ), md=4
        ),
        dbc.Col(
            dcc.Graph(id='graph_2',
            figure={
                    # 'data':df,
                    'layout': go.Layout(
                        paper_bgcolor='rgba(0,0,0,.6)',
                        plot_bgcolor='rgba(0,0,0,.8)'
                        )
                    }), md=4
        ),
        dbc.Col(
            dcc.Graph(id='graph_3',
            figure={
                    # 'data':df,
                    'layout': go.Layout(
                        paper_bgcolor='rgba(0,0,0,.6)',
                        plot_bgcolor='rgba(0,0,0,.8)'
                        )
                    }), md=4
        )
    ]
)



content_third_row = dbc.Row(
    [
        dbc.Col(
            dcc.Graph(id='graph_4',
            figure={
                    # 'data':df,
                    'layout': go.Layout(
                        paper_bgcolor='rgba(0,0,0,.6)',
                        plot_bgcolor='rgba(0,0,0,.8)'
                        )
                    }), md=12,
        )
    ]
)


content_fourth_row = dbc.Row(
    [
        dbc.Col(
            dcc.Graph(id='graph_5',figure={
                    # 'data':df,
                    'layout': go.Layout(
                        paper_bgcolor='rgba(0,0,0,.6)',
                        plot_bgcolor='rgba(0,0,0,.8)'
                        )
                    }), md=6
        ),
        dbc.Col(
            dcc.Graph(id='graph_6',
            figure={
                    # 'data':df,
                    'layout': go.Layout(
                        paper_bgcolor='rgba(0,0,0,.6)',
                        plot_bgcolor='rgba(0,0,0,.8)'
                        )
                    }), md=6
        )
    ]
)

content = html.Div(
    [
        html.H2('Analytics Dashboard', style=TEXT_STYLE),
        html.Hr(),
        html.Hr(),
        content_first_row,
        html.Hr(),
        content_second_row,
        html.Hr(),
        content_third_row,
        html.Hr(),
        content_fourth_row
    ],
    style=CONTENT_STYLE,
    className='mx-5 my-5'
)

layout = content
