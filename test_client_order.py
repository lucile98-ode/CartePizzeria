from mock import Mock, patch, PropertyMock
from client_order import ClientOrder, OrderException

# Method current_order

def test_client_order_current_order_empty():
    carte = Mock()
    co = ClientOrder(carte)
    assert co.current_order == []

# Method add

@patch('client_order.ClientOrder.current_order', new_callable=PropertyMock)
def test_client_order_price_current_order(mock_current_order):
    carte = Mock()
    co = ClientOrder(carte)
    element = Mock()
    element.price = 12.0
    mock_current_order.return_value = [element, element]
    assert co.price_current_order() == 24.0

# Method select_pizza

def test_client_order_select_pizza():
    element = Mock()
    carte = Mock()
    carte.pizzas = [element]
    carte.nb_pizzas.return_value = 1
    co = ClientOrder(carte)
    co.select_pizza(1)

def test_client_order_select_pizza_failure_index_min_val():
    carte = Mock()
    co = ClientOrder(carte)
    try:
        co.select_pizza(0)
    except OrderException:
        pass
    else:
        raise Exception("test should have failed")

def test_client_order_select_pizza_failure_index_max_val():
    carte = Mock()
    carte.nb_pizzas.return_value = 1
    co = ClientOrder(carte)
    try:
        co.select_pizza(2)
    except OrderException:
        pass
    else:
        raise Exception("test should have failed")

# ...