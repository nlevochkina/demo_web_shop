import allure
import requests
from allure_commons.types import AttachmentType
from selene import browser, have


@allure.title('Автотест на добавление товара в корзину авторизованным пользователем')
def test_add_to_cart_auth_user():
    with allure.step('Step 1. Авторизовываемся через API'):
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

    with allure.step('Step 3. Проверяем, что авторизация произошла'):
        browser.element('.account').should(have.text('qaguru1@example.com'))

    with allure.step('Step 4. Добавляем товар в корзину через API'):
        requests.post(url='https://demowebshop.tricentis.com/addproducttocart/details/31/1',
                      cookies={'NOPCOMMERCE.AUTH': cookie})
        allure.attach(body=str(login.cookies),
                      name='cookie',
                      attachment_type=AttachmentType.TEXT,
                      extension='txt')

    with allure.step('Step 5. Провряем, что товар добавлен в корзину'):
        browser.open('https://demowebshop.tricentis.com/cart')
        browser.element('.product-name').should(have.text('14.1-inch Laptop'))