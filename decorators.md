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

Un décorateur en Python est une fonction qui prend une autre fonction en paramètre, et qui retourne une fonction enrichie.  
Cela permet d’ajouter un comportement supplémentaire **sans modifier le code original** de la fonction.

---

### Exemple simple
        ```python
        def my_decorator(function):
            def new_function():
                print("Avant l'appel")
                function()
                print("Après l'appel")
            return new_function

        @my_decorator
        def say_hello():
            print("Bonjour !")

        say_hello()
        ```
**Sortie :**

        Avant l'appel
        Bonjour !
        Après l'appel

---

### Écriture équivalente sans `@`
        ```py
        def my_decorator(function):
            def new_function():
                print("Avant l'appel")
                function()
                print("Après l'appel")
            return new_function

        def say_hello():

        say_hello = my_decorator(say_hello)
        say_hello()
        ```




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

**Exemple avec arguments :** 
 ```py
        def my_decorator(function):
            def wrapper(*args, **kwargs):
                print("Avant appel")
                result = function(*args, **kwargs)
                print("Après appel")
                return result
            return wrapper

        @my_decorator
        def add(a, b):
            print(f"Résultat : {a + b}")
            return a + b

        add(5, 7)
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
### Utiliser `functools.wraps`
```py
        import functools

        def my_decorator(function):
            @functools.wraps(function)
            def wrapper(*args, **kwargs):
                print("Avant appel")
                return function(*args, **kwargs)
            return wrapper
```

Sans `@wraps`, le nom de `wrapper` écrase celui de la fonction décorée.

## Exemple sans `@wraps` :
    ``` python  
        def my_decorator(function):
            def wrapper(*args, **kwargs):
                return function(*args, **kwargs)
            return wrapper

        @my_decorator
        def say_hello():
            """This function says hello."""
            print("Bonjour !")

        print(say_hello.__name__)
        print(say_hello.__doc__)
    ``` 

**Sortie :**
    ``` text 
        wrapper
        None
    ```
### Exemple avec `@wraps` :**
    ```py
        import functools

        def my_decorator(function):
            @functools.wraps(function)
            def wrapper(*args, **kwargs):
                return function(*args, **kwargs)
            return wrapper

        @my_decorator
        def say_hello():
            """This function says hello."""
            print("Bonjour !")

        print(say_hello.__name__)
        print(say_hello.__doc__)
    ```

**Sortie :**
    ```text
        say_hello
        This function says hello.
    ```
    

## 5. Décorateurs intégrés utiles

Python fournit plusieurs décorateurs intégrés :

- **@staticmethod** : Définit une méthode qui n'utilise pas `self` ou `cls`.
- **@classmethod** : Définit une méthode de classe recevant `cls` au lieu de `self`.
- **@property** : Permet de transformer une méthode en attribut en lecture seule.

**Exemple :**

```python
class Circle:
    def __init__(self, rayon):
        self._rayon = rayon

    @property
    def surface(self):
        import math
        return math.pi * (self._rayon ** 2)

c = Circle(5)
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
@decorator_1
@decorator_2
@decorator_3
fonction()
```

Cela équivaut à :
```python
fonction = decorator_1(decorator_2(decorator_3(fonction)))
```

L'ordre **va de bas en haut**.

---

## 7. Décorateurs pour les classes

Un décorateur peut également modifier des **classes** entières.

**Exemple simple :**

```python
def add_attribute(cls):
        cls.added_attribute = "Ajouté!"
        return cls

@add_attribute
class MyClass:
    pass

print(MyClass.added_attribute)
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
