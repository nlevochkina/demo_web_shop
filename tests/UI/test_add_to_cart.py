import allure
from pages.search_page import search_page
from pages.product_page import product_page
from pages.card_page import card_page


@allure.title('Добавление товара в корзину')
def test_add_to_cart(open_browser):
    """Проверяем, что товар добавляется в корзину"""

    with allure.step('Step 1. Выполняем поиск товара'):
        search_page.do_search('camera')

    with allure.step('Step 3. Выполняем поиск товара'):
        search_page.open_product('.product-title')

    with allure.step('Step 3. Добавляем товар в корзину'):
        product_page.add_to_cart()

    with allure.step('Step 4. Проверяем, что товар добавился в корзину'):
        card_page.open_card()
