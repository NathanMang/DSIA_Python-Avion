"""Page router"""

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from dashboard.home_page.home_page import create_home_page
from dashboard.histogram_page.histogram_page import create_histogram_page_content, create_histogram_page_callback
from dashboard.map_page.map_page import create_map_page

def create_router_page():

    """Créé une page router"""

    app = dash.Dash(__name__)
    
    app.layout = html.Div(children=[

                                    dcc.Location(id='url', refresh=False),
                                    html.Nav(style={
                                        'display': 'flex',
                                        'justifyContent': 'center',
                                        'alignItems': 'center',
                                        'padding': '10px',
                                        'backgroundColor': '#f8f9fa',  # Couleur de fond légère
                                        'borderBottom': '1px solid #dee2e6',  # Bordure en bas
                                    }, children=[
                                        dcc.Link('Accueil', href='/', style={'margin': '0 15px', 'textDecoration': 'none', 'color': '#007bff'}),
                                        dcc.Link('Histogramme', href='/hist', style={'margin': '0 15px', 'textDecoration': 'none', 'color': '#007bff'}),
                                        dcc.Link('Carte', href='/carte', style={'margin': '0 15px', 'textDecoration': 'none', 'color': '#007bff'})
                                    ]),

                                    html.Div(id='page-content')
                        ]
    )

    # Callback pour afficher la bonne page en fonction de l'URL
    @app.callback(Output('page-content', 'children'), 
                  [Input('url', 'pathname')])
    def display_page(pathname):
        if pathname == '/':
            return create_home_page()
        elif pathname == '/hist':
            return create_histogram_page_content()
        elif pathname == '/carte':
            return create_map_page()
        else:
            return html.H1("404 - Page non trouvée")

    return app