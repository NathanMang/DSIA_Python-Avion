
top_40_airports=df_Final['Org_Airport'].value_counts().nlargest(40).index
df_top_40 = df_Final[df_Final['Org_Airport'].isin(top_40_airports)]
# Calculer le retard moyen (TaxiOut) par aéroport
avg_taxiout_by_airport = df_top_40.groupby('Origin')['TaxiOut'].mean().reset_index()
avg_taxiout_by_airport['TaxiOut'] = avg_taxiout_by_airport['TaxiOut'].round(2)
#print(avg_taxiout_by_airport)



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


# Créer une carte centrée sur les États-Unis
map_center = (39.8283, -98.5795)  # Coordonnées approximatives du centre des États-Unis
map = folium.Map(location=map_center, tiles='OpenStreetMap', zoom_start=4)

# Ajouter un titre à la carte
title_html = '''
     <h3 align="center" style="font-size:20px; font-weight: bold;">Temps moyen d'un décollage après embarquement par aéroport(TaxiOut)</h3>
     '''
map.get_root().html.add_child(folium.Element(title_html))

# Ajouter les aéroports avec le retard moyen sur la carte en utilisant CircleMarker
for index, row in avg_taxiout_by_airport.iterrows():
    airport_code = row['Origin']
    if airport_code in airport_coordinates:
         # Définir la couleur en fonction du temps d'embarquement
        taxi_out = row['TaxiOut']
        if taxi_out < 15:
            color = 'green'  # Moins de 15 minutes
        elif taxi_out < 20:
            color = 'yellow'  # Entre 15 et 20 minutes
        elif taxi_out < 30:
            color = 'orange'  # Entre 20 et 30 minutes
        else:
            color = 'red'  # Plus de 30 minutes
        # Ajouter chaque aéroport à la carte avec un cercle proportionnel au temps d'embarquement
        folium.CircleMarker(
            location=[airport_coordinates[airport_code]['lat'], airport_coordinates[airport_code]['lon']],
            radius=min(max(row['TaxiOut'] / 2, 20), 150),  # Ajuster la taille des cercles pour qu'ils soient visibles
            color=color,  # Couleur des bordures des cercles
            fill=True,
            fill_color=color,  # Remplir les cercles avec une couleur distinctive
            fill_opacity=0.6,
            popup=folium.Popup(f"Aéroport: {airport_code}<br>Temps moyen d'un décollage après embarquement total: {row['TaxiOut']} min", max_width=200)
        ).add_to(map)

# Ajouter une légende
legend_html =  """
     <div style="position: fixed; 
                 bottom: 50px; left: 50px; width: 160px; height: auto;
                 border:2px solid grey; z-index:9999; font-size:14px;
                 background-color: white;
                 opacity: 0.9; padding: 10px; border-radius: 5px;">
     <b>Légende</b><br>
     <span style="display: inline-block; 
                  width: 20px; height: 20px; background: green; 
                  border-radius: 50%;"></span>&nbsp; Moins de 15 min<br>
     <span style="display: inline-block; 
                  width: 20px; height: 20px; background: yellow; 
                  border-radius: 50%;"></span>&nbsp; 15-20 min<br>
     <span style="display: inline-block; 
                  width: 20px; height: 20px; background: orange; 
                  border-radius: 50%;"></span>&nbsp; 20-30 min<br>
     <span style="display: inline-block; 
                  width: 20px; height: 20px; background: red; 
                  border-radius: 50%;"></span>&nbsp; Plus de 30 min<br>
     </div>
     """
map.get_root().html.add_child(folium.Element(legend_html))

# Sauvegarder la carte
map.save(outfile='carte_choroplèthe.html')