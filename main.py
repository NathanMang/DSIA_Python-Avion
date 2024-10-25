"""Main"""

from data.clean_data import clean_data
from dashboard.page_router import create_router_page

def main():

    """fonction principale"""

    # Nettoie les données
    clean_data()

    # Lance l'application
    app = create_router_page()   # Récupère l'application
    app.run_server(debug=True)   # Run l'application récupérée

if __name__ == "__main__":
    main()