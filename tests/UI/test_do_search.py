import allure

from selene import browser, be


@allure.title('Поиск товара')
def test_do_search(open_browser):

    with allure.step('Step 1. Выполняем поиск товара'):
        browser.element('#small-searchterms').click()
        browser.element('#small-searchterms').should(be.blank).type('computer')
        browser.element("[type='submit']").press_enter()

    with allure.step('Step 2. Проверяем что на странице поиска есть товар'):
        browser.element('a[href="/simple-computer"]').should(be.visible)
