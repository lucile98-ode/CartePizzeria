
class CartePizzeriaException(Exception):
    pass

class CartePizzeria:

    def __init__(self):
        self.__pizzas = []

    @property
    def pizzas(self):
        return self.__pizzas

    def is_empty(self):
        return len(self.pizzas) == 0

    def nb_pizzas(self):
        return len(self.pizzas)

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def remove_pizza(self, name):
        found = False
        for pos, inner_pizza in enumerate(self.pizzas):
            if inner_pizza.name == name:
                found = True
                break
        if not found:
            raise CartePizzeriaException(f"pizza {name} is not registered")
        del self.pizzas[pos]
