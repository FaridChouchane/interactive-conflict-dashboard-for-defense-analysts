# 🧱 PostgreSQL Setup Template (SQLAlchemy + Python)

## 🎯 Objectif
Ce canevas permet de :
- 🚀 Créer automatiquement une **base PostgreSQL**
- 👤 Créer un **utilisateur applicatif** avec mot de passe
- 🔑 Lui accorder les **droits nécessaires**
- 🧩 Préparer les **tables de données** via SQLAlchemy

> 💡 Réutilisable pour tous projets Data : ETL, API, Dashboard, etc.

---

<details>
<summary>⚙️ <b>Prérequis</b></summary>

1. PostgreSQL doit être installé et en cours d’exécution :
   ```bash
   sudo service postgresql start
   ```
2. Le fichier `pg_hba.conf` doit autoriser l’authentification `md5` :
   ```text
   local   all             all                                     md5
   host    all             all             127.0.0.1/32            md5
   host    all             all             ::1/128                 md5
   ```
3. Le mot de passe du superutilisateur `postgres` doit être défini :
   ```sql
   ALTER USER postgres WITH PASSWORD 'postgresql';
   ```
</details>

---

<details open>
<summary>🧩 <b>Structure de projet recommandée</b></summary>

```
project_root/
│── scripts/
│   └── db_creation_and_connection.py
│── etl/
│── data/
│── README.md
│── requirements.txt
```
</details>

---

<details open>
<summary>🐍 <b>Script principal : db_creation_and_connection.py</b></summary>

### 🔧 Configuration
```python
PG_SUPERUSER = "postgres"
PG_SUPERPASS = "postgresql"      # mot de passe superutilisateur
PG_HOST = "localhost"
PG_PORT = "5432"
TARGET_DB = "defense_db"
NEW_USER = "fchmk"
NEW_USER_PASS = "postgresql"
```

### 🧠 Code complet
```python
from sqlalchemy import create_engine, text, Table, Column, Integer, String, MetaData, Date
import psycopg2

PG_SUPERUSER = "postgres"
PG_SUPERPASS = "postgresql"
PG_HOST = "localhost"
PG_PORT = "5432"
TARGET_DB = "defense_db"
NEW_USER = "fchmk"
NEW_USER_PASS = "motdepassefort"

admin_engine = create_engine(f"postgresql+psycopg2://{PG_SUPERUSER}:{PG_SUPERPASS}@{PG_HOST}:{PG_PORT}/postgres")

with admin_engine.connect() as conn:
    conn.execute(text("COMMIT"))
    db_exists = conn.execute(
        text("SELECT 1 FROM pg_database WHERE datname = :dbname"),
        {"dbname": TARGET_DB}
    ).scalar()

    if not db_exists:
        conn.execute(text(f"CREATE DATABASE {TARGET_DB}"))
        print(f"✅ Base {TARGET_DB} créée")
    else:
        print(f"ℹ️ Base {TARGET_DB} déjà existante")

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

    conn.execute(text(f"GRANT ALL PRIVILEGES ON DATABASE {TARGET_DB} TO {NEW_USER}"))
    print(f"🔑 Droits accordés sur {TARGET_DB} à {NEW_USER}")

user_engine = create_engine(f"postgresql+psycopg2://{NEW_USER}:{NEW_USER_PASS}@{PG_HOST}:{PG_PORT}/{TARGET_DB}")
metadata = MetaData()

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
```
</details>

---

<details open>
<summary>🧠 <b>Points clés à retenir</b></summary>

| Étape | Description |
|-------|-------------|
| ⚙️ `create_engine()` | Crée un moteur de connexion SQLAlchemy |
| 🧩 `text()` | Permet d’exécuter du SQL brut |
| 📚 `MetaData()` | Contient la définition des tables |
| 🏗️ `metadata.create_all()` | Crée les tables si absentes |
| ♻️ Idempotence | Le script peut être relancé sans erreur |
</details>

---

<details>
<summary>🧪 <b>Test d’exécution</b></summary>

```bash
python3 scripts/db_creation_and_connection.py
```

**Résultat attendu :**
```
ℹ️ Base defense_db déjà existante
ℹ️ Utilisateur fchmk déjà existant
🔑 Droits accordés sur defense_db à fchmk
✅ Table acled_events créée ou déjà existante

🎯 Configuration PostgreSQL terminée avec succès !
```
</details>

---

<details>
<summary>🚀 <b>Prochaines étapes</b></summary>

1. Ajouter un module `etl/acled_ingest.py` pour extraire les données ACLED.
2. Charger les données dans `acled_events`.
3. Créer un tableau de bord interactif (**Streamlit**, **Plotly Dash**, etc.).
</details>

---

## 📦 Technologies utilisées
- 🐍 **Python** ≥ 3.10  
- 🐘 **PostgreSQL** ≥ 14  
- ⚙️ **SQLAlchemy**  
- 🔌 **psycopg2**  
- 📊 **pandas** *(pour la suite ETL)*

---

## 🧾 Licence & Auteur
Libre de réutilisation et d’adaptation.  
👤 **Auteur : Farid Chouchane — Data Bellum™**
