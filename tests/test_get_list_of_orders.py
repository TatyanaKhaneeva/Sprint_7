import requests
import allure
from data.URLs import url

class TestGetListOfOrders:


    @allure.title('Получение списка заказов')
    @allure.description('Получение списка заказов (код - 200 и "orders" в ответе)')
    def test_get_list_of_orders(self):

        payload = {
            "firstName": "Harry",
            "lastName": "Potter",
            "address": "Private Drive, 12 h.",
            "metroStation": 3,
            "phone": "+7 912 345 67 89",
            "rentTime": 3,
            "deliveryDate": "2025-03-23",
            "comment": "Harry, you're a wizard!",
            "color": "GREY"
        }

        requests.post(f"{url}/api/v1/orders", json=payload)
        r = requests.get(f"{url}/api/v1/orders")
        assert r.status_code == 200
        assert 'orders' in r.json()