"""Histogram page"""

from dash import dcc, html
from dash.dependencies import Input, Output
from dashboard.histogram_page.histogram import create_histogram

def create_histogram_page_content():

    """Contenue de histogram page"""

    histogram = create_histogram() # Créé l'histogramme
    
    
    return html.Div(children=[

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

def create_histogram_page_callback(app):

    """Callback de histogram page"""

    # Callback / Interaction dynamique
    @app.callback(
        Output(component_id='histogram-graph', component_property='figure'),        # Composant à mettre à jour selon la valeur d'entrée (histogramme)
        [Input(component_id='retard-type-dropdown', component_property='value')]    # Entrée de la valeur (Type de retard sélectionner)
    )
    def update_histogram(selected_retard_type):

        """Mise à jour du composant"""

        # Retourne le nouveau histogramme
        return create_histogram(selected_retard_type)