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
from histogramme import creerHist
from carte_choroplèthe_px import creerCart
#
# Main
#

if __name__ == '__main__':

    app = dash.Dash(__name__) # (3)

    month = 1
    fig = creerHist(month)
    

    carte = creerCart()

    
    app.layout = html.Div(children=[

                            html.H1(children=f'Premier essai',
                                        style={'textAlign': 'center', 'color': '#7FDBFF'}), # (5)

                            html.Label('Month'),
                            dcc.Slider(
                                id='month-slider',
                                min=1,
                                max=6,
                                step=1,
                                value=1
                            ),

                            dcc.Graph(
                                id='graph1',
                                figure=fig
                            ), # (6)

                            dcc.Graph(
                                id='graph2',
                                figure=carte
                            ), # (6)

                            html.Div(children=f'''blablabla'''), # (7)
    ]
    )

    @app.callback(
        Output(component_id='graph1', component_property='figure'),
        [Input(component_id='month-slider', component_property='value')]
    )
    def update_figure(input_value):
        return creerHist(input_value)
    #
    # RUN APP
    #

    app.run_server(debug=True) # (8)

