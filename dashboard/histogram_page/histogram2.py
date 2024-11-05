import pandas as pd
import plotly.express as px

#Nombre d'occurrences de chaque type de délai
def create_histogram_delay():

    # Charger les données
    df_flight_delay = pd.read_csv('data//clean//Flight_Delay_Clean.csv')

    # Filtrer les colonnes liées aux différents types de retard
    delay_types = ['CarrierDelay', 'WeatherDelay', 'NASDelay', 'SecurityDelay', 'LateAircraftDelay']
    delay_counts = {delay_type: (df_flight_delay[delay_type] > 15).sum() for delay_type in delay_types}

    # Convertir le dictionnaire en DataFrame pour visualisation
    df_delay_counts = pd.DataFrame(list(delay_counts.items()), columns=['Type de Retard', 'Occurrences'])

    # Créer l'histogramme avec Plotly Express
    histogram_type_delay = px.bar(df_delay_counts, 
                x='Type de Retard', 
                y='Occurrences', 
                title='Nombre d\'occurrences pour chaque type de retard',
                labels={'Occurrences': 'Nombre d\'Occurrences'},
                color_discrete_sequence=['purple'])

    # Ajustements de style
    histogram_type_delay .update_layout(
        title_x=0.5,  # Centrer le titre
        xaxis_title="Type de Retard",
        yaxis_title="Nombre d'Occurrences"
    )
    return histogram_type_delay  