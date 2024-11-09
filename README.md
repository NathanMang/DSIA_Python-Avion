# Dashboard de Retards Aériens
## User Guide

Pour déployer et utiliser ce dashboard sur une autre machine, suivez les étapes ci-dessous :

1. **Cloner le dépôt** :

   Si vous n'avez pas Git d'installer:
   
   ```
   $ git --version
   git version 2.38.1.windows.1
   ```

   Télécharger le depuis cette [page](https://git-scm.com/downloads/win)

   Créer un dossier pour récupérer le projet

   Saisissez dans votre terminal:

   ```
   cd cheminpourouvrirleprojet
    
   git clone https://git.esiee.fr/viellarl/myprojectludo.git
   ```

2. **Ouvrir le projet** : 

   Saisissez dans votre terminal:

   ```
   cd cheminpourouvrirleprojet/myproject_nath_ludo
   ```

3. **Installez les dépendances** :

   Tapez la ligne de commande suivante dans le terminal:

   ```
   pip install -r requirements.txt
   ```

3. **Lancer le dashboard** : 

   Si vous n'avez pas Pyhton d'installer:
   
   ```
   $ python --version
   $ Python 3.12.7
   ```

   Télécharger le depuis cette [page](https://www.python.org/downloads/)

   Tapez la ligne de commande suivante dans le terminal:
   
   ```
   python main.py
   ```

4. **Accédez au dashboard** :

   http://127.0.0.1:8050/


## Data

Le dashboard utilise plusieurs ensembles de données, incluant :

- **avg_taxiout_by_airport** : Données nettoyées contenant des informations sur les coordonnées géographiques des 40 aéroports américains ayant le plus de vols en 2019.
  
- **Flight_Delay_clean** : Données nettoyées des retards de vols, comprenant des informations sur les compagnies aériennes, les types de retard, et le délai nécessaire pour qu'un avion décolle après l'embarquement complet.

- **CoordAirports** : Données brutes utilisées pour récupérer les coordonnées géographiques des aéroports américains.

- **Flight_delay** : Données brutes utilisées pour le nettoyage des données de retards.


## Developer Guide

Ce guide vous permettra de comprendre l'architecture du projet et de vous aider à ajouter facilement de nouvelles pages ou de nouveaux graphiques au dashboard.

Architecture du Code:

dashboard/ : Contient les différents pages du dashboard

      histogram_page/ : Dossier dédiée à la page des histogrammes. Chaque fichier représente un graphique (histogramme) ou une fonctionnalité de la page :

         histogram_airline.py : Fichier pour générer un premier histogramme dynamique sur compagnie aérienne

         histogram_arr_delay.py : Fichier pour générer un deuxième histogramme dynamique sur les retards à l'arrivée

         histogram_type_delay.py : Fichier pour générer un troisième histogramme statique par type de retard

         histogram_callback.py : Contient les callbacks nécessaires pour gérer les interactions de la page d'histogrammes

         histogram_layout.py : Définition de la mise en page pour la page d'histogramme

      home_page/ : Dossier dédiée à la page d'accueil

         histogram_layout.py : Définition de la mise en page pour la page d'accueil

      map_page/ : Dossier dédiée à la page de la carte

         map_layout.py : Définition de la mise en page pour la page de la carte

         map.py : Fichier pour générer la carte
         
         map.html : Carte généré par map.py sous format html

      assets/ : Contient les ressources statiques de l'application (images) et les images du Readme

      page_router.py : Gère la navigation entre les différentes pages du dashboard.

data/ : Stocke les données du projet.

      raw/ : Données brutes.

      clean/ : Données traitées et prêtes pour l'analyse.

      clean_data.py : Script pour nettoyer et préparer les données.

main.py : Point d'entrée principal de l'application, qui initialise le serveur et lance l'application Dash.

## Rapport d'analyse

**Rapport d’Analyse des Données de Retards Aériens**

**1. Introduction**

L'analyse des retards aériens vise à identifier et comprendre les facteurs influençant les délais des vols aux États-Unis. Ces retards peuvent survenir à l’arrivée ou au départ, et sont influencés par des variables telles que la compagnie aérienne, le type de retard, l’aéroport d’origine et la distance parcourue. Les causes de ces retards sont diverses, incluant des problèmes météorologiques, des questions de sécurité, ou des retards attribués aux compagnies aériennes elles-mêmes.

**Objectifs de l'analyse :**

•	Identifier les compagnies aériennes les plus affectées par les retards et en comprendre les causes principales.

•	Analyser la répartition des retards en fonction des types de retard (retard du transporteur, météo, gestion aérienne nationale, sécurité).

•	Visualiser les délais moyens de décollage par aéroport et observer les différences géographiques.

**2. Description des données**

Les données utilisées dans cette analyse proviennent de deux sources principales :

•	_Fichier de Retards de Vols_ : Ce fichier contient des informations sur les retards, incluant l'aéroport d'origine, la compagnie aérienne, les types de retard, et la durée du vol.

•	_Fichier de Coordonnées Géographiques des Aéroports_ : Utilisé pour associer les retards de vol aux localisations géographiques des aéroports.

_Variables clés :_

•	_Compagnie Aérienne(Airline)_: Code unique représentant chaque compagnie aérienne.

•	_Type de Retard_ : Catégorisations des retards (retard à l’arrivée, retard du transporteur, retard dû à la météo, retard lié à la gestion nationale, retard de sécurité).

•	_Aéroport d’Origine (Org_Airport)_ : Code IATA de l’aéroport de départ.

•	_Latitude et Longitude_ : Coordonnées géographiques des aéroports, permettant la visualisation géographique des données.

**3. Méthodologie**

Les données ont été nettoyées pour éliminer les valeurs manquantes et les doublons. Pour établir la carte choroplèthe, un filtrage a été effectué pour ne conserver que les aéroports parmi les 40 plus fréquentés aux États-Unis, assurant ainsi une analyse ciblée et pertinente. De plus, une jointure entre les deux fichiers de données a permis d'associer les coordonnées géographiques aux aéroports concernés.
Pour garantir la pertinence de l'analyse des retards, seules les données concernant les retards supérieurs à 15 minutes ont été retenues. Des visualisations interactives ont été élaborées pour faciliter l'exploration des données par les utilisateurs.

**4. Analyse et Visualisation**

_**Distribution des retards d’arrivée :**_

Cet histogramme illustre la répartition des retards d'arrivée des vols aériens en 2019, en se concentrant sur ceux ayant un retard supérieur à 15 minutes. Les données analysées concernent exclusivement les retards ayant eu plus de 1000 occurrences, ce qui permet de mettre en avant les retards les plus fréquents et d’alléger la complexité de l’histogramme. En filtrant ainsi les retards d'arrivée, l’objectif est de focaliser l’analyse sur les retards les plus significatifs, tout en écartant ceux qui occupent une part trop faible pour être représentatifs dans l'histogramme.

Chaque barre représente le nombre d'occurrences d'une durée de retard d'arrivée spécifique, mettant en évidence les retards les plus fréquents. Cette visualisation offre une vue d'ensemble sur la distribution des retards d'arrivée majeurs, permettant d’explorer leur impact sur la ponctualité des vols et d’identifier les plages de retard les plus récurrentes.

![histogramme arrival delay](assets/histogramme_arr_delay.png)

_**Distribution des Retards par Compagnie Aérienne :**_

Un histogramme dynamique a été conçu pour visualiser la répartition des retards parmi les différentes compagnies aériennes. Comme notre jeu de données se concentre uniquement sur les vols ayant subi des retards, le nombre de vols répertoriés par compagnie représente directement le nombre de vols en retard pour chaque compagnie. Cet histogramme est équipé d’un menu déroulant qui permet aux utilisateurs de sélectionner divers types de retards, offrant ainsi une vue plus détaillée sur les raisons des retards. Seules les occurrences de retards dépassant 15 minutes ont été considérées pour éviter de comptabiliser de légers décalages et se concentrer sur les délais significatifs.

![histogramme airline](assets/histogramme_airline.png)

**_Résultats observés pour les histogrammes :_**

Pour l'histogramme "_Distribution des retards d’arrivée_" :

Cet histogramme dynamique présente la répartition des retards d'arrivée des vols, en affichant toutes les occurrences de retards allant de 0 à 120 minutes. Toutefois, pour une analyse plus ciblée et afin d'éviter une surcharge d'informations, nous nous concentrons spécifiquement sur les plages de temps où le nombre d'occurrences est supérieur à 1000. Cette approche permet de se focaliser sur les retards les plus fréquents, offrant ainsi une vue plus claire des tendances principales dans les retards d'arrivée, tout en négligeant les cas moins significatifs. Grâce à l'interactivité de l'histogramme, l'utilisateur peut ajuster dynamiquement la plage de retards à afficher, offrant une analyse plus flexible et approfondie des données.

Les résultats observés montrent une nette concentration des retards entre 15 et 23 minutes, avec un nombre d'occurrences supérieur à 10 000. Ensuite, les retards d’une durée de 24 à 30 minutes affichent un nombre d’occurrences compris entre 8 000 et 10 000. Enfin, pour des retards entre 31 et 38 minutes, le nombre d'occurrences se situe entre 6 000 et 8 000.

Cette répartition démontre que la majorité des retards d’arrivée se concentre dans des délais courts, bien que certains retards plus longs restent significatifs. Cette visualisation met en relief les retards d’arrivée les plus fréquents et permet de mieux comprendre leur répartition, fournissant ainsi une base utile pour des stratégies d'optimisation visant à réduire ces retards significatifs.

Pour l'histogramme "_Distribution des Retards par Compagnie Aérienne_" :

Pour chaque type de retard, le nombre total d’occurrences de retard supérieur à 15 minutes pour toutes compagnies confondues est le suivant :

•	CarrierDelay : 141 000 occurrences

•	WeatherDelay : 21 500 occurrences

•	NASDelay : 105 600 occurrences

•	SecurityDelay : 830 occurrences

•	LateAircraftDelay : 225 000 occurrences

**Analyse des Résultats:**

1.	_LateAircraftDelay_ : Avec un total de 225 000 occurrences, ce type de retard est le plus fréquent parmi les retards supérieurs à 15 minutes. Le nombre d'occurrences maximum observé pour ce retard atteint 70 000 pour la compagnie « Southwest Airlines Co. ». Cela souligne l'effet en cascade des retards initiaux sur les vols suivants, indiquant un besoin d'amélioration de la gestion des correspondances.

2.	_CarrierDelay_ : Totalisant 141 000 occurrences, ces retards représentent souvent des défis internes aux compagnies aériennes (maintenance ou équipage). Ce type de retard atteint un maximum d'occurrences autour de 25 000 pour « American Airlines Inc. » et « Southwest Airlines Co. ». La réduction de ces retards pourrait être un axe d'optimisation pour améliorer la ponctualité.

3.	_NASDelay_ : Ce retard, lié aux contraintes de gestion du trafic aérien, compte 105 600 occurrences et atteint également un pic d'environ 21 000 occurrences pour la compagnie « American Airlines Inc. ». Ces retards sont souvent hors du contrôle direct des compagnies, soulignant les défis liés à la gestion globale du trafic.

4.	_WeatherDelay_ : Bien que ce type de retard soit moins fréquent, avec un total de 21 500 occurrences et un maximum d'environ 5 000 occurrences pour « Atlantic Southeast Airlines », il reflète l'impact des conditions météorologiques imprévisibles sur les horaires des vols.

5.	_SecurityDelay_ : Ce type de retard est le moins fréquent, avec 830 occurrences au total. Toutefois, il demeure critique en raison de la nature des contrôles de sécurité, qui visent à garantir la sûreté des vols.
Analyse des Compagnies Aériennes
Pour chaque type de retard, certaines compagnies sont récurrentes dans le top des plus affectées par les retards :

•	American Airlines Inc.

•	Southwest Airlines Co.

•	American Eagle Airlines Inc.

•	United Air Lines Inc.

Ces compagnies apparaissent souvent dans le top 4 des plus impactées, montrant un besoin d'optimisation dans la gestion de leurs opérations pour réduire les retards.

_**Visualisation Géographique des Délais de Décollage (TaxiOut) :**_

Pour mieux comparer l'efficacité des aéroports à gérer le traffic des avions au sol, une carte choroplèthe a été développée. Cette carte utilise une échelle de couleur allant du vert (délais de taxi inférieurs à 15 minutes) au rouge (délais de taxi supérieurs à 30 minutes). Elle est enrichie par une légende et des infobulles indiquant la durée moyenne entre la fin d'embarquement et le décollage pour chaque aéroport, permettant une vue d'ensemble géographique et une identification rapide des aéroports ayant un manque de gestion importants.


![carte](assets/carte.png)

_**Résultats observés pour la carte choroplèthe :**_

La carte choroplèthe développée pour visualiser les délais moyens de décollage (TaxiOut) révèle des disparités géographiques marquées dans les performances des aéroports à travers les États-Unis. Voici les principaux résultats :

_1.	Impact sur la Côte Est :_
o	Les aéroports de la côte est, en particulier ceux situés dans la région de New York, présentent des délais de taxi moyens significativement plus longs. Les temps moyens de décollage après embarquement des passagers varient de 20 à 40 minutes, atteignant des valeurs particulièrement élevées pour les aéroports tels que John F. Kennedy International Airport (JFK), LaGuardia Airport (LGA), et Newark Liberty International Airport (EWR). Ces retards au décollage peuvent être attribués à une combinaison de congestion aérienne, de restrictions météorologiques et d'une forte densité de trafic, rendant cette région l'une des plus critiques en termes de ponctualité des vols.

_2.	Comparaison avec la Côte Ouest :_
o	En revanche, la côte ouest des États-Unis affiche des temps de taxi moyens qui n'excèdent généralement pas 20 minutes. Les aéroports de Los Angeles (LAX) et de San Francisco (SFO) bénéficient d'une infrastructure plus adéquate et d'une gestion du trafic  plus efficace, ce qui contribue à réduire les délais de décollage. Cette différence de performance souligne l'importance d'une gestion aéroportuaire optimisée pour limiter les retards.

_3.	Zones de Congestion :_
o	La carte met en évidence des zones spécifiques où les retards sont particulièrement prononcés. Les aéroports avec des délais moyens de taxi supérieurs à 30 minutes sont clairement identifiés par des couleurs rouges sur la carte, indiquant une concentration de retards. Ces informations peuvent être cruciales pour les gestionnaires d'aéroport et les compagnies aériennes cherchant à cibler les problèmes de ponctualité dans ces régions.

_4.	Variabilité des Délais :_
o	Les infobulles associées à chaque aéroport fournissent des détails supplémentaires sur la durée moyenne de taxi, permettant aux utilisateurs de comprendre rapidement les retards en cours dans les différents aéroports. Cette visualisation interactive permet aux décideurs de réagir rapidement aux problèmes identifiés et d'élaborer des stratégies pour atténuer les délais.


**Conclusion :**

Cette analyse a permis de mettre en évidence les principaux facteurs de retards, notamment :

•	LateAircraftDelay et CarrierDelay sont les retards les plus fréquents, indiquant des opportunités d’amélioration pour les compagnies aériennes en termes de gestion interne.

•	Les retards dus à la météo et à la sécurité, bien que moins fréquents, ont un impact significatif en raison de leur imprévisibilité et de leur importance en matière de sécurité.

Ces résultats suggèrent que les compagnies aériennes pourraient optimiser leurs opérations pour minimiser les CarrierDelays et mieux coordonner leurs vols afin de réduire les LateAircraftDelays. Les retards liés aux facteurs externes, tels que la météo et le contrôle du trafic aérien, nécessitent une coordination avec les agences de gestion du trafic aérien pour atténuer leur impact sur les voyageurs.

En ce qui concerne les délais moyens de décollage (TaxiOut), l’analyse géographique a révélé des disparités importantes entre les aéroports. Cette visualisation a permis de mettre en évidence les zones de congestion les plus importante à travers le pays. Cette identification est cruciale pour cibler les aéroports nécessitant des efforts de gestion accrus et des stratégies de désengorgement, notamment pour améliorer la fluidité du trafic.

En conclusion, cette étude fournit une base solide pour une stratégie de réduction des retards, en ciblant les principaux types de retard ainsi que les aéroports présentant les plus longs délais de décollage. Elle peut servir de point de départ pour des initiatives d'amélioration continue visant à optimiser l'efficacité des compagnies aériennes et des aéroports, offrant ainsi une meilleure expérience aux voyageurs.


## Copyright
Je déclare sur l'honneur que le code fourni a été produit par nous-même, à l’exception des lignes ci dessous par ChatGPT:

```
df_avg_taxiout_by_airport = df_top_40_with_coords.groupby('Origin').agg({ 
    'TaxiOut': 'mean',
    'LATITUDE': 'first',
    'LONGITUDE': 'first'
}).reset_index()
```

.agg() permet d'appliquer différentes fonctions d'agrégation sur les colonnes du DataFrame après avoir effectué le groupement.

```
avg_taxiout_by_airport.apply(lambda row: add_marker(row, m), axis=1)
```

apply() est une fonction de pandas qui permet d'appliquer une fonction à chaque élément ou à chaque ligne/colonne d'un DataFrame

```
histogram.update_traces(marker=dict(line=dict(color='black', width=1)))
```

marker fait référence aux propriétés de l'apparence des éléments graphiques (ici, les barres de l'histogramme).
line=dict(color='black', width=1) : Cette partie définit les propriétés de la bordure des barres de l'histogramme.

```
dcc.Link(
```

Sert à créer un lien hypertexte qui permet de naviguer entre différentes pages du dashboard

```
m.get_root().html.add_child(folium.Element(legend_html))
```

get_root() renvoie l'élément racine de l'objet carte, qui contient tous les éléments de la carte
folium.Element(legend_html) crée un nouvel objet Element de Folium à partir d'une chaîne de caractères HTML

```
_html.Iframe_
```

html.Iframe est utilisé pour intégrer un iframe HTML, qui permet d'afficher la carte à l'intérieur du dashboard .