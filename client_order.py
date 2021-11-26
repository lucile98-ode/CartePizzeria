from carte_pizzeria import CartePizzeria

class OrderException(Exception):
    pass

class ClientOrder:

    def __init__(self, carte):
        self.__carte = carte
        self.__current_order = []

    @property
    def current_order(self):
        return self.__current_order

    def price_current_order(self):
        price = 0.0
        for element in self.current_order:
            price += element.price
        return price

    def select_pizza(self, i):
        if i <= 0:
            raise OrderException("index must be higher than 0")
        nb_pizzas = self.__carte.nb_pizzas()
        if i > nb_pizzas:
            raise OrderException(f"index must be lower than {nb_pizzas} (= nb_pizzas)")
        pizza = self.__carte.pizzas[i-1]
        self.current_order.append(pizza)

    def select_drink(self, i):
        if i <= 0:
            raise OrderException("index must be higher than 0")
        nb_drinks = self.__carte.nb_drinks()
        if i > nb_drinks:
            raise OrderException(f"index must be lower than {nb_drinks} (= nb_drinks)")
        drink = self.__carte.drinks[i-1]
        self.current_order.append(drink)

    def select_dessert(self, i):
        if i <= 0:
            raise OrderException("index must be higher than 0")
        nb_desserts = self.__carte.nb_desserts()
        if i > nb_desserts:
            raise OrderException(f"index must be lower than {nb_desserts} (= nb_desserts)")
        dessert = self.__carte.desserts[i-1]
        self.current_order.append(dessert)

    def inclusive_pizza_filtering(self, ingredients):
        res = []
        for pizza in self.__carte.pizzas:
            if set(ingredients).issubset(pizza.ingredients):
                res.append(pizza)
        return res

    def exclusive_pizza_filtering(self, max_price):
        res = []
        for pizza in self.__carte.pizzas:
            if pizza.price <= max_price:
                res.append(pizza)
        return res
