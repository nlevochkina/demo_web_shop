import allure
from pages.main_page import main_page
from pages.search_page import search_page
from pages.product_page import product_page


@allure.title('Проверяем отображение товаров в списке недавнопросмотренных')
def test_check_recently_viewed_products(open_browser):
    with allure.step('Step 1. Кликаем по категории books'):
        main_page.choose_category('a[href="/books"]')

    with allure.step('Step 2. Переходим на карточку товара'):
        search_page.open_product('a[href="/computing-and-internet"]')

    with allure.step('Step 3. Возвращаемся на главную страницу'):
        product_page.back_to_main_page()

    with allure.step('Step 4. Проверяем, что товар отображается в списке недавно просмотренных'):
        main_page.check_recently_viewed_products()
