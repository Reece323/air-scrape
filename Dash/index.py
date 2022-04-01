import dash
import dash_labs as dl
import dash_bootstrap_components as dbc

from app import app
from app import server


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
                dbc.DropdownMenuItem(page["name"], href=page["path"])
                for page in dash.page_registry.values()
                if page["module"] != "pages.not_found_404"
        ]


nav_contents = [
    dbc.NavItem([
        dbc.DropdownMenu(
            label='More Features',
            children = items,
            direction='down',
            className='',
            toggle_style={
                "background": "rgba(255, 90, 95, 1)"
            },
            toggleClassName="fst-italic border border-dark",
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

app.layout = dbc.Container(
    [
        navbar,
        carousel,
        dl.plugins.page_container
        
    ],
    fluid=True,
)

if __name__ == "__main__":
    app.run_server(debug=True, port=8001)