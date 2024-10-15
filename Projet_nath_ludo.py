import pandas as pd
import plotly.offline as pyo
import numpy as np
import plotly as plt
import plotly.express as px
import seaborn as sns
import dash
import folium
from folium import Choropleth
# Charger le fichier CSV
file_path = 'Flight_delay.csv'  # Remplacez par le chemin correct si nécessaire
df = pd.read_csv(file_path)

#Nettoyer les données
print("Donnée manquante au total: ")
total_missingValue=df.isna().sum().sum()
print(total_missingValue)
print("Pourcentage de donnée manquante: ")
print((total_missingValue/df.size)*100)
df_cleanNA=df.dropna()

df_Final=df_cleanNA.drop(['DayOfWeek','Date','UniqueCarrier','FlightNum','TailNum','Cancelled','CancellationCode','Diverted'],axis=1)
print("Taille du DataFrame nettoyé final")
print(df_Final.shape)
print(df_Final.dtypes)
print(df_Final['Airline'].nunique())
df_Final=pd.DataFrame(df_Final)
print(df_Final.head())

# Calculer la moyenne de TaxiIn pour chaque aéroport de destination
avg_taxi_in_by_dest = df_Final.groupby('Dest')['TaxiIn'].mean()

# Calculer la moyenne de TaxiOut pour chaque aéroport d'origine
avg_taxi_out_by_org = df_Final.groupby('Origin')['TaxiOut'].mean()

# Classer les moyennes par ordre croissant
sorted_taxi_in = avg_taxi_in_by_dest.sort_values()
sorted_taxi_out = avg_taxi_out_by_org.sort_values()

# Obtenir les 10 premiers et 10 derniers résultats
top_10_taxi_in = sorted_taxi_in.head(10)
bottom_10_taxi_in = sorted_taxi_in.tail(10)

top_10_taxi_out = sorted_taxi_out.head(10)
bottom_10_taxi_out = sorted_taxi_out.tail(10)

# Afficher les résultats
print("Top 10 TaxiIn par aéroport de destination (ordre croissant) :")
print(top_10_taxi_in)

print("\nBottom 10 TaxiIn par aéroport de destination (ordre croissant) :")
print(bottom_10_taxi_in)

print("\nTop 10 TaxiOut par aéroport d'origine (ordre croissant) :")
print(top_10_taxi_out)

print("\nBottom 10 TaxiOut par aéroport d'origine (ordre croissant) :")
print(bottom_10_taxi_out)





#Carte 

top_20_airports=df_Final['Org_Airport'].value_counts().nlargest(20).index
df_top_20 = df_Final[df_Final['Org_Airport'].isin(top_20_airports)]
print(df_top_20)

airport_coordinates = {
    'ORD': {'lat': 41.9742, 'lon': -87.9073},  # Chicago O'Hare International Airport
    'DFW': {'lat': 32.8998, 'lon': -97.0403},  # Dallas/Fort Worth International Airport
    'ATL': {'lat': 33.6407, 'lon': -84.4277},  # Hartsfield-Jackson Atlanta International Airport
    'DEN': {'lat': 39.8561, 'lon': -104.6737}, # Denver International Airport
    'LAX': {'lat': 33.9416, 'lon': -118.4085}, # Los Angeles International Airport
    'LAS': {'lat': 36.084, 'lon': -115.1537},  # McCarran International Airport (Las Vegas)
    'SFO': {'lat': 37.6213, 'lon': -122.3790}, # San Francisco International Airport
    'PHX': {'lat': 33.4343, 'lon': -112.0116}, # Phoenix Sky Harbor International Airport
    'MDW': {'lat': 41.7868, 'lon': -87.7522},  # Chicago Midway International Airport
    'MCO': {'lat': 28.4294, 'lon': -81.3089},  # Orlando International Airport
    'SLC': {'lat': 40.7899, 'lon': -111.9791}, # Salt Lake City International Airport
    'LGA': {'lat': 40.7769, 'lon': -73.8740},  # LaGuardia Airport (Marine Air Terminal)
    'JFK': {'lat': 40.6413, 'lon': -73.7781},  # John F. Kennedy International Airport
    'PHL': {'lat': 39.8719, 'lon': -75.2411},  # Philadelphia International Airport
    'CLT': {'lat': 35.214, 'lon': -80.9431},   # Charlotte Douglas International Airport
    'MIA': {'lat': 25.7959, 'lon': -80.2871},  # Miami International Airport
    'BWI': {'lat': 39.1754, 'lon': -76.6684},  # Baltimore-Washington International Airport
    'SAN': {'lat': 32.7338, 'lon': -117.1933}, # San Diego International Airport
    'SEA': {'lat': 47.4502, 'lon': -122.3088}, # Seattle-Tacoma International Airport
    'HOU': {'lat': 29.6454, 'lon': -95.2789},  # William P. Hobby Airport (Houston)
}

# Calculer le retard moyen (TaxiOut) par aéroport
avg_taxiout_by_airport = df_top_20.groupby('Origin')['TaxiOut'].mean().reset_index()

# Ajouter les coordonnées géographiques
avg_taxiout_by_airport['Latitude'] = avg_taxiout_by_airport['Origin'].map(lambda x: airport_coordinates[x]['lat'])
avg_taxiout_by_airport['Longitude'] = avg_taxiout_by_airport['Origin'].map(lambda x: airport_coordinates[x]['lon'])

# Créer une carte centrée sur les États-Unis
map_center = (39.8283, -98.5795)  # Coordonnées du centre des États-Unis
map = folium.Map(location=map_center, tiles='OpenStreetMap', zoom_start=4)

# Ajouter les aéroports avec le retard moyen sur la carte
for index, row in avg_taxiout_by_airport.iterrows():
    folium.CircleMarker(
        location=(row['Latitude'], row['Longitude']),
        radius=row['TaxiOut'] / 2,  # Ajuster la taille du cercle en fonction du retard
        color='crimson',
        fill=True,
        fill_color='crimson',
        fill_opacity=0.6,
        popup=f"{row['Origin']}: Retard Moyen de l'aéroport (TaxiOut): {row['TaxiOut']} min"
    ).add_to(map)

# Enregistrer la carte dans un fichier HTML
map.save(outfile='carte_airport_taxiout_map.html')


