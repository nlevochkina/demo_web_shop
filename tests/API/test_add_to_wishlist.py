import allure
import requests
from schemas.schemas import add_to_wish_list
from jsonschema.validators import validate


@allure.title('Автотест на добавление товара в wishlist')
def test_add_to_wishlist():
    body = {
        "success": True,
    }

    with allure.step('Step 1. Добавляем товар в wishlist через API'):
        response = requests.post(url='https://demowebshop.tricentis.com/addproducttocart/details/53/2', data=body)
        body = response.json()
        validate(instance=body, schema=add_to_wish_list)

    with allure.step('Step 2. Проверяем, что товар добавлен'):
        assert response.status_code == 200
