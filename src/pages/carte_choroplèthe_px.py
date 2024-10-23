import plotly.express as px
import pandas as pd
import folium
from folium import Choropleth
import json
import numpy as np
import plotly.io as pio

'''

def creerCart():
    # Chargement des données
    df_Final = pd.read_csv('data//clean//Flight_Delay_clean.csv')
    CoordAirports = pd.read_csv('data//raw//CoordAirports.csv')
    
    # Sélection des 40 aéroports les plus fréquentés
    top_40_airports = df_Final['Origin'].value_counts().nlargest(40).index
    df_top_40 = df_Final[df_Final['Origin'].isin(top_40_airports)]
    
    # Nettoyage des colonnes
    df_top_40.loc[:, 'Origin'] = df_top_40['Origin'].str.strip().str.upper()    
    CoordAirports['LOCID'] = CoordAirports['LOCID'].str.strip().str.upper()

    # Association des coordonnées des aéroports
    df_top_40_with_coords = df_top_40.merge(CoordAirports[['LOCID', 'LATITUDE', 'LONGITUDE']], 
                                            left_on='Origin', right_on='LOCID', how='left')

    # Suppression de la colonne LOCID
    df_top_40_with_coords = df_top_40_with_coords.drop('LOCID', axis=1)
    
    # Calcul du retard moyen (TaxiOut) par aéroport
    avg_taxiout_by_airport = df_top_40_with_coords.groupby('Origin')['TaxiOut'].mean().reset_index()
    avg_taxiout_by_airport['TaxiOut'] = avg_taxiout_by_airport['TaxiOut'].round(2)

    # Ajouter les coordonnées dans le DataFrame
    avg_taxiout_by_airport = avg_taxiout_by_airport.merge(
        df_top_40_with_coords[['Origin', 'LATITUDE', 'LONGITUDE']], 
        on='Origin', how='left'
    )

    # Créer la carte avec Plotly Express
    fig = px.scatter_geo(avg_taxiout_by_airport,
                         lat='LATITUDE',
                         lon='LONGITUDE',
                         size='TaxiOut',  # La taille est proportionnelle au temps moyen
                         hover_name='Origin',
                         hover_data={'TaxiOut': True},
                         title="Temps moyen de décollage après embarquement (TaxiOut) par aéroport",
                         )
    
  
    # Définir la couleur en fonction du temps d'embarquement
    fig.update_traces(marker=dict(
        size=avg_taxiout_by_airport['TaxiOut'] * 2,  # Ajuste la taille
        color=avg_taxiout_by_airport['TaxiOut'],
        colorscale=[
            [0, 'green'],  # Moins de 15 min
            [0.375, 'yellow'],  # Entre 15 et 20 min
            [0.75, 'orange'],  # Entre 20 et 30 min
            [1, 'red']  # Plus de 30 min
        ],
        colorbar=dict(
            title="Temps moyen (minutes)",
            tickvals=[10, 15, 20, 30, 40],
            ticktext=['< 15 min', '15-20 min', '20-30 min', '> 30 min']
        )
    ))

     

    # Ajuster les marges et ajouter un titre
    fig.update_layout(
        margin={"r": 0, "t": 50, "l": 0, "b": 0},  # Ajustement des marges
        title={
            'text': "Temps moyen d'un décollage après embarquement par aéroport (TaxiOut)",
            'y': 0.9,  # Position verticale du titre
            'x': 0.5,  # Centrer le titre
            'xanchor': 'center',
            'yanchor': 'top'
        }
    )

    return fig
'''
def creerCart():
    # Chargement des données
    df_Final = pd.read_csv('data//clean//Flight_Delay_clean.csv')
    
    df_Final_filtered=df_Final.filter(items=['TaxiOut','Origin'])
    
    CoordAirports = pd.read_csv('data//clean//CoordAirportsClean.csv')

    # Sélection des 40 aéroports les plus fréquentés
    top_40_airports =  df_Final_filtered['Origin'].value_counts().nlargest(40).index
    df_top_40 =  df_Final_filtered[ df_Final_filtered['Origin'].isin(top_40_airports)]

    # Nettoyage des colonnes
    df_top_40.loc[:, 'Origin'] = df_top_40['Origin'].str.strip().str.upper()    
    CoordAirports['LOCID'] = CoordAirports['LOCID'].str.strip().str.upper()

    # Association des coordonnées des aéroports
    df_top_40_with_coords = df_top_40.merge(CoordAirports[['LOCID', 'LATITUDE', 'LONGITUDE']], 
                                            left_on='Origin', right_on='LOCID', how='left')

    # Suppression de la colonne LOCID
    df_top_40_with_coords = df_top_40_with_coords.drop('LOCID', axis=1)

    # Calcul du retard moyen (TaxiOut) par aéroport
    avg_taxiout_by_airport = df_top_40_with_coords.groupby('Origin')['TaxiOut'].mean().reset_index()
    avg_taxiout_by_airport['TaxiOut'] = avg_taxiout_by_airport['TaxiOut'].round(2)

    # Ajouter les coordonnées dans le DataFrame
    avg_taxiout_by_airport = avg_taxiout_by_airport.merge(
        df_top_40_with_coords[['Origin', 'LATITUDE', 'LONGITUDE']], 
        on='Origin', how='left'
    )


    # Créer la carte avec Plotly Express
    fig = px.scatter_geo(avg_taxiout_by_airport,
                         lat='LATITUDE',
                         lon='LONGITUDE',
                         size='TaxiOut',  # La taille est proportionnelle au temps moyen
                         hover_name='Origin',
                         hover_data={'TaxiOut': True},
                         title="Temps moyen de décollage après embarquement (TaxiOut) par aéroport",
                         scope='usa',  # Limiter l'affichage aux États-Unis
                         color='TaxiOut',  # Couleur basée sur le temps moyen
                         color_continuous_scale=[
                             [0, 'green'],  # Moins de 15 min
                             [0.375, 'yellow'],  # Entre 15 et 20 min
                             [0.75, 'orange'],  # Entre 20 et 30 min
                             [1, 'red']  # Plus de 30 min
                         ],
                         size_max=30  # Taille maximale des cercles
                         )

    # Ajuster les marges et ajouter un titre
    fig.update_layout(
        margin={"r": 0, "t": 50, "l": 0, "b": 0},  # Ajustement des marges
        title={
            'text': "Temps moyen d'un décollage après embarquement par aéroport (TaxiOut)",
            'y': 0.9,  # Position verticale du titre
            'x': 0.5,  # Centrer le titre
            'xanchor': 'center',
            'yanchor': 'top'
        }
    )

    return fig






