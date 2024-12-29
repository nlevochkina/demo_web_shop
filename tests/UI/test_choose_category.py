import allure
from pages.locators import locators
from pages.main_page import main_page
from pages.search_page import search_page


@allure.title('Изменение сортировки на странице категории')
def test_choose_category(open_browser):
    """Проверяем изменение сортировки на странице категории"""

    with allure.step('Step 1. Переходим в категорию'):
        main_page.choose_category(locators.category_jewelry)

    with allure.step('Step 2. Выбираем сортировку от Z до А'):
        search_page.choose_sort()

    with allure.step('Step 3. Проверяем, что изменение сортировки произошла'):
        search_page.choose_sort()
