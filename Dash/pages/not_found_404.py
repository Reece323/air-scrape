from dash import html
import dash

dash.register_page(__name__, path="/404")


layout = html.Center(html.H1("Custom 404"))