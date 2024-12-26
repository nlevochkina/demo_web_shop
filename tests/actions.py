import requests
from selene import browser, be

def auth():
    response = requests.post(url='https://demowebshop.tricentis.com/login',
                             data={'email': 'qaguru1@example.com', 'password': '123456', 'RememberMe': False},
                             allow_redirects=False)
    cookie = response.cookies.get('NOPCOMMERCE.AUTH')
    browser.open('https://demowebshop.tricentis.com/')
    browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': cookie})
    browser.open('https://demowebshop.tricentis.com/')
    return response


def search(value):
    browser.element('#small-searchterms').click()
    browser.element('#small-searchterms').should(be.blank).type(value)
    browser.element("[type='submit']").press_enter()


def demo_shop_api(method, url, **kwargs):
    base_url = "https://demowebshop.tricentis.com/"
    new_url = base_url + url
    method = method.upper()
    response = requests.request(method=method, url=new_url, **kwargs)
    return response
