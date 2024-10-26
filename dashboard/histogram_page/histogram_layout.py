"""Histogram layout"""

from dash import dcc, html
from dashboard.histogram_page.histogram import create_histogram

def create_histogram_layout():

    """Contenue de histogram page"""

    delay_type = 'CarrierDelay'
    histogram = create_histogram(delay_type) # Créé l'histogramme
    
    layout =  html.Div(children=[

                            # En-tête
                            html.H1(children='Histogram page',
                                        style={'textAlign': 'center', 'color': '#7FDBFF'}),

                            # Menu déroulant pour sélectionner le type de retard
                            dcc.Dropdown(
                                id='retard-type-dropdown',
                                options=[
                                    {'label': 'CarrierDelay - Retard du transporteur', 'value': 'CarrierDelay'},
                                    {'label': 'WeatherDelay - Retard météorologique', 'value': 'WeatherDelay'},
                                    {'label': 'NASDelay - Retard du système national d\'aviation', 'value': 'NASDelay'},
                                    {'label': 'SecurityDelay - Retard de sécurité', 'value': 'SecurityDelay'},
                                    {'label': 'LateAircraftDelay - Retard d\'arrivée tardive de l\'appareil', 'value': 'LateAircraftDelay'}
                                ],
                                value='CarrierDelay',  # Valeur par défaut
                                clearable=False,
                                style={'width': '60%', 'margin-bottom': '20px'} # Style
                            ),

                            # Affichage de l'histogramme
                            dcc.Graph(
                                id='histogram-graph',
                                figure=histogram
                            ),

                            # Descritpion
                            html.Div(children='''blablabla''')
                    ]
    )

    # Retourne le layout de histogram page
    return layout