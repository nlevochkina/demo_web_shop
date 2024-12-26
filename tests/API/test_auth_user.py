import allure
from tests import actions
from selene import browser, have


@allure.title('Автотест на добавление товара в корзину авторизованным пользователем')
def test_auth_user():
    with allure.step('Step 1. Авторизовываемся через API'):
        response = actions.auth()

    with allure.step('Step 3. Проверяем, что авторизация произошла'):
        browser.element('.account').should(have.text('qaguru1@example.com'))
        assert response.status_code == 302
