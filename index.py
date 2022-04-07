import dash
import dash_bootstrap_components as dbc
import dash_labs as dl
from dash import html
from app import app, server

carousel = dbc.Row([
    dbc.Col([
            dbc.Carousel(
                items=[
                    {
                        "key": "1", "src": "/assets/airbnb_logo.png",
                        "img_style":{"max-height": "180px", 'max-width': '180px'}
                    },
                    {
                        "key": "2", "src": "/assets/air5.png",
                        "img_style":{"max-height":"180px", 'max-width': '180px'}
                        },
                    {
                        "key": "3", "src": "/assets/air6.png",
                        "img_style":{"max-height":"180px", 'max-width': '180px'}},
                ],
                controls=False,
                indicators=False,
                interval=8000,
                ride="carousel",
                className="logo animate__animated animate__infinite infinite carousel-fade my-element"
                )
            ],
            width=12
        )
    ]
)

items = [
                dbc.DropdownMenuItem(page["name"], href=page["path"],
                className='drop')
                for page in dash.page_registry.values()
                if page["module"] != "pages.not_found_404"
        ]


nav_contents = [
    dbc.NavItem([
        dbc.DropdownMenu(
            label='More Features',
            children = items,
            direction='down',
            className='noborder',
            toggle_style={
                "background": "rgba(255, 90, 95, .41)",
                'border-radius':'15px'
            },
            toggleClassName="fst-italic",
            )
        ]
        
    )
]

navbar = dbc.NavbarSimple(
    nav_contents,
    color='transparent'
)


########################
#########LAYOUT#########
########################

app.layout = html.Div(
    [
        navbar,
        carousel,
        dl.plugins.page_container
        
    ],
    style={'height':'100vh'},
    # fluid=True,
)

if __name__ == "__main__":
    app.run_server(debug=True, port=8099)
