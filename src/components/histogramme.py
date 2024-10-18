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

df_Final=pd.read_csv('data//clean//Flight_Delay_clean.csv')
plt.hist(df_Final['Distance'], bins=30, color='purple', edgecolor='black')
plt.title("Distribution des Distances des Vols")
plt.xlabel("Distance (miles)")
plt.ylabel("Nombre de Vols")
plt.xlim(0, 5000) 
plt.show()