

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

def creerHist(month):
        
    df_Final=pd.read_csv('data//clean//Flight_Delay_clean.csv')
    df_Final['Date'] = pd.to_datetime(df_Final['Date'], format='%d-%m-%Y')
    # Création de l'histogramme avec Plotly Express
    fig = px.histogram(df_Final[df_Final['Date'].dt.month == month], 
    x='Distance', 
    nbins=40,  # Nombre de bins
    title="Distribution des Distances des Vols",  # Titre du graphique
    labels={'Distance': 'Distance (miles)', 'count': 'Nombre de Vols'},  # Étiquettes des axes
    color_discrete_sequence=['purple'])  # Couleur des barres

    # Définition des bordures noires pour les barres de l'histogramme
    fig.update_traces(marker=dict(line=dict(color='black', width=1)))

    # Définir les limites de l'axe des X (comme dans Matplotlib avec `plt.xlim`)
    fig.update_layout(xaxis=dict(range=[0, 4600]))

    return fig