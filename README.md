test_create_order - проверка создания заказа (код - 201 и track в ответе)
test_create_courier - проверка создания курьера (код - 201 и текст - "ok": True'
test_create_courier_duplicate_login - проверка, что нельзя создать курьера с уже существующими данными (код - 409 и текст - "message": "Этот логин уже используется. Попробуйте другой."
test_create_courier_without_required_login - проверка невозможности создать курьера без логина
test_create_courier_without_required_password - проверка невозможности создать курьера без пароля
test_get_list_of_orders - проверка получения списка заказов
test_get_courier_id - проверка получения ID курьера при авторизации с валидным login и password
test_login_with_wrong_password - проверка, что авторизация курьера не пройдена при отправке неверного password
test_login_courier_without_password - проверка, что авторизация курьера не пройдена без пароля
test_login_courier_without_login - проверка, что авторизация курьера не пройдена без логина
