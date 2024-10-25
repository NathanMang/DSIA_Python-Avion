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

def creerHist():
        
    df_Final=pd.read_csv('data//clean//Flight_Delay_clean.csv')
    # Création de l'histogramme avec Plotly Express
    fig = px.histogram(df_Final, 
    x='Airline', 
    nbins=40,  # Nombre de bins
    title="Distribution des compagnies américaines",  # Titre du graphique
    labels={'Distance': 'Distance (miles)', 'count': 'Nombre de Vols'},  # Étiquettes des axes
    color_discrete_sequence=['purple']) # Couleur des barres

    

    # Ajuster les axes pour un affichage plus propre
    fig.update_layout(
        xaxis_title="Compagnie Aérienne",
        yaxis_title="Nombre de vols",
        title_x=0.5,  # Centrer le titre
        bargap=0.1,  # Espacement entre les barres
    )

    return fig

def histogram_Dynamique(retard_type='CarrierDelay'):
    
    
    df_Final=pd.read_csv('data//clean//Flight_Delay_clean.csv')

    retard_supérieur_15min=df_Final[df_Final[retard_type]>15]
    
    # Créer l'histogramme
    fig = px.histogram(
        retard_supérieur_15min,
        x='Airline',
        y=retard_type,
        title=f"Distribution des retards par compagnie aérienne ({retard_type})",
        labels={'Airline': 'Compagnie Aérienne', retard_type: 'Nombre occurrences'},
        color_discrete_sequence=['purple']
    )

    # Définir le style de l'histogramme
    fig.update_traces(marker=dict(line=dict(color='black', width=1)))
    fig.update_layout(
        xaxis_title="Compagnie Aérienne",
        yaxis_title="Nombre occurrences",
        title_x=0.5,
        bargap=0.1
    )

    return fig

