# Guide : Les décorateurs en Python

## Introduction

Les **décorateurs** sont l'une des fonctionnalités les plus puissantes et élégantes de Python. Ils permettent de modifier ou d'enrichir le comportement d'une fonction ou d'une classe **sans modifier son code source**.

Ils sont très utilisés en Python, notamment dans :
- la validation d'entrées,
- la gestion des accès (authentification, autorisation),
- le logging,
- la mesure de performance,
- et beaucoup de frameworks (Flask, Django, FastAPI, etc.).

---

## 1. Qu'est-ce qu'un décorateur ?

Un décorateur est simplement **une fonction qui prend une fonction en paramètre et retourne une nouvelle fonction**.

**Exemple basique** :

```python
def mon_decorateur(fonction):
    def nouvelle_fonction():
        print("Avant l'appel")
        fonction()
        print("Après l'appel")
    return nouvelle_fonction

@mon_decorateur
def dire_bonjour():
    print("Bonjour !")

# Appel

dire_bonjour()
```

**Sortie :**
```text
Avant l'appel
Bonjour !
Après l'appel
```

---

## 2. Pourquoi utiliser un décorateur ?

- **Séparation des responsabilités et Réutilisabilité** : Permet d'ajouter ou de modifier des comportements sans toucher au code existant, et d'appliquer facilement un même comportement à plusieurs fonctions.
- **Lisibilité** : Le comportement ajouté est clairement indiqué avec l'annotation `@`, ce qui rend le code plus explicite.
- **Respect du principe DRY (Don't Repeat Yourself)** : Évite la duplication de code en centralisant la logique réutilisable.

---

## 3. Créer des décorateurs plus avancés

### Décorateurs avec arguments

Pour écrire un décorateur qui accepte des arguments, il faut ajouter un niveau de fonction supplémentaire.

**Exemple :**

```python
def decorateur_avec_arguments(message):
    def decorateur(fonction):
        def wrapper():
            print(f"{message} - Avant l'appel")
            fonction()
            print(f"{message} - Après l'appel")
        return wrapper
    return decorateur

@decorateur_avec_arguments("[INFO]")
def saluer():
    print("Salut tout le monde!")

saluer()
```

**Sortie :**
```text
[INFO] - Avant l'appel
Salut tout le monde!
[INFO] - Après l'appel
```

### Décorateurs pour des fonctions avec paramètres

Pour décorer des fonctions qui prennent des arguments, il faut utiliser `*args` et `**kwargs` dans le wrapper.

```python
def mon_decorateur(fonction):
    def wrapper(*args, **kwargs):
        print("Avant appel")
        resultat = fonction(*args, **kwargs)
        print("Après appel")
        return resultat
    return wrapper

@mon_decorateur
def additionner(a, b):
    print(f"Résultat : {a + b}")
    return a + b

additionner(5, 7)
```

**Sortie :**
```text
Avant appel
Résultat : 12
Après appel
```

---

## 4. Utiliser `functools.wraps`

Quand on écrit un décorateur, il est recommandé d'utiliser `functools.wraps` pour conserver les métadonnées (nom, docstring) de la fonction originale.

```python
import functools

def mon_decorateur(fonction):
    @functools.wraps(fonction)
    def wrapper(*args, **kwargs):
        print("Avant appel")
        return fonction(*args, **kwargs)
    return wrapper
```


Sans `@wraps`, le nom de `wrapper` écrase celui de la fonction décorée.

**Exemple sans `@wraps` :**

```python
def mon_decorateur(fonction):
    def wrapper(*args, **kwargs):
        return fonction(*args, **kwargs)
    return wrapper

@mon_decorateur
def dire_bonjour():
    """Cette fonction dit bonjour."""
    print("Bonjour !")

print(dire_bonjour.__name__)
print(dire_bonjour.__doc__)
```

**Sortie :**
```text
wrapper
None
```

**Exemple avec `@wraps` :**

```python
import functools

def mon_decorateur(fonction):
    @functools.wraps(fonction)
    def wrapper(*args, **kwargs):
        return fonction(*args, **kwargs)
    return wrapper

@mon_decorateur
def dire_bonjour():
    """Cette fonction dit bonjour."""
    print("Bonjour !")

print(dire_bonjour.__name__)
print(dire_bonjour.__doc__)
```

**Sortie :**
```text
dire_bonjour
Cette fonction dit bonjour.
```

Le nom `dire_bonjour` est préservé.

La docstring est conservée.

---

## 5. Décorateurs intégrés utiles

Python fournit plusieurs décorateurs intégrés :

- **@staticmethod** : Définit une méthode qui n'utilise pas `self` ou `cls`.
- **@classmethod** : Définit une méthode de classe recevant `cls` au lieu de `self`.
- **@property** : Permet de transformer une méthode en attribut en lecture seule.

**Exemple :**

```python
class Cercle:
    def __init__(self, rayon):
        self._rayon = rayon

    @property
    def surface(self):
        import math
        return math.pi * (self._rayon ** 2)

c = Cercle(5)
print(c.surface)
```

**Sortie :**
```text
78.53981633974483
```

---

## 6. Empiler plusieurs décorateurs

Il est possible d'empiler plusieurs décorateurs sur une fonction :

```python
@decorateur_1
@decorateur_2
@decorateur_3
fonction()
```

Cela équivaut à :
```python
fonction = decorateur_1(decorateur_2(decorateur_3(fonction)))
```

L'ordre **va de bas en haut**.

---

## 7. Décorateurs pour les classes

Un décorateur peut également modifier des **classes** entières.

**Exemple simple :**

```python
def ajouter_attribut(cls):
    cls.attribut_ajoute = "Ajouté!"
    return cls

@ajouter_attribut
class MaClasse:
    pass

print(MaClasse.attribut_ajoute)
```

**Sortie :**
```text
Ajouté!
```

---

# Conclusion

Les décorateurs sont une manière puissante, flexible et élégante de modifier le comportement de fonctions ou de classes.

**À retenir :**
- Un décorateur est une fonction qui retourne une fonction.
- On peut facilement écrire ses propres décorateurs.
- `@wraps` est essentiel pour conserver les métadonnées.
- Ils sont omniprésents dans les frameworks modernes.

---
