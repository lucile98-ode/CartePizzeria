from mock import Mock, patch, PropertyMock
from carte_pizzeria import CartePizzeria, CartePizzeriaException
from carte_elements import Pizza, Drink, Dessert

# Method is_empty 

def test_carte_pizza_is_empty():
    c = CartePizzeria()
    assert c.is_empty()

@patch('carte_pizzeria.CartePizzeria.pizzas', new_callable=PropertyMock)
def test_carte_pizza_is_not_empty_with_pizzas(mock_pizzas):
    c = CartePizzeria()
    element = Mock()
    mock_pizzas.return_value = [element]
    assert not c.is_empty()

@patch('carte_pizzeria.CartePizzeria.drinks', new_callable=PropertyMock)
def test_carte_pizza_is_not_empty_with_drinks(mock_drinks):
    c = CartePizzeria()
    element = Mock()
    mock_drinks.return_value = [element]
    assert not c.is_empty()

@patch('carte_pizzeria.CartePizzeria.desserts', new_callable=PropertyMock)
def test_carte_pizza_is_not_empty_with_desserts(mock_desserts):
    c = CartePizzeria()
    element = Mock()
    mock_desserts.return_value = [element]
    assert not c.is_empty()

# Method nb_pizzas

def test_carte_pizza_nb_pizzas_with_no_pizzas():
    c = CartePizzeria()
    assert c.nb_pizzas() == 0

@patch('carte_pizzeria.CartePizzeria.pizzas', new_callable=PropertyMock)
def test_carte_pizza_nb_pizzas_with_multiple_pizzas(mock_pizzas):
    c = CartePizzeria()
    element = Mock()
    mock_pizzas.return_value = [element, element]
    assert c.nb_pizzas() == 2

# Method nb_drinks

def test_carte_pizza_nb_drinks_with_no_drinks():
    c = CartePizzeria()
    assert c.nb_drinks() == 0

@patch('carte_pizzeria.CartePizzeria.drinks', new_callable=PropertyMock)
def test_carte_pizza_nb_drinks_with_multiple_drinks(mock_drinks):
    c = CartePizzeria()
    element = Mock()
    mock_drinks.return_value = [element, element]
    assert c.nb_drinks() == 2

# Method nb_desserts

def test_carte_pizza_nb_desserts_with_no_desserts():
    c = CartePizzeria()
    assert c.nb_desserts() == 0

@patch('carte_pizzeria.CartePizzeria.desserts', new_callable=PropertyMock)
def test_carte_pizza_nb_desserts_with_multiple_desserts(mock_desserts):
    c = CartePizzeria()
    element = Mock()
    mock_desserts.return_value = [element, element]
    assert c.nb_desserts() == 2

# Method add

@patch('carte_pizzeria.CartePizzeria.pizzas', new_callable=PropertyMock)
def test_carte_pizza_add_pizza(mock_pizzas):
    c = CartePizzeria()
    element = Mock(spec=Pizza)
    element.name = "Mocked Pizza"
    element.ingredients = ["Nothing"]
    mock_pizzas.return_value = [element]

    second_element = Mock(spec=Pizza)
    second_element.name = "Second Pizza"
    second_element.ingredients = ["Nothing", "Empty"]
    c.add(second_element)

    thrid_element = Mock(spec=Pizza)
    thrid_element.name = "Third Pizza"
    thrid_element.ingredients = ["Empty"]
    c.add(thrid_element)

def test_carte_pizza_add_drink():
    c = CartePizzeria()
    element = Mock(spec=Drink)
    element.name = "Mocked Drink"
    c.add(element)

def test_carte_pizza_add_dessert():
    c = CartePizzeria()
    element = Mock(spec=Dessert)
    element.name = "Mocked Dessert"
    c.add(element)

@patch('carte_pizzeria.CartePizzeria.pizzas', new_callable=PropertyMock)
def test_carte_pizza_add_failure_because_of_name(mock_pizzas):
    c = CartePizzeria()
    element = Mock()
    element.name = "Mocked Pizza"
    mock_pizzas.return_value = [element]
    try:
        c.add(element)
    except CartePizzeriaException:
        pass
    else:
        raise Exception("test should have failed")

@patch('carte_pizzeria.CartePizzeria.pizzas', new_callable=PropertyMock)
def test_carte_pizza_add_failure_because_of_pizza_ingredients(mock_pizzas):
    c = CartePizzeria()
    element = Mock(spec=Pizza)
    element.name = "Mocked Pizza"
    element.ingredients = ["Nothing"]
    mock_pizzas.return_value = [element]
    other_element = Mock(spec=Pizza)
    other_element.name = "Other Pizza"
    other_element.ingredients = ["Nothing"]
    try:
        c.add(other_element)
    except CartePizzeriaException:
        pass
    else:
        raise Exception("test should have failed")

# Method remove

@patch('carte_pizzeria.CartePizzeria.pizzas', new_callable=PropertyMock)
def test_carte_pizza_remove(mock_pizzas):
    c = CartePizzeria()
    element = Mock()
    element_name = "Mocked Pizza"
    element.name = element_name
    mock_pizzas.return_value = [element]
    c.remove(element_name)

@patch('carte_pizzeria.CartePizzeria.pizzas', new_callable=PropertyMock)
def test_carte_pizza_remove_failure(mock_pizzas):
    c = CartePizzeria()
    element = Mock()
    element_name = "Mocked Pizza"
    element.name = element_name
    mock_pizzas.return_value = [element]
    try:
        c.remove(element_name + " ")
    except CartePizzeriaException:
        pass
    else:
        raise Exception("test should have failed")
