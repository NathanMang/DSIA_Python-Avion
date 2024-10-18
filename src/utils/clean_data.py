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

df_Final=df_cleanNA.drop(['DayOfWeek','Date','UniqueCarrier','FlightNum','TailNum','Cancelled','CancellationCode','Diverted'],axis=1)
print("Taille du DataFrame nettoyé final")
print(df_Final.shape)
print(df_Final.dtypes)
df_Final=pd.DataFrame(df_Final)
print(df_Final.head())

df.to_csv('data//clean//Flight_Delay_clean.csv', index=False, encoding='utf-8')