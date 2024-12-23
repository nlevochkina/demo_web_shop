import allure

from selene import browser, be


@allure.title('Добавляем товар в сравнение')
def test_add_to_compare(open_browser):

    with allure.step('Step 1. Выполняем поиск товара'):
        browser.element('#small-searchterms').click()
        browser.element('#small-searchterms').should(be.blank).type('computer')
        browser.element("[type='submit']").press_enter()

    with allure.step('Step 2. Открываем товар'):
        browser.element('a[href="/simple-computer"]').click()

    with allure.step('Step 3. Добавляем товар в сравнение'):
        browser.element('.compare-products').click()

    with allure.step('Step 4. Проверяем, что товар добавился в сравнение'):
        browser.element('.compare-products-page').should(be.visible)
        browser.element('a[href="/simple-computer"]').should(be.visible)
