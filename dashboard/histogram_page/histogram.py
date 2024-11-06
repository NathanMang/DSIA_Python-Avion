import pandas as pd
import plotly.express as px

def create_histogram(delay_type):

    df_flight_delay=pd.read_csv('data//clean//Flight_Delay_Clean.csv')  # Charge nos données nettoyées dans un data frame

    df_flight_delay_filtered = df_flight_delay[df_flight_delay[delay_type]>15]  # Filtre les données pour des retards supérieurs à 15 min
    
    delay_counts = df_flight_delay_filtered['Airline'].value_counts().reset_index()
    delay_counts.columns = ['Airline', 'Occurrences']
    
    # Créé l'histogramme
    histogram = px.histogram(
        delay_counts,                                                               # Sélection des données en fonction du retard
        x='Airline',                                                                # Variable observée
        y='Occurrences',
        title=f"Distribution des retards par compagnie aérienne ({delay_type})",    # Titre du graphique
        labels={'Airline': 'Compagnie Aérienne', 'Occurences': 'Nombre occurrences'}, # Étiquettes des axes
        color_discrete_sequence=['purple']                                          # Couleur des barres
    )

    # Définit le style de l'histogramme
    histogram.update_traces(marker=dict(line=dict(color='black', width=1))) # Bordures noires pour les barres
    histogram.update_layout(
        title_x=0.5,    # Alignement du titre
        bargap=0.1      # Distance entre les barres
    )

    # Retourne l'histogramme
    return histogram