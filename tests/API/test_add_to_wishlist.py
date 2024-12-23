import allure
import requests


@allure.title('Автотест на добавление товара в wishlist')
def test_add_to_wishlist():
    with allure.step('Step 1. Добавляем товар в wishlist через API'):
        response = requests.post(url='https://demowebshop.tricentis.com/compareproducts/add/44')

    with allure.step('Step 2. Проверяем, что товар добавлен'):
        assert response.status_code == 200