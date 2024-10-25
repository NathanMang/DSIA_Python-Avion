"""Carte"""

import pandas as pd
import folium

def add_marker(row, map_obj):
    
    """Ajoute un marqueur à la map fournit en paramètre"""

    # Définit la couleur du marqueur en fonction du délai
    taxi_out = row['TaxiOut']
    if taxi_out < 15:
        color = 'green'
    elif taxi_out < 20:
        color = 'yellow'
    elif taxi_out < 30:
        color = 'orange'
    else:
        color = 'red'

    # Créé et ajoute le marqueur à la carte
    folium.CircleMarker(
        location=[row['LATITUDE'], row['LONGITUDE']],   # Localisation du marqueur / aéroport
        radius=row['TaxiOut'] / 2,                      # Taille du cercle proportionnelle au temps de taxiOut
        color=color,                                    # Couleur du marqueur
        fill=True,                                      # Remplit le marqueur
        fill_color=color,                               # Couleur de remplissage du marqueur
        fill_opacity=0.6,                               # Opacité du marqueur
        popup=f"{row['Origin']}: {row['TaxiOut']} min", # Affichage du popup quand on appuie sur le marqueur (ex: "DEN: 18.44 min")
    ).add_to(map_obj)                                   # Ajoute le marqueur à la map

def create_map():

    '''Créé notre cartographie'''

    # Récupère les données
    avg_taxiout_by_airport = pd.read_csv('data//clean//avg_taxiout_by_airport.csv')

    # Créé une carte centrée sur les États-Unis
    map_center = [39.8283, -98.5795]                                            # Coordonnées du centre des États-Unis
    m = folium.Map(location=map_center, tiles='OpenStreetMap', zoom_start=4)    # Créé la carte

    # Ajoute tous les marqueurs 
    avg_taxiout_by_airport.apply(lambda row: add_marker(row, m), axis=1)

    # Ajoute une légende 
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

    # Sauvegarde la carte sous format HTML
    m.save(outfile='dashboard/map_page/map.html')