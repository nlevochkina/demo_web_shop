from selene import browser


class ProductPage:

    def add_to_cart(self):
        browser.element('.add-to-cart-button').click()

    def add_to_compare(self):
        browser.element('.compare-products').click()

    def back_to_main_page(self):
        browser.element('.header-logo').click()


product_page = ProductPage()
