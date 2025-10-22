from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class MainPage(Base):

    def __init__(self, driver):
        super(). __init__(driver)
        self.driver = driver

    # Locator
    # Locators for select products
    select_product_1 = '//button[@id="add-to-cart-sauce-labs-backpack"]'
    select_product_2 = '//button[@id="add-to-cart-sauce-labs-bike-light"]'
    select_product_3 = '//button[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'
    cart = '//div[@id="shopping_cart_container"]'

    # Locators for select burger menu
    btn_burger = '//button[@id="react-burger-menu-btn"]'
    link_about = '//a[@id="about_sidebar_link"]'

    # Getter
    # Getters for select products.
    def get_select_product_1(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_select_product_2(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.select_product_2)))

    def get_select_product_3(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.select_product_3)))

    def get_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    # Getters for select burger menu.
    def get_btn_burger(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.btn_burger)))

    def get_link_about(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.link_about)))


    # Action
    # Actions for select products.
    def click_select_product_1(self):
        self.get_select_product_1().click()
        print('Click select product 1.')

    def click_select_product_2(self):
        self.get_select_product_2().click()
        print('Click select product 1.')

    def click_select_product_3(self):
        self.get_select_product_3().click()
        print('Click select product 1.')

    def click_cart(self):
        self.get_cart().click()
        print('Click cart.')

    # Actions for select burger menu.
    def click_btn_burger(self):
        self.get_btn_burger().click()
        print('Click burger button.')

    def click_link_about(self):
        self.get_link_about().click()
        print('Click link about.')


    # Methods
    # Method for select product
    def select_products_1(self):
        self.get_current_url()
        self.click_select_product_1()
        self.click_cart()

    def select_products_2(self):
        self.get_current_url()
        self.click_select_product_2()
        self.click_cart()

    def select_products_3(self):
        self.get_current_url()
        self.click_select_product_3()
        self.click_cart()

    # Method fot select menu about
    def select_menu_about(self):
        self.get_current_url()
        self.click_btn_burger()
        self.click_link_about()
        self.assert_url('https://saucelabs.com/')