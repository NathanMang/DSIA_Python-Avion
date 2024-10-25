"""Home page"""

from dash import html

def create_home_page():

    """Contenue de home_page"""
    
    return html.Div(children=[

                            # En-tête
                            html.H1(children='Home Page', style={'textAlign': 'center', 'color': '#7FDBFF'}),

                            # Description
                            html.Div(children='''blablabla''')
                    ]
    )