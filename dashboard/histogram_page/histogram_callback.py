"""Histogram callback"""

from dash.dependencies import Input, Output
from dashboard.histogram_page.histogram_layout import create_histogram, create_histogram_arrival_delay

def create_histogram_callback(app):

    """Callback de histogram page"""

    # Callback / Interaction dynamique
    @app.callback(
        Output(component_id='histogram-graph', component_property='figure'),        # Composant à mettre à jour selon la valeur d'entrée (histogramme)
        [Input(component_id='retard-type-dropdown', component_property='value')]    # Entrée de la valeur (Type de retard sélectionner)
    )
    def update_histogram(selected_retard_type):

        """Mise à jour du composant (histogramme)"""

        # Retourne le nouveau histogramme
        return create_histogram(selected_retard_type)

    # callback pour l'histogramme dynamique basé sur la plage de retards d'arrivée
    @app.callback(
        Output('histogramArrDelay', 'figure'),  # Composant à mettre à jour selon la valeur d'entrée (histogramArrDelay)
        Input('delay-range-slider', 'value')    # Entrée de la valeur (Intervalles de minutes)
    )
    def update_arrival_delay_histogram(selected_range):

        """Mise à jour du composant (histogrammeArrDelay)"""

        min_delay, max_delay = selected_range                       # Récupérer min et max à partir du range slider
        return create_histogram_arrival_delay(min_delay, max_delay) # # Retourne le nouveau histogramArrDelay