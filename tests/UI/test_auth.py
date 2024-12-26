import allure
from pages.main_page import main_page


@allure.title('Авторизация на сайте')
def test_auth(open_browser):
    with allure.step('Step 1. Нажимаем кнопку Log in'):
        main_page.login()

    with allure.step('Step 3. Проверяем, что авторизация произошла'):
        main_page.check_auth()
