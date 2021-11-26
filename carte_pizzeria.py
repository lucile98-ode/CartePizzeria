"""Module defining CartePizzeria and CartePizzeriaException classes
"""
from carte_elements import Pizza, Drink, Dessert
from utils import same_ingredients

class CartePizzeriaException(Exception):
    """CartePizzeria dedicated exception
    """
    pass

class CartePizzeria:

    def __init__(self):
        self.__pizzas = []
        self.__drinks = []
        self.__desserts = []

    @property
    def pizzas(self):
        """Return pizzas private attribute
        """
        return self.__pizzas

    @property
    def drinks(self):
        """Return drinks private attribute
        """
        return self.__drinks

    @property
    def desserts(self):
        """Return desserts private attribute
        """
        return self.__desserts

    def is_empty(self):
        """Return True if it is empty, False otherwise
        """
        return self.nb_pizzas() + self.nb_drinks() +  self.nb_desserts() == 0

    def nb_pizzas(self):
        """Return the number of pizzas
        """
        return len(self.pizzas)

    def nb_drinks(self):
        """Return the number of drinks
        """
        return len(self.drinks)

    def nb_desserts(self):
        """Return the number of desserts
        """
        return len(self.desserts)

    def add(self, element):
        """Add an new element if it is not already registered.
        If the element is already registered, an exception is raised.
        """
        if self.__contains_name(element.name):
            raise CartePizzeriaException(f"element {element.name} is already registered")
        if isinstance(element, Pizza):
            if self.__contains_pizza_ingredients(element.ingredients):
                raise CartePizzeriaException(f"element {element.name} is already registered with another name")
            self.pizzas.append(element)
        elif isinstance(element, Drink):
            self.drinks.append(element)
        else:
            self.desserts.append(element)

    def __contains_name(self, name):
        """Return True if the name is equal to some registered element,
        False otherwise.
        """
        all_elements = self.pizzas + self.desserts + self.drinks
        for element in all_elements:
            if element.name == name:
                return True
        return False

    def __contains_pizza_ingredients(self, pizza_ingredients):
        """Return True if a registered pizza has the same ingredients
        as *pizza_ingredients*, Flase otherwise.
        """
        for pizza in self.pizzas:
            iter_ingredients = pizza.ingredients
            if same_ingredients(pizza_ingredients, iter_ingredients):
                return True
        return False

    def remove(self, name):
        """Remove an element based on its name. An exception is raised if
        the name is not registered.
        """
        found = False
        elements_per_type = [self.pizzas, self.desserts, self.drinks]
        for elements in elements_per_type:
            for pos, element in enumerate(elements):
                if element.name == name:
                    found = True
                    break
            if found:
                break
        if not found:
            raise CartePizzeriaException(f"element {element.name} is not registered")
        del elements[pos]

