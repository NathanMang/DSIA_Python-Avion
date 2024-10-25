

#
# Imports
#

import pandas as pd
import dash
#import dash_core_components as dcc
#import dash_html_components as html
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from histogramme import creerHist,histogram_Dynamique
#
from carte_choroplèthe_px import creerCart

#
# Main
#

if __name__ == '__main__':

    app = dash.Dash(__name__) # (3)

    
    fig = creerHist()
    
    

    #carte = creerCart()

    
    app.layout = html.Div(children=[

                            html.H1(children=f'Premier essai',
                                        style={'textAlign': 'center', 'color': '#7FDBFF'}), # (5)

                            
                            dcc.Graph(
                                id='graph1',
                                figure=fig
                            ), # (6)

                            
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
                                style={'width': '60%', 'margin-bottom': '20px'}
                            ),

                            # Graphique de l'histogramme
                            dcc.Graph(id='histogram-graph'),
                            html.Div(children=f'''blablabla'''), # (7)
    ]
    )

    @app.callback(
        Output('histogram-graph', 'figure'),
        Input('retard-type-dropdown', 'value')
    )
    def update_histogram(selected_retard_type):
        return histogram_Dynamique(selected_retard_type)
    
    # RUN APP
    #

    app.run_server(debug=True) # (8)