import allure
from tests import actions
from schemas.schemas import add_product
from jsonschema.validators import validate


@allure.title('Автотест на добавление товара в корзину неавторизованным пользователем')
def test_add_to_cart_user():
    body = {
        'success': True,
        'message': 'The product has been added to your shopping cart',
        'updatetopcartsectionhtml': '1'
    }

    with allure.step('Step 1. Добавляем товар в корзину через API'):
        response = actions.demo_shop_api(method='post', url='addproducttocart/details/31/1', data=body)

    with allure.step('Step 2. Провряем, что товар добавлен в корзину'):
        assert response.status_code == 200
        body = response.json()
        validate(instance=body, schema=add_product)
