"""Histogram callback"""

from dash.dependencies import Input, Output
from dashboard.histogram_page.histogram_layout import create_histogram
#Callback
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