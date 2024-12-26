from selene import browser, be, have


class MainPage:

    def login(self):
        browser.element('a[href="/login"]').click()
        browser.element('#Email').click()
        browser.element('#Email').should(be.blank).type('qaguru1@example.com')
        browser.element('#Password').click()
        browser.element('#Password').should(be.blank).type('123456')
        browser.element('.login-button').click()

    def check_auth(self):
        browser.element('.account').should(have.text('qaguru1@example.com'))

    def choose_category(self, value):
        browser.element(value).click()

    def check_recently_viewed_products(self):
        browser.element('a[href="/computing-and-internet"]').should(be.visible)

    def click_on_tag(self):
        browser.element('a[href="/producttag/8/awesome"]').click()


main_page = MainPage()
