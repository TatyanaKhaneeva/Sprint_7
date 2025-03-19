import pytest
import requests
import random
import string

from helper.helper import Helper


@pytest.fixture
def register_new_courier_and_return_login_password():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login_pass = []

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    yield login_pass

    payload = {
        "login": login_pass[0],
        "password": login_pass[1]
    }

    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
    response_data = response.json()
    courier_id = response_data['id']

    response = requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{courier_id}')



@pytest.fixture
def generate_random_data():
    helper = Helper()
    login = helper.generate_random_string(10)
    password = helper.generate_random_string(10)
    first_name = helper.generate_random_string(10)
    user_data = []
    user_data.append(login)
    user_data.append(password)
    user_data.append(first_name)
    return user_data


@pytest.fixture
def delete_courier_after_test():
    yield

    login_payload = {
        "login": pytest.courier_login,
        "password": pytest.courier_password
    }

    login_response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=login_payload)

    courier_id = login_response.json().get('id')
    requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{courier_id}')
