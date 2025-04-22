import requests
import allure
import pytest
from data.URLs import url
from helper.helper import Helper
from tests.conftest import generate_random_data

class TestCreateCourier:

    @allure.title('Создание курьера')
    @allure.step('Проверка создания курьера (код - 201 и текст - "ok": True')
    def test_create_courier(self, generate_random_data, delete_courier_after_test):
        payload = {
            "login": generate_random_data[0],
            "password": generate_random_data[1],
            "firstName": generate_random_data[2]
        }

        pytest.courier_login = payload["login"]
        pytest.courier_password = payload["password"]

        response = requests.post(f"{url}/api/v1/courier", data=payload)
        with allure.step("Проверка ответа ручки"):
            assert response.status_code == 201

        with allure.step("Проверка текста ответа"):
            response_text = '{"ok":true}'
            assert response.text == response_text




    @allure.title('Проверка невозможности создать курьера с существующим логином')
    @allure.description('Проверка, что нельзя создать курьера с уже существующими данными (код - 409 и текст - "message": "Этот логин уже используется. Попробуйте другой."')
    def test_create_courier_duplicate_login(self, generate_random_data, delete_courier_after_test):

        helper = Helper()
        password = helper.generate_random_string(5)
        firstName = helper.generate_random_string(7)
        payload = {
            "login": generate_random_data[0],
            "password": generate_random_data[1],
            "firstName": generate_random_data[2]
        }
        pytest.courier_login = payload["login"]
        pytest.courier_password = payload["password"]
        payload_for_error = {
            "login": generate_random_data[0],
            "password": password,
            "firstName": firstName
        }
        requests.post(f"{url}/api/v1/courier", data=payload)
        response = requests.post(f"{url}/api/v1/courier", data=payload_for_error)
        assert response.status_code == 409
        assert response.json() == {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."}, "Неверное содержимое ответа."


    @allure.title('Проверка невозможности создать курьера без логина')
    @allure.description(
            'Проверка заполнения не всех обязательных полей(логин). Курьер не создан (код - 400 и текст - "message": "Недостаточно данных для создания учетной записи")'
        )
    def test_create_courier_without_required_login(self, generate_random_data, delete_courier_after_test):
        payload = {
            "login": '',
            "password": generate_random_data[1],
            "firstName": generate_random_data[2]
        }
        pytest.courier_login = payload["login"]
        pytest.courier_password = payload["password"]

        response = requests.post(f"{url}/api/v1/courier", data=payload)

        assert response.status_code == 400
        assert response.json() == {"code": 400,
                                   "message": "Недостаточно данных для создания учетной записи"}, "Неверное содержимое ответа."

    @allure.title('Проверка невозможности создать курьера без пароля')
    @allure.description(
        'Проверка заполнения не всех обязательных полей(пароль). Курьер не создан (код - 400 и текст - "message": "Недостаточно данных для создания учетной записи")'
    )
    def test_create_courier_without_required_password(self, generate_random_data, delete_courier_after_test):
        payload = {
            "login": generate_random_data[0],
            "password": '',
            "firstName": generate_random_data[2]
        }
        pytest.courier_login = payload["login"]
        pytest.courier_password = payload["password"]

        response = requests.post(f"{url}/api/v1/courier", data=payload)

        assert response.status_code == 400
        assert response.json() == {"code": 400,
                                   "message": "Недостаточно данных для создания учетной записи"}, "Неверное содержимое ответа."