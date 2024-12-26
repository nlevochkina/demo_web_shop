from selene import browser, be


class CardPage:
    def open_card(self):
        browser.open('https://demowebshop.tricentis.com/cart')
        browser.element('.cart-item-row').should(be.visible)


card_page = CardPage()
