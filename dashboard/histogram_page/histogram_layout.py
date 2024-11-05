from dash import dcc, html
from dashboard.histogram_page.histogram import create_histogram

def create_histogram_layout():
    """Contenu de la page d'histogramme"""

    delay_type = 'CarrierDelay'
    histogram = create_histogram(delay_type)  # Créé l'histogramme

    layout = html.Div(children=[
        # En-tête
        html.H1(children='Histogramme des Retards Aériens par Compagnie',
                style={'textAlign': 'center', 'color': '#007BFF', 'margin-bottom': '30px', 'fontFamily': 'Arial, sans-serif'}),

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
            style={
                'width': '60%', 
                'margin': '0 auto 20px auto',  # Centre le dropdown avec marges
                'padding': '10px',              # Ajoute un peu de padding
                'fontSize': '16px',             # Agrandit le texte
                'borderRadius': '5px',          # Coins arrondis
                'boxShadow': '0 2px 5px rgba(0, 0, 0, 0.1)'  # Ombre douce
            }
        ),

        # Affichage de l'histogramme
        dcc.Graph(
            id='histogram-graph',
            figure=histogram,
            style={'margin-bottom': '30px'}  # Espace sous l'histogramme
        ),

        # Description
        html.Div(children='''Cet histogramme montre le nombre d\'occurrences des retards aériens en fonction de la compagnie 
            et du type de retard sélectionné. Explorez les différentes catégories de retards pour mieux comprendre 
            les impacts sur les horaires des vols. Utilisez le menu déroulant pour changer le type de retard affiché.''',
            style={
                'textAlign': 'center',
                'color': '#555',
                'fontSize': '16px',
                'maxWidth': '800px',  # Limite la largeur pour une meilleure lisibilité
                'margin': '0 auto'     # Centre le texte
            })
    ], style={
        'backgroundColor': '#F8F9FA',  # Fond clair pour le conteneur
        'padding': '20px',
        'borderRadius': '8px',         # Coins arrondis
        'boxShadow': '0 4px 20px rgba(0, 0, 0, 0.1)',  # Ombre douce pour le conteneur principal
        'maxWidth': '900px',           # Limite la largeur du conteneur principal
        'margin': '20px auto'          # Centre le conteneur principal avec un peu de marge
    })

    # Retourne le layout de la page d'histogramme
    return layout
