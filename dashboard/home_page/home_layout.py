"""Home layout"""

from dash import html

def create_home_layout():

    """Contenue de home_page"""
    
    layout = html.Div(children=[

                            # En-tête
                            html.H1(children='Home Page', style={'textAlign': 'center', 'color': '#7FDBFF'}),

                            # Description
                            html.Div(children='''blablabla''')
                    ]
    )

    # Retourne le layout de home page
    return layout