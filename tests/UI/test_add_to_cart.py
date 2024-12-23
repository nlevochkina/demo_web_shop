import allure
import requests
from allure_commons.types import AttachmentType

from selene import browser, be


@allure.title('Добавление товара в корзину')
def test_add_to_cart(open_browser):

    with allure.step('Step 1. Авторизуемся пользователем через API'):
        login = requests.post(url='https://demowebshop.tricentis.com/login',
                              data={'email': 'qaguru1@example.com', 'password': '123456', 'RememberMe': False},
                              allow_redirects=False)
        allure.attach(body=login.text,
                      name='response',
                      attachment_type=AttachmentType.TEXT,
                      extension='txt')
        allure.attach(body=str(login.cookies),
                      name='cookie',
                      attachment_type=AttachmentType.TEXT,
                      extension='txt')

    with allure.step('Step 2. Получаем cookie через API'):
        cookie = login.cookies.get('NOPCOMMERCE.AUTH')
        browser.open('https://demowebshop.tricentis.com/')
        browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': cookie})
        browser.open('https://demowebshop.tricentis.com/')

    with allure.step('Step 3. Выполняем поиск товара'):
        browser.element('#small-searchterms').click()
        browser.element('#small-searchterms').should(be.blank).type('camera')
        browser.element("[type='submit']").press_enter()

    with allure.step('Step 4. Открываем товар'):
        browser.element('a[href="/digital-slr-camera"]').click()

    with allure.step('Step 5. Добавляем товар в корзину'):
        browser.element('.add-to-cart-button').click()

    with allure.step('Step 6. Проверяем, что товар добавился в корзину'):
        browser.open('https://demowebshop.tricentis.com/cart')
        browser.element('.cart-item-row').should(be.visible)


