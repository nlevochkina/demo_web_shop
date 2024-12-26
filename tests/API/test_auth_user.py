import allure
from tests import actions
from pages.main_page import main_page


@allure.title('Автотест на добавление товара в корзину авторизованным пользователем')
def test_auth_user():
    with allure.step('Step 1. Авторизовываемся через API'):
        response = actions.auth()

    with allure.step('Step 3. Проверяем, что авторизация произошла'):
        main_page.check_auth()
        assert response.status_code == 302
