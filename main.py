"""Main"""

# Importe les fichiers nécessaires
from data.clean_data import clean_data                                              # Fichier de nettoyage des données
from dashboard.page_router import create_router_page                                # Fichier de création de la page router
from dashboard.histogram_page.histogram_callback import create_histogram_callback   # Fichier de création des callbacks

def main():

    """fonction principale"""

    # Nettoie les données
    clean_data()

    # Lance l'application
    app = create_router_page()      # Récupère l'application
    create_histogram_callback(app)  # Récupère le callback de histogram page
    app.run_server(debug=True)      # Run l'application récupérée

if __name__ == "__main__":
    main()