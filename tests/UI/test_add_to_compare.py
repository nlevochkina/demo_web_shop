import allure
from pages.search_page import search_page
from pages.product_page import product_page
from pages.compare_page import compare_page


@allure.title('Добавление товара в список сравнения')
def test_add_to_compare(open_browser):
    """Проверяем, что товар добавляется в список сравнения"""

    with allure.step('Step 1. Выполняем поиск товара'):
        search_page.do_search('book')

    with allure.step('Step 2. Открываем товар'):
        search_page.open_product('.product-title')

    with allure.step('Step 3. Добавляем товар в сравнение'):
        product_page.add_to_compare()

    with allure.step('Step 4. Проверяем, что товар добавился в сравнение'):
        compare_page.open_compare_page()
