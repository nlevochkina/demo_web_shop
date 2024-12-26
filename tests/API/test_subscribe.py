import allure
import json
from tests import actions
from schemas.schemas import subscribe
from jsonschema.validators import validate


def test_subscribe():
    with allure.step('Step 1. Авторизовываемся через API'):
        actions.auth()

    with allure.step('Step 2. Отправляем запрос на подписку'):
        response = actions.demo_shop_api(method='post', url='subscribenewsletter',
                                         data={'email': '1234@mail.ru'})
        assert response.status_code == 200
        content = response.text
        json_data = json.loads(content)
        validate(instance=json_data, schema=subscribe)
