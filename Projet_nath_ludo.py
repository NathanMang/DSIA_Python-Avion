import pandas as pd

# Charger le fichier CSV
file_path = 'Flight_delay.csv'  # Remplacez par le chemin correct si nécessaire
df = pd.read_csv(file_path)

# Calculer la moyenne de TaxiIn pour chaque aéroport de destination
avg_taxi_in_by_dest = df.groupby('Dest')['TaxiIn'].mean()

# Calculer la moyenne de TaxiOut pour chaque aéroport d'origine
avg_taxi_out_by_org = df.groupby('Origin')['TaxiOut'].mean()

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
