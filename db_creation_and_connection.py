from sqlalchemy import create_engine, text, Table, Column, Integer, String, MetaData, Date
import psycopg2

# ======================================================
# ⚙️ CONFIGURATION — à adapter selon ton environnement
# ======================================================
PG_SUPERUSER = "postgres"
PG_SUPERPASS = "postgresql"      # ton mot de passe postgres défini plus tôt
PG_HOST = "localhost"
PG_PORT = "5432"
TARGET_DB = "defense_db"
NEW_USER = "fchmk"
NEW_USER_PASS = "postgresql"

# ======================================================
# 🚀 Connexion au superuser (postgres)
# ======================================================
admin_engine = create_engine(f"postgresql+psycopg2://{PG_SUPERUSER}:{PG_SUPERPASS}@{PG_HOST}:{PG_PORT}/postgres")

# ======================================================
# 🧱 Étape 1 : Vérifier / Créer la base de données
# ======================================================
with admin_engine.connect() as conn:
    conn.execute(text("COMMIT"))  # on sort de la transaction implicite
    db_exists = conn.execute(
        text("SELECT 1 FROM pg_database WHERE datname = :dbname"),
        {"dbname": TARGET_DB}
    ).scalar()

    if not db_exists:
        conn.execute(text(f"CREATE DATABASE {TARGET_DB}"))
        print(f"✅ Base {TARGET_DB} créée")
    else:
        print(f"ℹ️ Base {TARGET_DB} déjà existante")

# ======================================================
# 👤 Étape 2 : Vérifier / Créer l'utilisateur
# ======================================================
with admin_engine.connect() as conn:
    user_exists = conn.execute(
        text("SELECT 1 FROM pg_roles WHERE rolname = :username"),
        {"username": NEW_USER}
    ).scalar()

    if not user_exists:
        conn.execute(text(f"CREATE USER {NEW_USER} WITH PASSWORD '{NEW_USER_PASS}'"))
        print(f"✅ Utilisateur {NEW_USER} créé")
    else:
        print(f"ℹ️ Utilisateur {NEW_USER} déjà existant")

    # Donner les droits à l'utilisateur sur la base
    conn.execute(text(f"GRANT ALL PRIVILEGES ON DATABASE {TARGET_DB} TO {NEW_USER}"))
    print(f"🔑 Droits accordés sur {TARGET_DB} à {NEW_USER}")

# ======================================================
# 🧩 Étape 3 : Connexion à la base cible
# ======================================================
user_engine = create_engine(f"postgresql+psycopg2://{NEW_USER}:{NEW_USER_PASS}@{PG_HOST}:{PG_PORT}/{TARGET_DB}")
metadata = MetaData()

# ======================================================
# 🗂️ Étape 4 : Création de la table acled_events si absente
# ======================================================
acled_events = Table(
    "acled_events", metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("event_date", Date),
    Column("country", String(100)),
    Column("event_type", String(100)),
    Column("actor1", String(200)),
    Column("actor2", String(200)),
    Column("fatalities", Integer)
)

metadata.create_all(user_engine)
print("✅ Table acled_events créée ou déjà existante")

print("\n🎯 Configuration PostgreSQL terminée avec succès !")
