# Guide Docker pour les projets Python

Ce document explique l'intérêt d'utiliser Docker et des Dockerfiles au sein de ses projets python.

---

## 1. Pourquoi Docker?
**Docker** est un outil de virtualisation légère qui permet de contenir une application avec toutes ses dépendances dans un environnement isolé, appelé **conteneur**. Posséder un Docker dans un projet d'équipe permet entre autre de:
 - Avoir le même environnement chez tous les collaborateurs.
 - Déployer facilement une app sans se soucier de la configuration du système hôte
 - Obtenir une reproductibilité des expériences/projets (très utile en data science ou ML)

### La notion de conteneur
L'objectif d'un conteneur est le même que pour un serveur dédié virtuel : héberger des services sur un même serveur physique tout en les isolant les uns des autres. Un conteneur est cependant moins figé qu'une machine virtuelle en matière de taille de disque et de ressources allouées. Un conteneur permet d'isoler chaque service : le serveur web, la base de données, des applications pouvant être exécutées de façon indépendante dans leur conteneur dédié, contenant uniquement les dépendances nécessaires. Chaque conteneur peut être relié aux autres par des réseaux virtuels. Il est possible de monter des volumes de disque de la machine hôte dans un conteneur. Si aucun processus n'est démarré dans le conteneur, alors celui-ci s'arrête. On parle parfois de virtualisation d'OS : contrairement à la virtualisation qui émule par logiciel différentes machines sur une machine physique, la conteneurisation émule différents OS sur un seul OS. (source: Wikipedia)

### Applications

En particulier en Python, nous devons souvent installer une version spécifique de Python, générer un environnement virtuel, installer des paquets (`pip`,`uv`, etc.) puis exécuter son script.

Docker permet alors de tout automatiser dans un fichier `Dockerfile` et en un clic on peut construire une image qui contient le projet entier, ses dépendances, et une commande de démarrage `CMD`

Les images Docker sont des fichiers utilisé pour exécuter du code dans un conteneur.

---

## 2. Installation de Docker

