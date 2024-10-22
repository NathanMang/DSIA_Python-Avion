#
# Imports
#

import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html

from histogramme import creerHist
from carte_choroplèthe_px import creerCart
#
# Main
#

if __name__ == '__main__':

    app = dash.Dash(__name__) # (3)

    fig = creerHist()

    carte = creerCart()

    
    app.layout = html.Div(children=[

                            html.H1(children=f'Premier essai',
                                        style={'textAlign': 'center', 'color': '#7FDBFF'}), # (5)

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

    #
    # RUN APP
    #

    app.run_server(debug=True) # (8)