from selene import browser, be
from pages.locators import locators


class ComparePage:

    def open_compare_page(self):
        browser.element('.compare-products-page').should(be.visible)
        browser.element(locators.item_book).should(be.visible)


compare_page = ComparePage()
