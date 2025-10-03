                👤 Utilisateur
                      │
    ┌─────────────────┴─────────────────┐
    │                                   │
 Applications visibles             Services Windows
 (Word, Chrome, Python, pgAdmin)   (PostgreSQL, Windows Update, Spouleur d'impression)
    │                                   │
    │   ↔ Interaction directe           │   ↔ Fonctionnent sans fenêtre
    │                                   │   ↔ Démarrent avec Windows
    │                                   │   ↔ "Tournent en arrière-plan"
    └─────────────────┬─────────────────┘
                      │
             ⚡ Fournissent des ressources
             (ex: PostgreSQL répond aux requêtes SQL
              depuis Python, psql, pgAdmin…)
