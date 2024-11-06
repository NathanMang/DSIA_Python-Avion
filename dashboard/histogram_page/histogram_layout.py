from dash import dcc, html
from dashboard.histogram_page.histogram import create_histogram
from dashboard.histogram_page.histogram2 import create_histogram_delay
from dashboard.histogram_page.histogramArrDelay import create_histogram_arrival_delay

def create_histogram_layout():
    """Contenu de la page d'histogramme"""

    delay_type = 'CarrierDelay'
    histogram = create_histogram(delay_type)  # Créé l'histogramme
    histogram2 = create_histogram_delay()  # Créé l'histogramme
    histogramArrDelay=create_histogram_arrival_delay()

    layout = html.Div(children=[
        # En-tête
        html.H1(children='Histogramme des Retards Aériens par Compagnie',
                style={'textAlign': 'center', 'color': '#007BFF', 'marginBottom': '30px', 'fontFamily': 'Arial, sans-serif'}),

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


        dcc.Graph(
            id='histogramArrDelay',
            figure=histogramArrDelay,
            style={'marginBottom': '30px'}  # Espace sous l'histogramme
        ),

        # Description
        html.Div(children='''Cet histogramme illustre la répartition des retards d'arrivée des vols aériens, en se concentrant sur ceux ayant des retards supérieurs à 15 minutes. Les données proviennent des vols aériens ayant subi des retards en 2019, et seules les retards ayant plus de 6000 occurrences sont affichées ici. Nous choisissons de visualiser uniquement les retards d'arrivée ayant plus de 6000 occurrences afin de se concentrer sur les retards les plus fréquents et de simplifier l'analyse. Les retards moins fréquents, bien qu'intéressants, peuvent occuper une portion trop petite de l'histogramme. Chaque barre représente le nombre d'occurrences pour un retard d'arrivée spécifique, mettant en lumière les retards les plus fréquents dans cette plage. Cette visualisation permet d'explorer l'impact des différents retards d'arrivée sur les horaires des vols et d'obtenir une vue d'ensemble sur la distribution de ces retards significatifs.''',
            style={
                'textAlign': 'center',
                'color': '#555',
                'fontSize': '16px',
                'maxWidth': '800px',   # Limite la largeur pour une meilleure lisibilité
                'margin': '0 auto'     # Centre le texte
            }),

        # Affichage de l'histogramme
        dcc.Graph(
            id='histogram-graph',
            figure=histogram,
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

        dcc.Graph(
            id='histogram-graph-2',
            figure=histogram2,
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
        'margin': '20px auto'          # Centre le conteneur principal avec un peu de marge
    })

    # Retourne le layout de la page d'histogramme
    return layout
