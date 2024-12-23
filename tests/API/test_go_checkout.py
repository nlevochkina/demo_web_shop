import allure
import requests
from allure_commons.types import AttachmentType
from selene import browser, have


@allure.title('Автотест на редирект со страницы чекаута')
def test_go_checkout():
    with allure.step('Step 1. Переходим на страницу чекаута неавторизованным пользователем'):
        response = requests.post('https://demowebshop.tricentis.com/onepagecheckout', allow_redirects=False)
        assert response.status_code == 302

    with allure.step('Step 2. Редиректимся на страницу корзины'):
        redirected_response = requests.get('https://demowebshop.tricentis.com/cart')
        assert redirected_response.status_code == 200