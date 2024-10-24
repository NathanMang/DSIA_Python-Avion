import plotly.express as px
import pandas as pd
import folium
from folium import Choropleth
import json
import numpy as np
import plotly.io as pio

def ajouter_marqueur(row, map_obj):
    # Définir la couleur du délai 
    taxi_out = row['TaxiOut']
    if taxi_out < 15:
        color = 'green'
    elif taxi_out < 20:
        color = 'yellow'
    elif taxi_out < 30:
        color = 'orange'
    else:
        color = 'red'

    # Ajouter le marqueur à la carte
    folium.CircleMarker(
        location=[row['LATITUDE'], row['LONGITUDE']],
        radius=row['TaxiOut'] / 2,  # Taille du cercle proportionnelle au temps de taxiOut
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.6,
        popup=f"{row['Origin']}: {row['TaxiOut']} min",
    ).add_to(map_obj)

def creerCart():
    # Chargement des données
    avg_taxiout_by_airport = pd.read_csv('data//clean//DataPourCarte.csv')

    # Créer une carte centrée sur les États-Unis
    map_center = [39.8283, -98.5795]  # Coordonnées du centre des États-Unis
    m = folium.Map(location=map_center, tiles='OpenStreetMap', zoom_start=4)

    # Ajouter tous les marqueurs 
    avg_taxiout_by_airport.apply(lambda row: ajouter_marqueur(row, m), axis=1)

    # Ajouter une légende 
    legend_html = '''
     <div style="position: fixed; bottom: 50px; left: 50px; width: 160px; height: auto;
                 border:2px solid grey; z-index:9999; font-size:14px; background-color:white;
                 padding:10px; opacity: 0.9;">
     <b>Légende</b><br>
     <i style="background:green;width:20px;height:20px;border-radius:50%;display:inline-block;"></i> Moins de 15 min<br>
     <i style="background:yellow;width:20px;height:20px;border-radius:50%;display:inline-block;"></i> 15-20 min<br>
     <i style="background:orange;width:20px;height:20px;border-radius:50%;display:inline-block;"></i> 20-30 min<br>
     <i style="background:red;width:20px;height:20px;border-radius:50%;display:inline-block;"></i> Plus de 30 min<br>
     </div>
    '''
    m.get_root().html.add_child(folium.Element(legend_html))

    # Sauvegarder la carte en HTML
    m.save(outfile='carte_taxiout.html')
    return m


map_obj = creerCart()


