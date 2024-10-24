

import pandas as pd
import plotly.offline as pyo
import folium
from folium import Choropleth
import numpy as np
import plotly as plt
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import dash
import json

# Charger le fichier CSV
file_path = 'data//raw//Flight_delay.csv'  # Remplacez par le chemin correct si nécessaire
df = pd.read_csv(file_path)

#Nettoyer les données
print("Donnée manquante au total: ")
total_missingValue=df.isna().sum().sum()
print(total_missingValue)
print("Pourcentage de donnée manquante: ")
print((total_missingValue/df.size)*100)
df_cleanNA=df.dropna()

df_Final=df_cleanNA.drop(['DayOfWeek','UniqueCarrier','FlightNum','TailNum','Cancelled','CancellationCode','Diverted'],axis=1)
#print("Taille du DataFrame nettoyé final")
#print(df_Final.shape)
#print(df_Final.dtypes)
df_Final=pd.DataFrame(df_Final)
#print(df_Final.head())

df_Final.to_csv('data//clean//Flight_Delay_clean.csv', index=False, encoding='utf-8')

CoordAirports = pd.read_csv('data//raw//CoordAirports.csv')
CoordAirports_filtered=CoordAirports.filter(items=['LOCID', 'LONGITUDE', 'LATITUDE'])

CoordAirports_filtered=pd.DataFrame(CoordAirports_filtered)
CoordAirports_filtered.to_csv('data//clean//CoordAirportsClean.csv', index=False, encoding='utf-8')





# Lecture des données
df_Final_filtered = df_Final.filter(items=['TaxiOut', 'Origin'])
CoordAirports = pd.read_csv('data//clean//CoordAirportsClean.csv')

# Sélection des 40 aéroports les plus fréquentés
top_40_airports = df_Final_filtered['Origin'].value_counts().nlargest(40).index
df_top_40 = df_Final_filtered[df_Final_filtered['Origin'].isin(top_40_airports)]

# Nettoyage des colonnes
df_top_40['Origin'] = df_top_40['Origin'].str.strip().str.upper()    
CoordAirports['LOCID'] = CoordAirports['LOCID'].str.strip().str.upper()

# Association des coordonnées des aéroports
df_top_40_with_coords = df_top_40.merge(
    CoordAirports[['LOCID', 'LATITUDE', 'LONGITUDE']], 
    left_on='Origin', 
    right_on='LOCID', 
    how='left'
).drop('LOCID', axis=1)

# Calcul du retard moyen (TaxiOut) par aéroport
avg_taxiout_by_airport = df_top_40_with_coords.groupby('Origin').agg({
    'TaxiOut': 'mean',    # Calcule le retard moyen pour chaque aéroport
    'LATITUDE': 'first',  # On peut prendre la première occurrence des coordonnées
    'LONGITUDE': 'first'
}).reset_index()

# Arrondir le retard moyen
avg_taxiout_by_airport['TaxiOut'] = avg_taxiout_by_airport['TaxiOut'].round(2)

# Sauvegarde dans un fichier CSV
avg_taxiout_by_airport.to_csv('data//clean//DataPourCarte.csv', index=False, encoding='utf-8')

# Affichage des résultats
print(avg_taxiout_by_airport.head())



