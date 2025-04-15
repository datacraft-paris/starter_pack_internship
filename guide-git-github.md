## 🖥️ Utiliser GitHub Desktop pour un usage graphique de Git

### 🚀 Pourquoi utiliser GitHub Desktop ?

GitHub Desktop est une application graphique qui permet de :

- Gérer tes dépôts GitHub sans ligne de commande  
- Visualiser les changements, commits, branches  
- Faire des pull/push facilement  
- Travailler plus confortablement si tu débutes avec Git  

---

### 🔧 Installation de GitHub Desktop

1. Va sur [desktop.github.com](https://desktop.github.com)  
2. Télécharge la version pour Windows ou macOS  
3. Installe et connecte-toi à ton compte GitHub  

---

### 📁 Cloner un dépôt GitHub avec GitHub Desktop

1. Clique sur `File > Clone repository`  
2. Va dans l’onglet `URL`  
3. Colle l’URL HTTPS de ton dépôt (depuis GitHub)  
4. Choisis un dossier de destination sur ton ordinateur  
5. Clique sur `Clone`  

---

### ✍️ Faire des modifications et commits

1. Ouvre le dossier cloné dans ton éditeur (comme VS Code)  
2. Modifie des fichiers  
3. Retourne dans GitHub Desktop : tu verras les changements dans l’onglet `Changes`  
4. Renseigne un message de commit et clique sur `Commit to main`  

---

### 📤 Envoyer tes modifications sur GitHub (push)

1. Clique sur `Push origin` en haut de l’interface  
2. Tes changements sont envoyés sur GitHub  

---

### 🔁 Récupérer les changements distants (pull)

1. Clique sur `Fetch origin` pour voir les nouveautés  
2. Puis sur `Pull origin` pour télécharger les modifs  

---

### 🌿 Créer une branche avec GitHub Desktop

1. En haut à gauche, clique sur la liste des branches  
2. Clique sur `New branch`  
3. Nomme ta branche et valide  
4. Tu peux maintenant travailler séparément sans toucher à `main`  

---

### ✅ Bonnes pratiques avec GitHub Desktop

- Toujours faire un `Fetch` avant de commencer  
- Renseigner des messages de commit clairs  
- Créer des branches pour les fonctionnalités distinctes  
- Faire des `push` réguliers pour sauvegarder ton travail  

---

GitHub Desktop est une excellente passerelle vers Git pour les débutants. Une fois à l’aise avec l’interface graphique, tu pourras progressivement basculer vers la ligne de commande pour plus de puissance !

---

## 🧠 Bonnes pratiques : nommage des branches et messages de commit

### 🌿 Nommage des branches

Pour garder un projet clair et organisé, adopte un schéma cohérent pour nommer tes branches. Voici quelques conventions simples :

#### 🔧 Structure recommandée :

type/nom-court-descriptif

#### 🔑 Types de branches courants :

- `feature/` → nouvelle fonctionnalité  
- `fix/` → correction de bug  
- `refactor/` → amélioration du code sans changement fonctionnel  
- `docs/` → documentation  
- `test/` → tests  
- `hotfix/` → correctif urgent en production

#### ✅ Exemples :

- `feature/ajout-login`
- `fix/correction-affichage-mobile`
- `refactor/clean-fonction-auth`

---

### ✍️ Bonnes pratiques pour les messages de commit

Un bon message de commit rend l’historique clair pour toi et les autres.

#### 🔹 Format recommandé :

type: description courte au présent

#### 🔑 Types fréquents :

- `feat:` → ajout d'une fonctionnalité  
- `fix:` → correction de bug  
- `docs:` → modification de documentation  
- `refactor:` → refonte du code sans nouvelle fonctionnalité  
- `style:` → changements de formatage (indentation, espaces, etc.)  
- `test:` → ajout/modif de tests  
- `chore:` → tâches diverses (update deps, config...)

#### ✅ Exemples de bons commits :

- `feat: ajout du formulaire d’inscription`
- `fix: résolution du bug de pagination`
- `refactor: simplification de la fonction de calcul`
- `docs: ajout d’un exemple dans le README`

---

### 🧼 Astuces supplémentaires

- Commits **petits et fréquents** = historique lisible
- Utilise le **présent** dans tes messages (`ajoute`, pas `ajouté`)
- Sois **précis** sur ce que tu fais
- **Évite les messages vagues** comme `update`, `fix`, `changement`

---