"""Histogramme dynamique en fonction du temps de retard d'arrivé"""
import pandas as pd
import plotly.express as px

def create_histogram_arrival_delay(min_delay, max_delay):
    # Charger les données
    df_flight_delay = pd.read_csv('data//clean//Flight_Delay_Clean.csv')

    # Filtrer pour ne garder que les retards d'arrivée dans la plage choisie
    df_flight_delay_filtered = df_flight_delay[
        (df_flight_delay['ArrDelay'] >= min_delay)
    ]
    df_flight_delay_filtered = df_flight_delay[
        (df_flight_delay['ArrDelay'] < max_delay)
    ]

    # Compter les occurrences pour chaque retard d'arrivée unique
    delay_counts = df_flight_delay_filtered['ArrDelay'].value_counts().reset_index()
    delay_counts.columns = ['ArrDelay', 'Occurrences']  # Renommer les colonnes

    # Filtrer pour ne conserver que les valeurs où le nombre d'occurrences est supérieur à 1000
    delay_counts_filtered = delay_counts[delay_counts['Occurrences'] > 1000].sort_values(by='ArrDelay')
    
    # Créer l'histogramme pour la distribution des retards d'arrivée
    histogram_arr_delay = px.bar(
        delay_counts_filtered, 
        x='ArrDelay', 
        y='Occurrences', 
        title=f"Distribution des retards d'arrivée ({min_delay} à {max_delay} minutes)",
        labels={'ArrDelay': 'Retard à l\'arrivée (minutes)', 'Occurrences': 'Nombre d\'Occurrences'},
        color_discrete_sequence=['purple']
    )

    # Ajustements de style
    histogram_arr_delay.update_layout(
        title_x=0.5,
        xaxis_title="Retard à l'arrivée (minutes)",
        yaxis_title="Nombre d'Occurrences",
        bargap=0.1,
        xaxis=dict(
            range=[min_delay, max_delay]  # Ajuste la plage de l'axe x en fonction du curseur
        )
        
    )

    # Retourne l'histogramme
    return histogram_arr_delay
