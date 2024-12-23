import allure

from selene import browser, be, have


@allure.title('Проверка изменения сортировки на странице категории')
def test_choose_category(open_browser):

    with allure.step('Step 1. Переходим в категорию'):
        browser.element('a[href="/jewelry"]').click()

    with allure.step('Step 2. Выбираем сортировку от Z до А'):
        browser.element('#products-orderby').click()
        browser.element(f'//*[text()="Name: Z to A"]').click()
        browser.element('.product-item').should(be.visible)

    with allure.step('Step 3. Проверяем, что изменение сортировки произошла'):
        browser.element('#products-orderby').should(have.text('Name: Z to A'))
