from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class CheckoutPage(Base):

    def __init__(self, driver):
        super(). __init__(driver)
        self.driver = driver

    # Locators
    input_first_name = '//input[@id="first-name"]'
    input_last_name = '//input[@id="last-name"]'
    input_zip_code = '//input[@id="postal-code"]'
    btn_finish = '//button[@id="finish"]'

    # Getters
    # Get btn continue
    def get_btn_finish(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.btn_finish)))

    # Actions
    # Click btn continue
    def click_btn_finish(self):
        self.get_btn_finish().click()
        print('Btn finish was successfully clicked.')

    # Methods
    def payment(self):
        self.get_current_url()
        self.click_btn_finish()