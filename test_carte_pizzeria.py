from mock import Mock, patch, PropertyMock
from carte_pizzeria import CartePizzeria, CartePizzeriaException
from carte_elements import Pizza, Drink, Dessert

# Method is_empty 

def test_carte_pizza_is_empty():
    """
    """
    carte_pizza = CartePizzeria()
    assert carte_pizza.is_empty()

@patch('carte_pizzeria.CartePizzeria.pizzas', new_callable=PropertyMock)
def test_carte_pizza_is_not_empty_with_pizzas(mock_pizzas):
    """Test carte pizzeria is not empty (has pizzas)
    """
    carte_pizza = CartePizzeria()
    element = Mock()
    mock_pizzas.return_value = [element]
    assert not carte_pizza.is_empty()

@patch('carte_pizzeria.CartePizzeria.drinks', new_callable=PropertyMock)
def test_carte_pizza_is_not_empty_with_drinks(mock_drinks):
    """Test carte pizzeria is not empty (has drinks)
    """
    carte_pizza = CartePizzeria()
    element = Mock()
    mock_drinks.return_value = [element]
    assert not carte_pizza.is_empty()

@patch('carte_pizzeria.CartePizzeria.desserts', new_callable=PropertyMock)
def test_carte_pizza_is_not_empty_with_desserts(mock_desserts):
    """Test carte pizzeria is not empty (has desserts)
    """
    carte_pizza = CartePizzeria()
    element = Mock()
    mock_desserts.return_value = [element]
    assert not carte_pizza.is_empty()

# Method nb_pizzas

def test_carte_pizza_nb_pizzas_with_no_pizzas():
    """Test nb pizzas with no pizzas
    """
    carte_pizza = CartePizzeria()
    assert carte_pizza.nb_pizzas() == 0

@patch('carte_pizzeria.CartePizzeria.pizzas', new_callable=PropertyMock)
def test_carte_pizza_nb_pizzas_with_multiple_pizzas(mock_pizzas):
    """Test nb pizzas with multiple pizzas
    """
    carte_pizza = CartePizzeria()
    element = Mock()
    mock_pizzas.return_value = [element, element]
    assert carte_pizza.nb_pizzas() == 2

# Method nb_drinks

def test_carte_pizza_nb_drinks_with_no_drinks():
    """
    """
    carte_pizza = CartePizzeria()
    assert carte_pizza.nb_drinks() == 0

@patch('carte_pizzeria.CartePizzeria.drinks', new_callable=PropertyMock)
def test_carte_pizza_nb_drinks_with_multiple_drinks(mock_drinks):
    """
    """
    carte_pizza = CartePizzeria()
    element = Mock()
    mock_drinks.return_value = [element, element]
    assert carte_pizza.nb_drinks() == 2

# Method nb_desserts

def test_carte_pizza_nb_desserts_with_no_desserts():
    """
    """
    carte_pizza = CartePizzeria()
    assert carte_pizza.nb_desserts() == 0

@patch('carte_pizzeria.CartePizzeria.desserts', new_callable=PropertyMock)
def test_carte_pizza_nb_desserts_with_multiple_desserts(mock_desserts):
    """
    """
    carte_pizza = CartePizzeria()
    element = Mock()
    mock_desserts.return_value = [element, element]
    assert carte_pizza.nb_desserts() == 2

# Method add

@patch('carte_pizzeria.CartePizzeria.pizzas', new_callable=PropertyMock)
def test_carte_pizza_add_pizza(mock_pizzas):
    """
    """
    carte_pizza = CartePizzeria()
    element = Mock(spec=Pizza)
    element.name = "Mocked Pizza"
    element.ingredients = ["Nothing"]
    mock_pizzas.return_value = [element]

    second_element = Mock(spec=Pizza)
    second_element.name = "Second Pizza"
    second_element.ingredients = ["Nothing", "Empty"]
    carte_pizza.add(second_element)

    thrid_element = Mock(spec=Pizza)
    thrid_element.name = "Third Pizza"
    thrid_element.ingredients = ["Empty"]
    carte_pizza.add(thrid_element)

def test_carte_pizza_add_drink():
    """
    """
    carte_pizza = CartePizzeria()
    element = Mock(spec=Drink)
    element.name = "Mocked Drink"
    carte_pizza.add(element)

def test_carte_pizza_add_dessert():
    """
    """
    carte_pizza = CartePizzeria()
    element = Mock(spec=Dessert)
    element.name = "Mocked Dessert"
    carte_pizza.add(element)

@patch('carte_pizzeria.CartePizzeria.pizzas', new_callable=PropertyMock)
def test_carte_pizza_add_failure_because_of_name(mock_pizzas):
    """
    """
    carte_pizza = CartePizzeria()
    element = Mock()
    element.name = "Mocked Pizza"
    mock_pizzas.return_value = [element]
    try:
        carte_pizza.add(element)
    except CartePizzeriaException:
        pass
    else:
        raise Exception("test should have failed")

@patch('carte_pizzeria.CartePizzeria.pizzas', new_callable=PropertyMock)
def test_carte_pizza_add_failure_because_of_pizza_ingredients(mock_pizzas):
    """
    """
    carte_pizza = CartePizzeria()
    element = Mock(spec=Pizza)
    element.name = "Mocked Pizza"
    element.ingredients = ["Nothing"]
    mock_pizzas.return_value = [element]
    other_element = Mock(spec=Pizza)
    other_element.name = "Other Pizza"
    other_element.ingredients = ["Nothing"]
    try:
        carte_pizza.add(other_element)
    except CartePizzeriaException:
        pass
    else:
        raise Exception("test should have failed")

# Method remove

@patch('carte_pizzeria.CartePizzeria.pizzas', new_callable=PropertyMock)
def test_carte_pizza_remove(mock_pizzas):
    """
    """
    carte_pizza = CartePizzeria()
    element = Mock()
    element_name = "Mocked Pizza"
    element.name = element_name
    mock_pizzas.return_value = [element]
    carte_pizza.remove(element_name)

@patch('carte_pizzeria.CartePizzeria.pizzas', new_callable=PropertyMock)
def test_carte_pizza_remove_failure(mock_pizzas):
    """
    """
    carte_pizza = CartePizzeria()
    element = Mock()
    element_name = "Mocked Pizza"
    element.name = element_name
    mock_pizzas.return_value = [element]
    try:
        carte_pizza.remove(element_name + " ")
    except CartePizzeriaException:
        pass
    else:
        raise Exception("test should have failed")
