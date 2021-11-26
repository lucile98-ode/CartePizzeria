from mock import Mock, patch, PropertyMock
from carte_pizzeria import CartePizzeria, CartePizzeriaException

def test_carte_pizza_is_empty():
    c = CartePizzeria()
    assert c.is_empty()

@patch('carte_pizzeria.CartePizzeria.pizzas', new_callable=PropertyMock)
def test_carte_pizza_is_not_empty(mock_pizzas):
    c = CartePizzeria()
    element = Mock()
    mock_pizzas.return_value = [element]
    assert not c.is_empty()

def test_carte_pizza_nb_pizzas_with_no_pizzas():
    c = CartePizzeria()
    assert c.nb_pizzas() == 0

@patch('carte_pizzeria.CartePizzeria.pizzas', new_callable=PropertyMock)
def test_carte_pizza_nb_pizzas_with_multiple_pizzas(mock_pizzas):
    c = CartePizzeria()
    element = Mock()
    mock_pizzas.return_value = [element, element]
    assert c.nb_pizzas() == 2

def test_carte_pizza_add_pizza():
    c = CartePizzeria()
    pizza = Mock()
    c.add_pizza(pizza)

@patch('carte_pizzeria.CartePizzeria.pizzas', new_callable=PropertyMock)
def test_carte_pizza_remove_pizza(mock_pizzas):
    c = CartePizzeria()
    pizza_name = "Mocked Pizza"
    pizza = Mock()
    pizza.name = pizza_name
    mock_pizzas.return_value = [pizza]
    c.remove_pizza(pizza_name)

@patch('carte_pizzeria.CartePizzeria.pizzas', new_callable=PropertyMock)
def test_carte_pizza_remove_pizza_failure(mock_pizzas):
    c = CartePizzeria()
    pizza_name = "Mocked Pizza"
    pizza = Mock()
    pizza.name = pizza_name + "X"
    mock_pizzas.return_value = [pizza]
    try:
        c.remove_pizza(pizza_name)
    except CartePizzeriaException:
        pass
    else:
        raise Exception("test should have failed")