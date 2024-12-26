from selene import browser, be, have
from tests import actions


class SearchPage:

    def do_search(self, value):
        actions.search(value)

    def open_product(self, value):
        browser.element(value).click()

    def choose_sort(self):
        browser.element('#products-orderby').click()
        browser.element(f'//*[text()="Name: Z to A"]').click()
        browser.element('.product-item').should(be.visible)

    def check_sort(self):
        browser.element('#products-orderby').should(have.text('Name: Z to A'))

    def check_search_on_tag(self):
        browser.element('.page-title').should(have.text("Products tagged with 'awesome'"))
        browser.element('.product-item').should(be.visible)


search_page = SearchPage()
