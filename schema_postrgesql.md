                         💻 Ton ordinateur (Windows)
┌───────────────────────────────────────────────────────────┐
│                                                           │
│   1) Logiciel PostgreSQL (programme)                      │
│   ----------------------------------------------------    │
│   📂 C:\Program Files\PostgreSQL\17                       │
│   ├── bin\        → exécutables (psql.exe, postgres.exe)  │
│   ├── pgAdmin 4\  → outil graphique de gestion            │
│   ├── lib\, share\ … → fichiers nécessaires               │
│                                                           │
│   ⚡ Sert à faire tourner le serveur PostgreSQL            │
│                                                           │
│                                                           │
│   2) Serveur PostgreSQL (service Windows)                 │
│   ----------------------------------------------------    │
│   🔄 Processus qui tourne en arrière-plan                 │
│   - Écoute sur : localhost:5432                           │
│   - Démarré automatiquement avec Windows (service)        │
│                                                           │
│   ⚡ C’est lui qui “répond” à tes requêtes SQL             │
│                                                           │
│                                                           │
│   3) Dossier DATA (les vraies bases de données)           │
│   ----------------------------------------------------    │
│   📂 Exemple : C:\Program Files\PostgreSQL\17\data        │
│        ou dans AppData\Roaming\PostgreSQL\                │
│                                                           │
│   - Contient tous les fichiers binaires des bases         │
│   - Tu n’ouvres jamais ces fichiers à la main             │
│                                                           │
│   ⚡ C’est là que sont stockées tes tables, données, etc.  │
│                                                           │
│                                                           │
│   → Accès utilisateur :                                   │
│     - en ligne de commande :  psql -U postgres -h localhost│
│     - en graphique       :  pgAdmin 4                     │
│     - en Python          :  SQLAlchemy + psycopg2         │
│                                                           │
└───────────────────────────────────────────────────────────┘
