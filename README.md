# CartePizzeria
[TECHNOLOG] TD autours des tests et de l'Intégration Continue

Votre équipe est chargée de développer plusieurs éléments d'un projet associé à une Pizzeria.

Pour information, une pizza est un objet défini par un nom, une liste d'ingrédients et un prix.

# Exercice 1 - Créez un projet TD_Test_CI sur Github.

Le client sait qu'il servira des pizzas mais n'a pas encore définit tout ce qui composera son menu.
Dans un premier temps, il vous est demandé de coder la classe `CartePizzeria` mais pas la classe Pizza.
La classe CartePizzeria doit implémenter les méthodes suivantes :

- is_empty() -> retourne un booléen indiquant si la carte est vide ou non
- nb_pizzas() -> retourne le nombre de pizzas de la carte
- add_pizza(pizza) -> ajoute une pizza à la carte
- remove_pizza(name) -> retire la pizza nommée `name` de la carte, si celle-ci n'existe pas, lève une exception `CartePizzeriaException`

Pour cela il est attendu que vous utilisiez Git (en particulier les commandes `commit`, `branch`, `push`, ...)

# Exercice 2 - Créez vos tests unitaires

Bien que la class Pizza ne soit pas encore à disposition, vous allez réaliser les tests associés à la classe CartePizzeria en utilisant les mocks !

Note sur l'installation de `pytest` :
Pour les personnes sous linux, vous pouvez passer par `pip` ou `pip3` et tapper la commande `pip install pytest mock` ou `pip3 install pytest mock`.
Pour les autres, tappez `python3 -m pip install -U pytest` et `python3 -m pip install -U mock` (adaptation des commandes précédemment utilisez pour installer mypy).  

# Exercice 3 - Ajoutez de la CI à votre projet

Afin de rendre votre dépôt plus "sérieux" votre patron vous demande de réaliser quelque modification à votre dépôt:

- Mise en place d'une CI avec l'exécution des tests unitaires et une mesure du niveau de couverture du code. Pour cela, vous allez utiliser le package pytest-cov et définir que le niveau de couverture du code est insuffisant s'il est inférieur à 80% (`pytest --cov=. --cov-fail-under=80`, cf https://pytest-cov.readthedocs.io/en/latest/config.html)
- Desactivation du push dans la master ! 
- Activation des PR/MR si et seulement si le pipeline est OK ! 

# Exercice 4 - Elements de la carte et évolution de la carte

Le client a maintenant une meilleure vu sur ce qu'il aimerait avoir dans sa carte :
- Une pizza devra avoir un nom, un prix, une description, une séquence d'ingrédients ainsi qu'une indication sur sa base (tomate ou crème).
- Une boisson devra avoir un nom, un prix et une indication sur la présence d'alcool
- Un déssert devra avoir un nom, un prix, une liste d'ingredients et une indication sur sa réalisation "fait maison" ou non.

Par ailleurs, il vous est demandé de retravailler la classe `CartePizzeria` pour ajouter les méthodes suivantes :
- nb_drinks() -> retourne le nombre de boissons dans la carte
- nb_desserts() -> retourne le nombre de désserts dans la carte
- add(element) -> ajoute `element` à la carte si celui-ci n'est pas déjà présent, sinon déclenche une exception `CartePizzeriaException`
  la présence d'un élément dans la carte suit les règles suivantes :
	- il existe déjà un élément ayant le même nom
	- si l'élément est une pizza, celle-ci est considérée présente s'il existe une autre pizza avec les mêmes ingrédients et même base
- remove(name) -> retire l'élément nommé `name` dans la carte
- trois getters retournant respectivement la liste des pizzas, boissons et désserts.

L'apparition des méthodes `add` et `remove` vous amène à retirer les méthodes `add_pizza` et `remove_pizza`.

# Exercice 5 - Facilité la vie au client

Maintenant que la classe `CartePizzeria` convient au client, celui-ci souhaite pouvoir disposer d'une classe `ClientOrder`.
Celle-ci encapsule la commande du client et doit lui permettre de facilement pouvoir interagir avec la carte.
Le client souhaite y retrouver les méthodes :
- current_order() -> retourne la liste des éléments de la commande en cours 
- price_current_order() -> retourne le prix de la commande en cours
- select_pizza(int i) -> ajoute la $i$-ème pizza à la commande courante (i commence à 1)
- select_drink(int i) -> ajoute la $i$-ème boisson à la commande courante (i commence à 1)
- select_dessert(int i) -> ajoute le $i$-ème déssert à la commande courante (i commence à 1)
- ajout une méthode qui facilite la vie à l'utilisateur sur ses choix de pizza, i.e. retourne la liste des pizzas respectant un critère:
	- d'inclusion (liste d'ingrédients)
	- d'exclusion (prix)

# Exercice 6 -  Extra

Ajoutez d'autre jobs à la CI :
	- linter (niveau de propreté à votre convenance)
	- typage statique (actif ou pas)
