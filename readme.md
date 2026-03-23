# 🎮 Gaming Planner

> Bot Discord + interface web locale pour planifier tes sessions de jeu à la semaine.

---

## ✨ Features

- **Vue semaine** — planifie chaque jour avec le jeu et l'heure de ton choix
- **Liste de jeux** — gère ta bibliothèque de jeux directement depuis l'interface
- **Embed Discord** — envoie un planning formaté sur ton serveur en un clic
- **Envoi automatique** — le bot poste le planning chaque soir à 20h automatiquement
- **Interface web locale** — accessible sur `http://localhost:3000`

---

## 🗂️ Structure

```
gaming-planner/
├── bot/
│   └── bot.py          # Bot Discord (discord.py)
├── web/
│   ├── server.py       # API REST (FastAPI)
│   └── public/
│       └── index.html  # Interface web (Tailwind CSS)
├── data/
│   └── planning.json   # Stockage du planning
├── .env                # Variables d'environnement (non versionné)
├── .gitignore
└── requirements.txt
```

---

## 🚀 Installation

### 1. Cloner le repo

```bash
git clone https://github.com/ton-user/gaming-planner.git
cd gaming-planner
```

### 2. Créer le virtualenv et installer les dépendances

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configurer les variables d'environnement

Crée un fichier `.env` à la racine :

```env
DISCORD_TOKEN=ton_token_discord
CHANNEL_ID=id_du_salon_cible
```

> **Où trouver ces valeurs ?**
> - `DISCORD_TOKEN` → [Discord Developer Portal](https://discord.com/developers/applications) → ton app → onglet **Bot** → Reset Token
> - `CHANNEL_ID` → Discord, mode développeur activé → clic droit sur le salon → **Copier l'identifiant**

### 4. Initialiser le planning

Crée `data/planning.json` :

```json
{ "sessions": [], "games": [] }
```

---

## ▶️ Lancement

```bash
source venv/bin/activate
uvicorn web.server:app --reload --port 3000
```

Ouvre ensuite [http://localhost:3000](http://localhost:3000) dans ton navigateur.

---

## 🖥️ Utilisation

### Interface web

| Section | Description |
|---|---|
| **Semaine** | Sélectionne un jeu et une heure pour chaque jour |
| **Enregistrer** | Sauvegarde la semaine dans le JSON |
| **→ Discord** | Envoie le planning de la semaine sur Discord |
| **Jeux** | Ajoute ou supprime des jeux de ta liste |

### Bot Discord

Le bot se connecte automatiquement au démarrage du serveur.  
Il envoie un embed chaque soir à **20h** avec les sessions de la semaine en cours.

---

## 📦 Dépendances

| Package | Rôle |
|---|---|
| `fastapi` | Framework API REST |
| `uvicorn` | Serveur ASGI |
| `discord.py` | Bot Discord |
| `apscheduler` | Tâche cron (envoi automatique) |
| `python-dotenv` | Lecture du `.env` |
| `aiofiles` | Lecture de fichiers async |

---

## 🔒 .gitignore

```
venv/
.env
__pycache__/
*.pyc
```

> ⚠️ Ne commit **jamais** ton `.env` — il contient ton token Discord.

---

## 📸 Aperçu

```
Planning
SESSIONS DE JEU · SEMAINE COURANTE

SEMAINE                                    [ ENREGISTRER ]

LUNDI     23/03    [ Albion Online  ▾ ]   [ 21:00 ]
MARDI     24/03    [ PokéMMO        ▾ ]   [ 20:00 ]
MERCREDI  25/03    [ Soirée Chill   ▾ ]   [ 16:00 ]
...

JEUX                                       [ + AJOUTER ]
[ Albion Online × ]  [ PokéMMO × ]  [ Soirée Chill × ]
```

---

*Made with 🎮 by Yunus*