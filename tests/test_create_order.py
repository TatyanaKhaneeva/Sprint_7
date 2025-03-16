import requests
import allure
import pytest
from data.URLs import url

class TestCreateOrder:

    @pytest.mark.parametrize('color', [
        ['BLACK'],
        ['GREY'],
        ['BLACK', 'GRAY'],
        []
    ])
    @allure.title('Создание заказа')
    @allure.description('Проверка создания заказа (код - 201 и track в ответе)')
    def test_create_order(self, color):

        payload = {
            "firstName": "Harry",
            "lastName": "Potter",
            "address": "Private Drive, 12 h.",
            "metroStation": 3,
            "phone": "+7 912 345 67 89",
            "rentTime": 3,
            "deliveryDate": "2025-03-23",
            "comment": "Harry, you're a wizard!",
            "color": color
        }

        r = requests.post(f"{url}/api/v1/orders", json=payload)
        assert r.status_code == 201
        assert 'track' in r.json()