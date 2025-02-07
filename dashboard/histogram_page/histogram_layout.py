"""Histogram layout"""
from dash import dcc, html
from dashboard.histogram_page.histogram_airline import create_histogram
from dashboard.histogram_page.histogram_type_delay import create_histogram_delay
from dashboard.histogram_page.histogram_arr_delay import create_histogram_arrival_delay

def create_histogram_layout():
    """Contenu de la page d'histogramme"""

    delay_type = 'CarrierDelay'                                             # Valeur par défaut pour l'affichage de l'histogram
    histogram_airline = create_histogram(delay_type)                                # Créé l'histogramme
    histogram_type_delay = create_histogram_delay()                                   # Créé l'histogramDelay
    min_delay,max_delay=15,30                                                # Valeur par défaut pour l'affichage de l'histogramArrDelay
    histogramArrDelay=create_histogram_arrival_delay(min_delay, max_delay)  # Créé l'histogramArrDelay

    layout = html.Div(children=[
        # En-tête
        html.H1(children='Histogrammes',
                style={'textAlign': 'center', 'color': '#007BFF', 'marginBottom': '30px', 'fontFamily': 'Arial, sans-serif'}),

        
        # RangeSlider pour ajuster la plage des retards d'arrivée (min et max)
        dcc.RangeSlider(
            id='delay-range-slider',
            min=15,     # Valeur minimum
            max=120,    # Valeur maximum
            step=1,     # Step
            marks={i: str(i) for i in range(15, 120, 5)},  # Marques de 5 en 5
            value=[15, 30],  # Valeur initiale (plage 15 à 30)
            tooltip={"placement": "bottom", "always_visible": True},  # Afficher la valeur des curseurs
        ),

        # Affichage de l'histogramArrDelay 
        dcc.Graph(
            id='histogramArrDelay',
            figure=histogramArrDelay,
            style={'marginBottom': '30px'}  # Espace sous l'histogramme
        ),

        # Description
        html.Div(children='''Cet histogramme montre la distribution des retards d'arrivée des vols aériens dans une plage de temps définie par l'utilisateur, allant de min_delay à max_delay minutes. Les données utilisées proviennent des vols ayant subi des retards en 2019, et seules les occurrences dont le nombre est supérieur à 1000 ont été retenues pour cette analyse, afin de se concentrer sur les retards les plus fréquents et de simplifier l'interprétation des résultats. L'axe des abscisses représente le nombre de minutes de retard à l'arrivée, tandis que l'axe des ordonnées indique le nombre d'occurrences pour chaque plage de retard. L'interface dynamique permet de sélectionner la plage de retards à afficher à l'aide d'un curseur, offrant ainsi une vue personnalisée de la distribution des retards dans la plage temporelle choisie.''',
            style={
                'textAlign': 'center',
                'color': '#555',
                'fontSize': '16px',
                'maxWidth': '800px',   # Limite la largeur pour une meilleure lisibilité
                'margin': '0 auto'     # Centre le texte
            }),

            
        
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
                'boxShadow': '0 2px 5px rgba(0, 0, 0, 0.1)'  # Ombre 
            }
        ),

        # Affichage de l'histogramme
        dcc.Graph(
            id='histogram-graph',
            figure=histogram_airline,
            style={'marginBottom': '30px'}  # Espace sous l'histogramme
        ),

        # Description
        html.Div(children='''Cet histogramme montre le nombre d'occurrences des retards aériens en fonction de la compagnie et du type de retard sélectionné. Le dataset contient uniquement des vols ayant subi des retards en 2019, et pour cette visualisation, seuls les vols ayant eu des retards supérieurs à 15 minutes ont été retenus. Cela signifie que chaque barre représente le nombre de retards significatifs pour chaque compagnie aérienne.

                Explorez les différentes catégories de retards pour mieux comprendre les impacts sur les horaires des vols. Utilisez le menu déroulant pour changer le type de retard affiché.''',
            style={
                'textAlign': 'center',
                'color': '#555',
                'fontSize': '16px',
                'maxWidth': '800px',   # Limite la largeur pour une meilleure lisibilité
                'margin': '0 auto'     # Centre le texte
            }),
        
        # Affichage de l'histogramDelay
        dcc.Graph(
            id='histogram-graph-2',
            figure=histogram_type_delay,
            style={'marginBottom': '30px'}  # Espace sous l'histogramme
        ),

        # Description
        html.Div(children='''Cet histogramme illustre le nombre d'occurrences pour chaque type de retard aérien, en mettant l'accent sur les retards supérieurs à 15 minutes. Cet histogramme a été créé pour permettre une visualisation claire et rapide des retards aériens par type, afin de mieux comprendre les différentes causes des retards. \n En observant les données, on peut noter une disparité significative entre les types de retards.''',
            style={
                'textAlign': 'center',
                'color': '#555',
                'fontSize': '16px',
                'maxWidth': '800px',  # Limite la largeur pour une meilleure lisibilité
                'margin': '0 auto'     # Centre le texte
            }),
        

    ], style={
        'backgroundColor': '#F8F9FA',  # Fond clair 
        'padding': '20px',
        'borderRadius': '8px',         # Coins arrondis
        'boxShadow': '0 4px 20px rgba(0, 0, 0, 0.1)',  # Ombre 
        'maxWidth': '900px',           # Limite la largeur du conteneur principal
        'margin': '40px auto 20px auto'          # Centre le conteneur principal avec un peu de marge
    })

    # Retourne le layout de la page d'histogramme
    return layout
