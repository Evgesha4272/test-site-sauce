from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class UserPage(Base):

    def __init__(self, driver):
        super(). __init__(driver)
        self.driver = driver

    # Locators
    input_first_name = '//input[@id="first-name"]'
    input_last_name = '//input[@id="last-name"]'
    input_zip_code = '//input[@id="postal-code"]'
    btn_continue = '//input[@id="continue"]'

    # Variables
    first_name = 'Alex'
    last_name = 'Smith'
    zip_code = '12345'

    # Getters
    # Get input first name
    def get_input_first_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.input_first_name)))

    # Get input last name
    def get_input_last_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.input_last_name)))

    # Get input zip code
    def get_input_zip_code(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.input_zip_code)))

    # Get btn continue
    def get_btn_continue(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.btn_continue)))

    # Actions
    # Put data in input first name
    def put_input_first_name(self):
        self.get_input_first_name().send_keys(self.first_name)
        print('Input first name was successfully entered.')

    # Put data in input last name
    def put_input_last_name(self):
        self.get_input_last_name().send_keys(self.last_name)
        print('Input last name was successfully entered.')

    # Put data in input zip
    def put_input_zip_code(self):
        self.get_input_zip_code().send_keys(self.zip_code)
        print('Input zip code was successfully entered.')

    # Click btn continue
    def click_btn_continue(self):
        self.get_btn_continue().click()
        print('Btn continue was successfully clicked.')

    # Methods
    def input_information(self):
        self.get_current_url()
        self.put_input_first_name()
        self.put_input_last_name()
        self.put_input_zip_code()
        self.click_btn_continue()