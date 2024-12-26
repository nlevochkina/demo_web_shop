import allure
from pages.main_page import main_page
from pages.search_page import search_page


@allure.title('Поиск товара по тегу')
def test_search_product_by_tag(open_browser):
    with allure.step('Step 1. Кликаем по тегу awesome'):
        main_page.click_on_tag()

    with allure.step('Step 2. Проверяем, что открылась страница с товарами по тегу'):
        search_page.check_search_on_tag()

    with allure.step('Step 3. Открываем карточку товара и проверяем наличие тега'):
        search_page.open_product('.picture')
