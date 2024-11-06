import pandas as pd
import plotly.express as px

def create_histogram_arrival_delay():
    # Charger les données
    df_flight_delay = pd.read_csv('data//clean//Flight_Delay_Clean.csv')

    # Filtrer pour ne garder que les retards d'arrivée supérieurs à 15 minutes
    df_flight_delay_filtered = df_flight_delay[df_flight_delay['ArrDelay'] > 15]

    # Compter les occurrences pour chaque retard d'arrivée unique
    delay_counts = df_flight_delay_filtered['ArrDelay'].value_counts().reset_index()
    delay_counts.columns = ['ArrDelay', 'Occurrences']  # Renommer les colonnes

    # Filtrer pour ne conserver que les valeurs où le nombre d'occurrences est supérieur à 6000
    delay_counts_filtered = delay_counts[delay_counts['Occurrences'] > 6000].sort_values(by='ArrDelay')
    
    # Créer l'histogramme pour la distribution des retards d'arrivée
    histogram_arr_delay = px.bar(
        delay_counts_filtered, 
        x='ArrDelay', 
        y=delay_counts_filtered['Occurrences'], 
        title="Distribution des retards d'arrivée (ArrDelay) avec plus de 6000 occurrences",
        labels={'ArrDelay': 'Retard à l\'arrivée (minutes)', 'Occurrences': 'Nombre d\'Occurrences'},
        color_discrete_sequence=['purple']
    )

    # Ajustements de style
    histogram_arr_delay.update_layout(
        title_x=0.5,         # Centrer le titre
        xaxis_title="Retard à l'arrivée (minutes)",
        yaxis_title="Nombre d'Occurrences",
        bargap=0.1 ,          # Espacement entre les barres
        yaxis=dict(
            range=[6000, None])  # L'axe Y commence à 6000
    )

    return histogram_arr_delay


