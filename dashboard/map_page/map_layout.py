"""Map layout"""

from dash import html
from dashboard.map_page.map import create_map

def create_map_layout():

    """Contenue de map_page """
    
    create_map() # Créé la carte
    
    layout = html.Div(children=[

                            # En-tête
                            html.H1(children='Map page',
                                        style={'textAlign': 'center', 'color': '#7FDBFF'}),

                            # Affichage de la carte
                            html.Iframe(id='map', srcDoc = open('dashboard/map_page/map.html', "r", encoding="utf-8").read(),
                                        width="100%", height="600"),

                            # Description
                            html.Div(children='''blablabla''')
                    ]
    )

    # Retourne le layout de map page
    return layout