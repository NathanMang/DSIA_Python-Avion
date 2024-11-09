"""CleanData"""

import pandas as pd


def clean_data():
    
    """Nettoyage des données de nos fichiers"""



    # Fichier sur le retard des avions

    # Récupère les données
    file_path = 'data//raw//Flight_delay.csv'  # Chemin d'accès du fichier
    df_flight_delay = pd.read_csv(file_path)   # Charge les données dans un dataframe

    # Nettoie les données
    df_flight_delay = df_flight_delay.filter(items=['CarrierDelay', 'WeatherDelay', 'NASDelay', 'SecurityDelay', 'LateAircraftDelay',
                                                    'Airline', 'TaxiOut', 'Origin','ArrDelay'])  # Récupère les colonnes nécessaires
    df_flight_delay = df_flight_delay.dropna()  # Supprime les lignes contenant des valeurs manquantes

    # Enregistre le DataFrame dans un fichier CSV
    df_flight_delay.to_csv('data//clean//Flight_Delay_Clean.csv', index=False, encoding='utf-8')



    # Fichier sur les coordonnées des aéroport

    # Récupère les données
    file_path = 'data//raw//CoordAirports.csv'                     # Chemin d'accès du fichier
    df_coord_airports = pd.read_csv('data//raw//CoordAirports.csv') # Charge les données dans un dataframe

    # Nettoie les données
    df_coord_airports = df_coord_airports.filter(items=['LOCID', 'LONGITUDE', 'LATITUDE'])   # Récupère les colonnes nécessaires

    # PS: LOCID est un identifiant unique à chaque aéroport



    # Fusion des deux fichiers

    # Sélection des 40 aéroports les plus fréquentés
    df_top_40_airports_id = df_flight_delay['Origin'].value_counts().nlargest(40).index          # Index des 40 premiers aéroports
    df_top_40_airports = df_flight_delay[df_flight_delay['Origin'].isin(df_top_40_airports_id)]  # Garde les 40 premiers aéroports
    
    # Normalisation des valeurs
    df_top_40_airports = df_top_40_airports.copy()
    df_top_40_airports['Origin'] = df_top_40_airports['Origin'].str.strip().str.upper() # Supprime les espaces et convertit en majuscule
    df_top_40_airports = df_top_40_airports.copy()
    df_coord_airports['LOCID'] = df_coord_airports['LOCID'].str.strip().str.upper()       # Supprime les espaces et convertit en majuscule

    # Association des coordonnées des aéroports
    df_top_40_with_coords = df_top_40_airports.merge(     # Fusionne df_top_40_airports
        df_coord_airports,                                 # avec df_CoordAirports
        left_on='Origin',                                 # selon la colonne 'Origin'
        right_on='LOCID',                                 # et la colonne 'LOCID'
        how='left'                                        # joint le deuxième DataFrame au premier
    ).drop('LOCID', axis=1)                               # Supprime la colonne 'LOCID' identique à la colonne 'Origin'
    
    # Calcul du temps de décollage moyen (TaxiOut) par aéroport
    df_avg_taxiout_by_airport = df_top_40_with_coords.groupby('Origin').agg({   # Regroupe les données par aéroport 
        'TaxiOut': 'mean',                                                      # leur moyenne de temps de décollage après embarquement total de l'avion
        'LATITUDE': 'first',                                                    # latitude
        'LONGITUDE': 'first'                                                    # longitude
    }).reset_index()

    # Arrondir le retard moyen
    df_avg_taxiout_by_airport['TaxiOut'] = df_avg_taxiout_by_airport['TaxiOut'].round(2)

    # Enregistre le DataFrame dans un fichier CSV
    df_avg_taxiout_by_airport.to_csv('data//clean//avg_taxiout_by_airport.csv', index=False, encoding='utf-8')