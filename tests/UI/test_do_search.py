import allure
from pages.search_page import search_page


@allure.title('Поиск товара')
def test_do_search(open_browser):
    with allure.step('Step 1. Выполняем поиск товара'):
        search_page.do_search('computer')

    with allure.step('Step 2. Проверяем что на странице поиска есть товар'):
        search_page.open_product('a[href="/simple-computer"]')
