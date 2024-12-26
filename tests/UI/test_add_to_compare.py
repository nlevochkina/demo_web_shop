import allure
from pages.search_page import search_page
from pages.product_page import product_page
from pages.compare_page import compare_page
from selene import browser, be


@allure.title('Добавляем товар в сравнение')
def test_add_to_compare(open_browser):
    with allure.step('Step 1. Выполняем поиск товара'):
        search_page.do_search('book')

    with allure.step('Step 2. Открываем товар'):
        browser.element('a[href="/health"]').click()

    with allure.step('Step 3. Добавляем товар в сравнение'):
        product_page.add_to_compare()

    with allure.step('Step 4. Проверяем, что товар добавился в сравнение'):
        compare_page.open_compare_page()
