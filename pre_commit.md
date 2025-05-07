# Guide Pre-commit : formattage, linting et utilisation Black, Ruff

## 1. Pourquoi utiliser Black, Ruff ?

**Git commit** permet d'enregistrer des modifications locales du code source dans un dépôt Git. C'est une étape essentielle pour collaborer efficacement et suivre l'historique des changements.

- **Black** : Un formateur de code Python automatique. Il reformate votre code pour respecter un style standardisé, améliorant ainsi la lisibilité et la cohérence.
- **Ruff** : Un outil ultra-rapide pour Python qui combine linter et correcteur automatique. Il analyse le code pour détecter les erreurs, les incohérences de style, les fautes de syntaxe, ainsi que les mauvaises pratiques, et peut corriger automatiquement un grand nombre de problèmes identifiés.

L'objectif global est de **maintenir un code propre**, **standardisé** et **sans erreur** avant chaque commit.

---

## 2. Installation des outils nécessaires

### Installer Black et Ruff avec UV

Vous pouvez installer Black et Ruff via UV directement dans votre projet :

```bash
uv tool install black ruff
```

**uv tool install** sert à installer un outil CLI (en ligne de commande) spécifique directement via UV, sans passer par pip ni toucher ton environnement Python pour pouvoir l'utiliser globalement.

---

## 3. Utiliser UVX pour lancer les outils

**uvx** est une commande spéciale qui permet d'exécuter directement des outils installés via UV, sans avoir à activer un environnement.

Exemple :

- Lancer Black :

```bash
uvx black .
```

- Lancer Ruff :

```bash
uvx ruff .
```

### Fix automatique avec `--fix`

Ruff peut analyser et corriger automatiquement certaines erreurs :

```bash
uvx ruff check . --fix
```

#### Décomposition de la commande

- **`check`** :
  C'est l'action par défaut de Ruff. Elle lance une analyse complète du code pour détecter :
  - des erreurs,
  - des problèmes de style,
  - des fautes de syntaxe,
  - des mauvaises pratiques de programmation,
  - et d'éventuelles vulnérabilités de sécurité.

- **`.`** :
  Spécifie que l'analyse doit être effectuée sur le répertoire courant (`.`), c'est-à-dire l'ensemble du projet.

- **`--fix`** :
  Indique à Ruff de corriger automatiquement toutes les erreurs qui peuvent l'être, en appliquant des modifications sûres, comme :
  - reformater les indentations incorrectes,
  - supprimer les imports inutilisés,
  - corriger les chaînes de caractères mal formées,
  - remplacer certaines constructions Python par des versions plus propres,
  - supprimer les variables inutilisées, etc.

Cela analyse tout ton projet et corrige automatiquement tous les problèmes détectés de ton projet Python pour qu'il soit clean, rapide et conforme aux standards.

---

## 4. Formater et linter automatiquement avant le commit (avec pre-commit)

### Installer Pre-Commit

Pour installer Pre-Commit dans votre projet, utilisez la commande suivante :

```bash
uv add pre-commit
```

### Configurer les hooks pour Black et Ruff : exemple de fichier `.pre-commit-config.yaml`

Avant de pouvoir utiliser Black et Ruff avec Pre-Commit, il est nécessaire de configurer les hooks correspondants dans le fichier `.pre-commit-config.yaml`.

Créez un fichier `.pre-commit-config.yaml` à la racine de votre projet :

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: check-yaml
      - id: end-of-file-fixer
      - id: trailing-whitespace
  - repo: local
    hooks:
      - id: black
        name: black
        entry: uvx black
        language: system
        types: [python]
      - id: ruff
        name: ruff
        entry: uvx ruff check . --fix
        language: system
        types: [python]
```

Puis lancez :

```bash
pre-commit install
```

> Après cette configuration, chaque tentative de commit lancera automatiquement Black et Ruff. Si des erreurs sont détectées, le commit sera bloqué jusqu'à correction.

---
### Forcer un commit sans exécuter les hooks Pre-Commit

Dans certains cas, il peut arriver qu'une correction automatique effectuée par Pre-Commit (par exemple, une modification imposée par Black ou Ruff) ne corresponde pas à vos attentes. Si vous souhaitez tout de même effectuer un commit sans exécuter les hooks, vous pouvez utiliser l'option suivante :

```bash
git commit -m "Votre message de commit" --no-verify
```

#### Explications :
- **`--no-verify`** : Cette option permet de bypasser tous les hooks configurés (Pre-Commit, linting, tests, etc.) et de forcer le commit.
- **À noter** : Cette commande doit être utilisée avec précaution et uniquement dans des cas exceptionnels, car elle désactive toutes les protections automatiques mises en place pour garantir la qualité du code.

---


# Happy coding! 🚀

N'oubliez pas : un code propre, c'est un futur heureux pour tous les développeurs du projet !
