import allure
from tests import actions


@allure.title('Автотест на редирект со страницы чекаута')
def test_go_checkout():
    with allure.step('Step 1. Переходим на страницу чекаута неавторизованным пользователем'):
        response = actions.demo_shop_api(method='post', url='onepagecheckout', allow_redirects=False)
        assert response.status_code == 302

    with allure.step('Step 2. Редиректимся на страницу корзины'):
        redirected_response = actions.demo_shop_api(method='get', url='/cart')
        assert redirected_response.status_code == 200
