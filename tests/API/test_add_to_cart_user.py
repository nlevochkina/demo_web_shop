import allure
import requests
from schemas.schemas import add_product
from jsonschema import validate


@allure.title('Автотест на добавление товара в корзину неавторизованным пользователем')
def test_add_to_cart_user():
    body = {
        "success": True,
    }

    with allure.step('Step 1. Добавляем товар в корзину через API'):
        response = requests.post(url='https://demowebshop.tricentis.com/addproducttocart/details/31/1',
                                 data=body)

    with allure.step('Step 2. Провряем, что товар добавлен в корзину'):
        assert response.status_code == 200
        body = response.json()
        validate(instance=body, schema=add_product)
