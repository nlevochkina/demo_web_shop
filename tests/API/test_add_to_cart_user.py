import allure
import requests


@allure.title('Автотест на добавление товара в корзину неавторизованным пользователем')
def test_add_to_cart_user():
    with allure.step('Step 1. Добавляем товар в корзину через API'):
        response = requests.post(url='https://demowebshop.tricentis.com/addproducttocart/details/31/1')

    with allure.step('Step 2. Провряем, что товар добавлен в корзину'):
        assert response.status_code == 200



