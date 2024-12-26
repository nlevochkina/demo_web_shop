from selene import browser, be


class ComparePage:

    def open_compare_page(self):
        browser.element('.compare-products-page').should(be.visible)
        browser.element('a[href="/health"]').should(be.visible)


compare_page = ComparePage()
