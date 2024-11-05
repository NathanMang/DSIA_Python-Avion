from dash import html, dcc

def create_home_layout():
    """Contenu de home_page"""

    layout = html.Div(children=[
        # En-tête
        html.H1(children='Bienvenue sur le Dashboard de Retards Aériens',
                style={
                    'textAlign': 'center',
                    'color': '#007BFF',
                    'margin-bottom': '20px',
                    'fontFamily': 'Arial, sans-serif',
                    'animation': 'fadeIn 1s'  # Animation d'apparition
                }),

        # Description
        html.Div(children='''
            Ce dashboard interactif vous permet d'analyser les retards des vols aériens en fonction de plusieurs critères.
            Explorez les données pour mieux comprendre les impacts des conditions météorologiques, des compagnies aériennes 
            et d'autres facteurs sur les retards de vol. 
            Utilisez les fonctionnalités ci-dessus pour naviguer à travers les différentes visualisations et statistiques.
        ''', style={
            'textAlign': 'center',
            'color': '#555',
            'fontSize': '18px',
            'margin-bottom': '30px',
            'lineHeight': '1.6',
            'maxWidth': '800px',  # Limite la largeur pour une meilleure lisibilité
            'margin': '0 auto',    # Centre le texte
            'padding': '10px',     # Ajoute un peu d'espace autour du texte
            'backgroundColor': '#f0f8ff',  # Couleur d'arrière-plan léger
            'borderRadius': '8px',  # Coins arrondis pour la description
            'boxShadow': '0 2px 10px rgba(0, 0, 0, 0.1)',  # Ombre douce
            'transition': 'transform 0.3s'  # Transition pour l'interaction
        }),

        # Image illustrative
        html.Img(id='home-image',src='../images/Avion.jpeg',
                  style={
                      'display': 'block',
                      'margin': '0 auto',
                      'width': '50%',
                      'margin-top': '20px',
                      'borderRadius': '10px',  # Coins arrondis
                      'boxShadow': '0 4px 10px rgba(0, 0, 0, 0.1)',  # Ombre douce
                      'transition': 'transform 0.3s'  # Transition pour l'image
                  }),

        # Footer
        html.Div(children='''© 2024 - Dashboard de Retards Aériens - Mang Nathan & Ludovic Viellard''',
                 style={
                     'textAlign': 'center',
                     'color': '#777',
                     'fontSize': '14px',
                     'margin-top': '50px',
                     'fontFamily': 'Arial, sans-serif'
                 })
    ], style={
        'backgroundColor': '#F8F9FA',
        'padding': '20px',
        'borderRadius': '8px',  # Coins arrondis pour le conteneur principal
        'boxShadow': '0 4px 20px rgba(0, 0, 0, 0.1)',  # Ombre douce pour le conteneur principal
        'maxWidth': '900px',    # Limite la largeur du conteneur principal
        'margin': '0 auto',      # Centre le conteneur principal
        'animation': 'fadeIn 1s'  # Animation d'apparition pour le conteneur principal
    })

   
    

    # Retourne le layout de la page d'accueil
    return layout
