import os

# Buscamos el archivo dentro de la carpeta 'data' de nuestro proyecto
# Esto funcionará en cualquier PC
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RUTA_CSV = os.path.join(BASE_DIR, "data", "matches_by_teams.csv")

COLS_FEATURES = ['core_goals', 'core_shots', 'core_saves', 'core_assists', 'boost_amount_collected']
COL_TARGET = 'winner'