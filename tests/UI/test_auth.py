import allure

from selene import browser, be, have


@allure.title('Авторизация на сайте')
def test_auth(open_browser):

    with allure.step('Step 1. Нажимаем кнопку Log in'):
        browser.element('a[href="/login"]').click()

    with allure.step('Step 2. Вводим email и password'):
        browser.element('#Email').click()
        browser.element('#Email').should(be.blank).type('qaguru1@example.com')
        browser.element('#Password').click()
        browser.element('#Password').should(be.blank).type('123456')
        browser.element('.login-button').click()

    with allure.step('Step 3. Проверяем, что авторизация произошла'):
        browser.element('.account').should(have.text('qaguru1@example.com'))