"""Page router"""

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from dashboard.home_page.home_layout import create_home_layout
from dashboard.histogram_page.histogram_layout import create_histogram_layout
from dashboard.map_page.map_layout import create_map_layout

def create_router_page():

    """Créé une page router"""

    # Créer l'application
    app = dash.Dash(__name__, suppress_callback_exceptions=True)
    
    # Créer le contenur de la page
    app.layout = html.Div(children=[

                                    dcc.Location(id='url', refresh=False),
                                    html.Nav(

                                        # Style de la barre de navigation
                                        style={
                                        'display': 'flex',
                                        'justifyContent': 'center',
                                        'alignItems': 'center',
                                        'padding': '15px 0',
                                        'backgroundColor': '#ffffff',       # Fond blanc
                                        'borderBottom': '2px solid #e0e0e0',# Ligne de séparation douce en bas
                                        'boxShadow': '0px 4px 6px rgba(0, 0, 0, 0.1)'  # Légère ombre pour la profondeur
                                        }, 

                                        # Liste des liens
                                        children=[
                                        dcc.Link(
                                            'Accueil', 
                                            href='/', 
                                            style={
                                                'margin': '0 20px', 
                                                'textDecoration': 'none', 
                                                'color': '#007bff',                 # Bleu pour les liens
                                                'fontWeight': 'bold',               # Texte gras
                                                'fontSize': '16px',
                                                'transition': 'color 0.3s ease'     # Transition douce pour le changement de couleur
                                            },
                                            # Effet au survol
                                            className='nav-link'
                                        ),
                                            
                                        dcc.Link(
                                            'Histogramme', 
                                            href='/hist', 
                                            style={
                                                'margin': '0 20px', 
                                                'textDecoration': 'none', 
                                                'color': '#007bff', 
                                                'fontWeight': 'bold',
                                                'fontSize': '16px',
                                                'transition': 'color 0.3s ease'
                                            },
                                            className='nav-link'
                                        ),
                                        
                                        dcc.Link(
                                            'Carte', 
                                            href='/carte', 
                                            style={
                                                'margin': '0 20px', 
                                                'textDecoration': 'none', 
                                                'color': '#007bff', 
                                                'fontWeight': 'bold',
                                                'fontSize': '16px',
                                                'transition': 'color 0.3s ease'
                                            },
                                            className='nav-link'
                                        )
                                        ]
                                    ),

                                    
                                    
                                    # Reste du contenue
                                    html.Div(id='page-content')
                        ]
                    )

    # Callback pour afficher la bonne page en fonction de l'URL
    @app.callback(Output('page-content', 'children'), 
                  [Input('url', 'pathname')])
    def display_page(pathname):
        if pathname == '/':
            return create_home_layout()
        elif pathname == '/hist':
            return create_histogram_layout()
        elif pathname == '/carte':
            return create_map_layout()
        else:
            return html.H1("404 - Page non trouvée")

    return app