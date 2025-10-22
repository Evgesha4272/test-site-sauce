from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class CartPage(Base):

    def __init__(self, driver):
        super(). __init__(driver)
        self.driver = driver

    # Locators
    btn_checkout = '//button[@id="checkout"]'

    # Getters
    def get_btn_checkout(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.btn_checkout)))

    # Actions
    def click_btn_checkout(self):
        self.get_btn_checkout().click()
        print('Click btn checkout.')

    # Methods
    def product_confirm(self):
        self.get_current_url()
        self.click_btn_checkout()