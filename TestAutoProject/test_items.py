import time
import pytest
from selenium.webdriver.common.by import By

link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


class TestAddToBasket():
    @pytest.mark.smoke
    def test_add_to_basket_btn_is_displayed(self, browser):
        browser.get(link)
        # time.sleep(30)
        basket_btn = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
        assert basket_btn.is_displayed, "Basket button isn't displayed"

        '''Если выдает pytest: error: unrecognized arguments: --language=es, запускать тест из директории 
        TestAutoProject, а не из SelenMultipleLanguagesTestPackage'''

