 """
 import os
 import sys

# Ajouter le répertoire parent au PYTHONPATH pour permettre les imports relatifs
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import de l'application principale
from trading_dashboard_pro.app import (
    st, setup_config, show_login_screen, show_assets_view, show_details_view,
    show_admin_view, show_profile_data_view, load_profile_data, save_profile_data
)
 
 # Configuration de la page
 st.set_page_config(