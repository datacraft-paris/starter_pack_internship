# Programmation Orientée Objet

La programmation orientée objet (POO) est un style de programmation dans lequel l’accent est mis sur les objets réutilisables pour faire les choses, plutôt que sur les procédures étape par étape.

La POO est particulièrement adaptée lorsque l'on souhaite créer des programmes **structurés, évolutifs** et **faciles à maintenir** dans le temps.

Dans la POO, tout commence par une **classe**, qui définit un type d’objet avec :

- des **attributs** (les données),
- et des **méthodes** (les fonctions associées à ces données).

Chaque **instance** d'une classe possède ses propres attributs, ce qui permet à chaque objet de fonctionner de manière **indépendante**.

---

## Les 4 principes fondamentaux de la POO

- **Encapsulation** :  
  L’objet regroupe les données et les méthodes qui les manipulent. Cela permet de **protéger les données internes** et de ne donner accès qu’à ce qui est nécessaire.

- **Héritage** :  
  Une classe peut hériter des propriétés et méthodes d’une autre classe. Cela permet de **réutiliser du code** et de structurer des hiérarchies logiques.

- **Polymorphisme** :  
  Plusieurs objets peuvent partager le **même nom de méthode**, mais avoir des **comportements différents**. Cela rend le code plus flexible et générique.

- **Abstraction** :  
  L’utilisateur d’un objet n’a pas besoin de connaître les détails internes de son fonctionnement. On **cache la complexité** derrière des interfaces simples.

---

## Le constructeur `__init__` et la création d’objets

Quand on crée un objet, Python appelle automatiquement une méthode spéciale appelée `__init__`.  
C’est ici que l’on initialise les attributs propres à chaque instance.

**Exemple avec la classe `Event` :**
```py
        class Event:
            def __init__(self, date: str, location: str, participants: list[str], topic: str, event_id: int):
                self.date = date
                self.location = location
                self.participants = participants
                self.topic = topic
                self.event_id = event_id

        e = Event("2025-06-15", "Paris", ["Alice", "Bob"], "IA et société", 1)
```

---

## Encapsulation et convention `_attribute`

Par convention, un attribut dont le nom commence par un underscore (`_`) est considéré comme **protégé**.  
Cela signifie qu’il **ne doit pas être accédé ou modifié directement depuis l’extérieur**, même s’il reste accessible techniquement.

**Exemple :**
```py

        self._participants = participants
```
---

## Affichage personnalisé avec `__str__`

La méthode spéciale `__str__` permet de **définir ce qui s'affiche** lorsqu'on fait `print(my_object)`.

**Exemple dans la classe `Event` :**
```py
        def __str__(self):
            return f"Événement '{self.topic}' le {self.date} à {self.location} avec {len(self.participants)} participants"
```
Ainsi :
```py
        print(e)
```
donnera :
```text
        Événement 'IA et société' le 2025-06-15 à Paris avec 2 participants
```
---

## Bonnes pratiques

- N’accédez pas directement aux attributs depuis l’extérieur : utilisez des méthodes dédiées si besoin.
- Donnez des **noms clairs et cohérents** aux classes, variables et fonctions.
- Une classe = une responsabilité principale.
- Factorisez le code redondant ; utilisez l’héritage si c’est pertinent.
- Ajoutez toujours `__str__` pour faciliter l'affichage et le débogage.

---

## Exemple complet : classe `Event`

Complétez ou inspirez-vous de ce modèle pour votre propre classe :
```py
        class Event:
            def __init__(self, date: str, location: str, participants: list[str], topic: str, event_id: int):
                self.date = date
                self.location = location
                self.participants = participants
                self.topic = topic
                self.event_id = event_id

            def __str__(self):
                return f"Événement '{self.topic}' le {self.date} à {self.location} avec {len(self.participants)} participants"

        e = Event("2025-06-15", "Paris", ["Alice", "Bob"], "IA et société", 1)
        print(e)
```
**Sortie attendue :**
```text
        Événement 'IA et société' le 2025-06-15 à Paris avec 2 participants
```
---

## À faire

Allez dans le dossier `oop` et observez le fichier `exemple_class.py`.

Créez votre propre classe `Event`, inspirez-vous du modèle ci-dessus, puis :

- ajoutez des méthodes utiles (ex : `add_participant()`, `get_number_of_participants()`)
- testez votre code avec plusieurs événements différents
- affichez chaque objet à l’aide de `print()`
