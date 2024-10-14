import pandas as pd
import plotly.offline as pyo
import numpy as np
import plotly as plt
import plotly.express as px
import seaborn as sns
import dash
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


