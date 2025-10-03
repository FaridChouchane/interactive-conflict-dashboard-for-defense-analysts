# interactive-conflict-dashboard-for-defense-analysts
# Data Integration

But :

récupérer des données ACLED en Python et les stocker dans PostgreSQL.

Actions :

Crée un script Python etl/acled_ingest.py.

use requests pour appeler l’API ACLED.

Parse la réponse JSON → DataFrame pandas.

Push dans PostgreSQL avec SQLAlchemy ou psycopg2.
