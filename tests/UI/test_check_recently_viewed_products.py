import allure
from pages.locators import locators
from pages.main_page import main_page
from pages.search_page import search_page
from pages.product_page import product_page


@allure.title('Отображение товаров в списке недавнопросмотренных')
def test_check_recently_viewed_products(open_browser):
    """Проверяем отображение товаров в списке недавнопросмотренных"""

    with allure.step('Step 1. Кликаем по категории books'):
        main_page.choose_category(locators.category_books)

    with allure.step('Step 2. Переходим на карточку товара'):
        search_page.open_product(locators.product_computer)

    with allure.step('Step 3. Возвращаемся на главную страницу'):
        product_page.back_to_main_page()

    with allure.step('Step 4. Проверяем, что товар отображается в списке недавно просмотренных'):
        main_page.check_recently_viewed_products()
