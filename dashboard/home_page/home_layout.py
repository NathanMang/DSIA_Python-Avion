from dash import html

def create_home_layout():
    """Contenu de la page d'accueil"""

    layout = html.Div(children=[ 
        # En-tête
        html.H1(children='Bienvenue sur le Dashboard de Retards Aériens',
                className="fadeIn",
                style={ 
                    'textAlign': 'center',
                    'color': '#007BFF',
                    'marginBottom': '20px',
                    'fontFamily': 'Arial, sans-serif',
                }),

        # Description
        html.Div(children=''' 
            Ce dashboard interactif vous permet d'analyser les retards des vols aériens en fonction de plusieurs critères.
            Explorez les données pour mieux comprendre les impacts des conditions météorologiques, des compagnies aériennes 
            et d'autres facteurs sur les retards de vol. 
            Utilisez les fonctionnalités ci-dessus pour naviguer à travers les différentes visualisations et statistiques.
        ''', className="fadeIn", style={
            'textAlign': 'center',
            'color': '#555',
            'fontSize': '18px',
            'marginBottom': '30px',
            'lineHeight': '1.6',
            'maxWidth': '800px',
            'margin': '0 auto',
            'padding': '10px',
            'backgroundColor': '#f0f8ff',
            'borderRadius': '8px',
            'boxShadow': '0 2px 10px rgba(0, 0, 0, 0.1)',
            'transition': 'transform 0.3s'
        }),

        # Image illustrative
        html.Img(src='https://i.topito.com/pSCBxE1Pferq4l9m4XB7GpsfzVk_-0rm9t3InmCfjXo=/1340x704/smart/filters:fill(white):format(webp):quality(70)/https%3A%2F%2Fmedia.topito.com%2Fwp-content%2Fuploads%2F2017%2F04%2Ftop-retard-avion.jpg', 
                 style={'width': '75%', 
                        'height': 'auto', 
                        'display': 'block', 
                        'margin': '0 auto'
                        }
                ),

        # Footer
        html.Div(children='''© 2024 - Dashboard de Retards Aériens - Mang Nathan & Ludovic Viellard''',
                 className="fadeIn",
                 style={ 
                     'textAlign': 'center',
                     'color': '#777',
                     'fontSize': '14px',
                     'marginTop': '50px',
                     'fontFamily': 'Arial, sans-serif'
                 })
    ], style={ 
        'backgroundColor': '#F8F9FA',
        'padding': '20px',
        'borderRadius': '8px',
        'boxShadow': '0 4px 20px rgba(0, 0, 0, 0.1)',
        'maxWidth': '900px',
        'margin': '0 auto'
        
    })

    return layout
