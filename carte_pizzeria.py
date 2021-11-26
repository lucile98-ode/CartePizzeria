from carte_elements import Pizza, Drink, Dessert
from utils import same_ingredients

class CartePizzeriaException(Exception):
    pass

class CartePizzeria:

    def __init__(self):
        self.__pizzas = []
        self.__drinks = []
        self.__desserts = []

    @property
    def pizzas(self):
        return self.__pizzas

    @property
    def drinks(self):
        return self.__drinks

    @property
    def desserts(self):
        return self.__desserts

    def is_empty(self):
        return self.nb_pizzas() + self.nb_drinks() +  self.nb_desserts() == 0

    def nb_pizzas(self):
        return len(self.pizzas)

    def nb_drinks(self):
        return len(self.drinks)

    def nb_desserts(self):
        return len(self.desserts)

    def add(self, element):
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
        all_elements = self.pizzas + self.desserts + self.drinks
        for element in all_elements:
            if element.name == name:
                return True
        return False

    def __contains_pizza_ingredients(self, pizza_ingredients):
        for pizza in self.pizzas:
            iter_ingredients = pizza.ingredients
            if same_ingredients(pizza_ingredients, iter_ingredients):
                return True
        return False

    def remove(self, name):
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

