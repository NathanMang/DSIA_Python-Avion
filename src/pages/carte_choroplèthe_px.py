import plotly.express as px
import pandas as pd
import folium

def creerCart():
    # Exemple de données
    df_Final = pd.read_csv('data//clean//Flight_Delay_clean.csv')
    top_40_airports = df_Final['Org_Airport'].value_counts().nlargest(40).index
    df_top_40 = df_Final[df_Final['Org_Airport'].isin(top_40_airports)]

    # Calcul du retard moyen (TaxiOut) par aéroport
    avg_taxiout_by_airport = df_top_40.groupby('Origin')['TaxiOut'].mean().reset_index()
    avg_taxiout_by_airport['TaxiOut'] = avg_taxiout_by_airport['TaxiOut'].round(2)

    # Ajouter les coordonnées des aéroports
    airport_coordinates = {
    'ORD': {'lat': 41.9742, 'lon': -87.9073},  # Chicago O'Hare International Airport
    'DFW': {'lat': 32.8998, 'lon': -97.0403},  # Dallas/Fort Worth International Airport
    'ATL': {'lat': 33.6407, 'lon': -84.4277},  # Hartsfield-Jackson Atlanta International Airport
    'DEN': {'lat': 39.8561, 'lon': -104.6737}, # Denver International Airport
    'LAX': {'lat': 33.9416, 'lon': -118.4085}, # Los Angeles International Airport
    'LAS': {'lat': 36.084, 'lon': -115.1537},  # McCarran International Airport
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
    'HOU': {'lat': 29.6454, 'lon': -95.2789},  # William P. Hobby Airport
    'BOS': {'lat': 42.3656, 'lon': -71.0096},  # Gen. Edward Lawrence Logan International Airport
    'DAL': {'lat': 32.8471, 'lon': -96.8517},  # Dallas Love Field
    'FLL': {'lat': 26.0726, 'lon': -80.1527},  # Fort Lauderdale-Hollywood International Airport
    'TPA': {'lat': 27.9755, 'lon': -82.5332},  # Tampa International Airport
    'STL': {'lat': 38.7487, 'lon': -90.3700},  # St. Louis International Airport at Lambert Field
    'OAK': {'lat': 37.7213, 'lon': -122.2214}, # Oakland International Airport
    'BNA': {'lat': 36.1263, 'lon': -86.6774},  # Nashville International Airport
    'MCI': {'lat': 39.2976, 'lon': -94.7139},  # Kansas City International Airport
    'DCA': {'lat': 38.8512, 'lon': -77.0402},  # Ronald Reagan Washington National Airport
    'IAD': {'lat': 38.9531, 'lon': -77.4565},  # Washington Dulles International Airport
    'SJC': {'lat': 37.3639, 'lon': -121.9290}, # Norman Y. Mineta San José International Airport
    'RDU': {'lat': 35.8776, 'lon': -78.7875},  # Raleigh-Durham International Airport
    'SMF': {'lat': 38.6951, 'lon': -121.5908}, # Sacramento International Airport
    'PDX': {'lat': 45.5898, 'lon': -122.5951}, # Portland International Airport
    'SNA': {'lat': 33.6757, 'lon': -117.8678}, # John Wayne Airport (Orange County Airport)
    'MKE': {'lat': 42.9477, 'lon': -87.8966},  # General Mitchell International Airport
    'EWR': {'lat': 40.6895, 'lon': -74.1745},  # Newark Liberty International Airport
    'AUS': {'lat': 30.1975, 'lon': -97.6664},  # Austin-Bergstrom International Airport
    'ABQ': {'lat': 35.0402, 'lon': -106.609},  # Albuquerque International Sunport
    'PIT': {'lat': 40.4914, 'lon': -80.2329}   # Pittsburgh International Airport
}

    # Ajouter les coordonnées dans le DataFrame
    avg_taxiout_by_airport['lat'] = avg_taxiout_by_airport['Origin'].map(lambda x: airport_coordinates[x]['lat'])
    avg_taxiout_by_airport['lon'] = avg_taxiout_by_airport['Origin'].map(lambda x: airport_coordinates[x]['lon'])

    # Créer la carte avec Plotly Express
    fig = px.scatter_geo(avg_taxiout_by_airport,
                         lat='lat',
                         lon='lon',
                         size='TaxiOut',  # La taille est proportionnelle au temps moyen
                         hover_name='Origin',
                         hover_data={'TaxiOut': True},
                         title="Temps moyen de décollage après embarquement (TaxiOut) par aéroport")

   
    
    # Définir la couleur en fonction du temps d'embarquement
    fig.update_traces(marker=dict(size=avg_taxiout_by_airport['TaxiOut'] * 2,
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
                                      ticktext=['< 15 min', '15-20 min', '20-30 min', '> 30 min'])
                                  ))

    # Ajuster les limites de la carte et améliorer l'esthétique
    fig.update_geos(
    visible=False, resolution=110, scope="usa",
    showcountries=True, countrycolor="Black",
    showsubunits=True, subunitcolor="Blue"
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