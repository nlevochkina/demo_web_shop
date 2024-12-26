import allure
from pages.main_page import main_page
from pages.search_page import search_page


@allure.title('Проверка изменения сортировки на странице категории')
def test_choose_category(open_browser):
    with allure.step('Step 1. Переходим в категорию'):
        main_page.choose_category('a[href="/jewelry"]')

    with allure.step('Step 2. Выбираем сортировку от Z до А'):
        search_page.choose_sort()

    with allure.step('Step 3. Проверяем, что изменение сортировки произошла'):
        search_page.choose_sort()