### Ubuntu
Le principal se situe sur le [site officiel de Docker](https://docs.docker.com/engine/install/ubuntu/#prerequisites).

Pour les système Linux, c'est Docker Engine qui est installé (sans interface graphique).

Il faut disposer de l'une de ces 3 versions de Ubuntu en version 64-bit pour procéder à l'installation :
- Ubuntu Oracular 24.10
- Ubuntu Noble 24.04 (LTS)
- Ubuntu Jammy 22.04 (LTS)

Pour l'installation, il suffit de lancer les deux lignes suivantes:
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

Pour vérifier que Docker s'est bien installé, on peut vérifier si on possède bien une version de Docker:
```bash
docker --version
```
Output:
```bash
`Docker version 28.3.0, build 38b7060`
```

On peut également tester de la manière suivante (on peut ajouter un `sudo` au cas où cela ne passe pas):
```
docker run hello-world
```
On devrait obtenir une sortie similaire à cela:
```bash
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
e6590344b1a5: Pull complete
Digest: sha256:940c619fbd418f9b2b1b63e25d8861f9cc1b46e3fc8b018ccfe8b78f19b8cc4f
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

### Windows et MacOS
Télécharger Docker Desktop, qui comprend une interface graphique comparé à Engine, sur https://www.docker.com/products/docker-desktop/ et suivre les instructions.

Pour vérifier que tout est bien installé, on peut procéder par les mêmes tests que pour l'installation Ubuntu.

---

## 3. L'essentiel d'un Dockerfile
Un Dockerfile, c’est tout simplement une suite d’instructions qui permettent de créer une image fonctionnelle à partir d’une image de base.

Il contient tout ce qu’il faut pour que ton application tourne correctement :
 - Installation des dépendances
 - Copie du code
 - Configuration de l’environnement
 - Commande de lancement de l’application

Les instructions les plus courantes sont (cf Annexe - Dockerfile Reference):
| Instruction  | Rôle                                                      |
| ------------ | --------------------------------------------------------- |
| `FROM`       | Spécifie l’image de base (ex: `ubuntu`, `python`, `node`) |
| `WORKDIR`    | Définit le dossier courant dans l’image                   |
| `COPY`       | Copie des fichiers locaux dans l’image                    |
| `RUN`        | Exécute une commande pendant la construction              |
| `CMD`        | Définit la commande par défaut à exécuter au démarrage    |
| `ENV`        | Définit une variable d’environnement                      |

Commençons par essayer d'en écrire un basique en suivant plusieurs étapes.

### Étape 1 : Choisir une image de base
On utiise `FROM` pour indiquer l'image de départ.

Exemple:
```Dockerfile
# Pour Python
FROM python:3.12-slim

# Pour Python dans un projet uv
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim
```

### Étape 2 : Définir le répertoire de travail
On définit l'endroit dans le conteneur où on va exécuter les opérations du Dockerfile avec `WORKDIR`.

Exemple:
```Dockerfile
WORKDIR /app
```

### Étape 3 : Copier les fichiers
L’instruction `COPY` permet d’intégrer des fichiers et ou des dossiers pour les ajouter au système de fichiers de l’image dans le répertoire \<destination\> : `COPY <fichier1> ... <fichierN> <destination>`

Exemple:
```Dockerfile
COPY pyproject.toml uv.lock ./
```

### Étape 4 : Installer les fichiers de dépendances
L’instruction `RUN` permet de lancer des commandes aux moments de la construction de l’image. Elle exécute une ou plusieurs commandes shell et ajoute une couche sur l'image courante. La couche ajouté est utilisée dans la prochaine étape du Dockerfile

Exemple: (avec `uv`)
```Dockerfile
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --no-install-project --no-dev
```

### Étape 5 : Copier le reste du code
Les dépendances sont installées, on peut donc maintenant copier le reste du code source.

Exemple:
```Dockerfile
COPY . /app
```

### Étape 6 : Spécifier la commande par défaut
Ce sont les fichiers que Docker exécutera quand on lancera `docker run`.

Exemple:
```Dockerfile
# Commande exécutée par défaut : lance main.py
CMD [ "python", "main.py" ]
```

---
On peut également faire appel à l’instruction `ENV` permettant de définir des variables d’environnement qui seront utilisées dans les commandes exécutées avec l’instruction `RUN`. Ces variables sont persistantes et seront disponibles au moment de l’exécution de l’image de conteneur.

---

## 3. Exemple complet
Fichier Dockerfile "standard" en python pour un projet uv.
```dockerfile
# Utilise une image minimale avec Python 3.12 et uv préinstallé
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# Change le répertoire de travail à /app
WORKDIR /app

# Copie les fichiers de gestion des dépendances
COPY pyproject.toml uv.lock ./

# Configure des variables d’environnement pour uv
ENV UV_COMPILE_BYTECODE=1 \
    UV_FROZEN=1 \
    UV_LINK_MODE=copy \
    UV_NO_INSTALLER_METADATA=1 \
    VIRTUAL_ENV=/app/.venv \
    PYTHONUNBUFFERED=1

# Installe les dépendances (sans les dev) en utilisant le cache si possible
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --no-install-project --no-dev

# Ajoute le chemin du venv au PATH
ENV PATH="/app/.venv/bin:$PATH"

# Copie le reste du code source dans le conteneur
COPY . /app

# Commande exécutée par défaut : lance main.py
CMD [ "python", "main.py" ]
```
D'autres exemples sont présents en annexe.

### Exemple d'arborescence d'un projet avec Dockerfile
```
projet/
├── main.py
├── pyproject.toml
├── uv.lock
└── Dockerfile
```

---

## Mise en pratique

On dispose d'un projet dont l'arborescence correspond à cela (en prenant en compte uniquement les fichiers qui nous intéressent):
```
projet/
├── Dockerfile
├── docker-entrypoint.sh
├── pyproject.toml
├── uv.lock
└── docker/
    └── main.py
```
**Disclaimer 1** : tu as impérativement besoin des fichiers `pyproject.toml` et `uv.lock` qui décrivent les dépendances et qui sont exploitées dans le dockerfile. Ils sont générées grâce à uv (cf Section [Setup Environnement](./environment_setup.md))

**Disclaimer 2** : au sein du `pyproject.toml` il faut impérativement que le champ `name` dans `[project]` ait pour valeur le nom de ta session. Si tu ne la connais pas, tu peux la trouver en faisant :
```bash
echo $HOME
```
Output: `/home/<nom_de_session>`

On va utiliser le fichier `docker-enterpoint.sh` suivant (il exécute le programme main avec python):
```bash
#!/bin/sh
set -e
exec uv run python -m main
```

Et le fichier Dockerfile :
```Dockerfile
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

# Copier le projet
COPY pyproject.toml uv.lock ./

ENV UV_COMPILE_BYTECODE=1 \
    UV_FROZEN=1 \
    UV_LINK_MODE=copy \
    UV_NO_INSTALLER_METADATA=1 \
    VIRTUAL_ENV=/app/.venv \
    PYTHONUNBUFFERED=1
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --no-install-project --no-dev
ENV PATH="/app/.venv/bin:$PATH"

COPY docker /app

# Exposer le port 8000 pour FastAPI
EXPOSE 8000

# Lancer FastAPI
COPY docker-entrypoint.sh ./docker-entrypoint.sh
RUN chmod +x ./docker-entrypoint.sh

ENTRYPOINT ["./docker-entrypoint.sh"]
```

Étape par étape, l'éxecution du dockerfile va :
 1. Créer une image légère pour Python avec `FROM`
 2. Définir le répertoire de travail vers `/app` avec `WORKDIR`
 3. Copier les dépendances `uv.lock` et `pyprojet.toml` dans l'image Docker avec `COPY`
 4. Définir des variables d'environnement pour `uv` et Python avec `ENV`
 5. Installer les dépendances avec `RUN`
 6. Ajoute l’environnement virtuel créé à la variable `PATH`
 7. Copier le dossier `docker/` (et donc `main.py`) dans l'image
 8. Déclarer qu'on se place sur le port 8000 (pour FastAPI) avec `EXPOSE`
 9. Copier et rendre exécutable le script shell
 10. Rendre ce script comme point d'entrée du conteneur, c'est ce qui sera exécuté par défaut quand on fera `docker run`

On va donc construire notre image en lançant la commande
```bash
docker build -t <nom_image_docker> .
```

Et l'exécuter avec
```bash
docker run <nom_image_docker>
```

On devrait obtenir comme sortie :
```bash
Bytecode compiled 224 files in 91ms
Hello, Datacrafter !
```

Le programme `main.py` n'est qu'un simple affichage mais vous êtes libres de mettre à jour le code et faire des choses plus élaborées.

Félicitation, tu as créé ta première image Docker !

---

## Annexe

- [Dockerfile Reference](https://docs.docker.com/reference/dockerfile/)
- [Exemple Dockerfile (Github)](https://github.com/komljen/dockerfile-examples)
- [Ecrire un Dockerfile](https://blog.stephane-robert.info/docs/conteneurs/images-conteneurs/ecrire-dockerfile/)
