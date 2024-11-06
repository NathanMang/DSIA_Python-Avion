"""Map layout"""

from dash import html
from dashboard.map_page.map import create_map
#MAP 
def create_map_layout():
    """Contenu de map_page """
    
    create_map()  # Crée la carte
    
    layout = html.Div(children=[
        # En-tête
        html.H1(children='Page de la Carte',
                style={'textAlign': 'center', 'color': '#007BFF', 'margin-bottom': '10px'}),
        
        # Sous-titre
        html.H2(children='Temps moyen pour décoller après embarquement total par aéroport (TaxiOut)',
                style={'textAlign': 'center', 'color': '#0056b3', 'margin-bottom': '30px'}),  # Ajout d'un sous-titre

        # Affichage de la carte
        html.Iframe(id='map', 
                    srcDoc=open('dashboard/map_page/map.html', "r", encoding="utf-8").read(),
                    width="100%", 
                    height="600",
                    style={'border': 'none', 'box-shadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'margin-bottom': '30px'}),

        # Description
        html.Div(children='''
            Cette carte présente les 40 aéroports américains ayant le plus de vols en 2019. 
            Explorez les temps moyens de décollage après l'embarquement pour mieux comprendre les 
            performances des différents aéroports. 
            Utilisez la carte interactive pour visualiser les données géographiques et identifier les tendances.
        ''', 
        style={'textAlign': 'center', 'color': '#555', 'fontSize': '16px', 'margin': '0 auto', 'width': '80%'}),
        
        # Footer
        html.Div(children='''© 2024 - Dashboard de Retards Aériens - Mang Nathan & Ludovic Viellard''', 
                 style={'textAlign': 'center', 'color': '#777', 'fontSize': '14px', 'margin-top': '50px'})
    ], style={'backgroundColor': '#F8F9FA', 'padding': '20px'})

    # Retourne le layout de map page
    return layout
