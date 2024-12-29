import requests
from selene import browser, be
from tests.config import BASE_URL


def auth():
    response = requests.post(url=BASE_URL,
                             data={'email': 'qaguru1@example.com', 'password': '123456', 'RememberMe': False},
                             allow_redirects=False)
    cookie = response.cookies.get('NOPCOMMERCE.AUTH')
    browser.open(BASE_URL)
    browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': cookie})
    browser.open(BASE_URL)
    return response


def search(value):
    browser.element('#small-searchterms').click()
    browser.element('#small-searchterms').should(be.blank).type(value)
    browser.element("[type='submit']").press_enter()


def demo_shop_api(method, url, **kwargs):
    new_url = BASE_URL + url
    method = method.upper()
    response = requests.request(method=method, url=new_url, **kwargs)
    return response
