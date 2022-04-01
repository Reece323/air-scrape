import dash
import dash_bootstrap_components as dbc
import dash_labs as dl  # pip install dash-labs

app = dash.Dash(
    __name__,
    plugins=[dl.plugins.pages],
    external_stylesheets=[
        dbc.themes.SUPERHERO,
        'https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css'],
        suppress_callback_exceptions=True,
        meta_tags=[{'name': 'viewport',
        'content': 'width=device-width, initial-scale=1.0'}]
    )

server = app.server
