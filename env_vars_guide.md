# 📋 Guide des Variables d’Environnement dans un Projet Python

Ce guide explique comment utiliser des **variables d’environnement** pour gérer proprement les configurations sensibles dans vos projets Python (ex: clés API, secrets, paramètres de connexion…).

---

## ✅ Pourquoi utiliser des variables d’environnement ?

- 🔐 **Sécurité** : ne pas exposer ses clés API / mots de passe dans le code source.
- 🔁 **Flexibilité** : différents fichiers `.env` pour différents environnements (dev, staging, prod).
- 💡 **Lisibilité** : centralise la configuration à un seul endroit.

---

## 📦 1. Installer `python-dotenv`

Ajoutez la dépendance dans votre projet :

```bash
uv add python-dotenv
```

---

## 📄 2. Créer un fichier `.env`

Exemple de fichier `.env` à placer à la racine du projet :

```
# .env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
DATABASE_URL=postgresql://user:pass@localhost:5432/dbname
DEBUG=True
```

### 🧠 Recommandations de nommage :

- Majuscules avec des underscores : `API_KEY`, `SECRET_KEY`, `DEBUG_MODE`
- Clairs et explicites : `GOOGLE_MAPS_API_KEY`, `AWS_SECRET_ACCESS_KEY`, etc.

---

## 🧫 3. Charger les variables avec `load_dotenv` et les extraire avec `os.getenv`

Dans votre code Python (ex: `main.py` ou `settings.py`) :

```python
from dotenv import load_dotenv
import os

# Charge les variables du .env
load_dotenv(override=True)  # `override=True` permet de forcer la mise à jour si déjà définies dans l'env

# Récupérer les variables
api_key = os.getenv("OPENAI_API_KEY")
debug_mode = os.getenv("DEBUG") == "True"
```

### 📌 Important :

- `override=True` est utile si vous voulez forcer la priorité du `.env` sur les variables déjà présentes dans l’environnement système (utile en dev).
- Les variables sont toujours des **chaînes de caractères** → pensez à convertir les booléens ou entiers manuellement.

---

## 🚫 4. Ne **jamais** versionner le fichier `.env`

Ajoutez-le à `.gitignore` :

```
# .gitignore
.env
```

Cela évite de **pousser accidentellement vos secrets sur GitHub** ou tout autre dépôt distant.

---

## 🛠️ 5. Bonnes pratiques

- ✅ Préfixez les variables par service : `AWS_`, `OPENAI_`, `GCP_`, etc.
- ✅ Utilisez un `.env.example` (ou `.env.template`) à **versionner** pour indiquer les variables nécessaires sans inclure les vraies valeurs.
- ✅ Ne stockez pas de données longues/multilignes (certificats…) → préférez des fichiers séparés.
- ✅ Ne chargez pas `load_dotenv()` dans des modules appelés souvent (ex: un fichier utilitaire importé partout).
- ✅ Protégez vos environnements de prod (utilisez `os.environ` directement pour ne pas dépendre du `.env`).

---

## 📁 6. Exemple de structure de projet

```
my_project/
├── src/my_project/
│       ├── __init__.py
│       └── main.py
├── .env
├── .env.example
├── .gitignore
├── .python-version
├── README.md
└── pyproject.toml
```

---

## 🗉️ 7. Aller plus loin (bonus)

- Vous pouvez avoir plusieurs fichiers `.env` :
  - `.env.dev`, `.env.prod`, etc.
- Utilisez `dotenv.load_dotenv(dotenv_path=".env.dev")` pour charger le bon fichier dynamiquement.

---
