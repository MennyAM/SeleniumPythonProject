from selenium.webdriver.common.by import By
from POMDemo.Locators.locators import Locators


class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.welcome_link_xpath = Locators.welcome_link_xpath
        self.logout_link_linkText = Locators.logout_link_linkText

    def click_welcome(self):
        self.driver.find_element(By.XPATH, Locators.welcome_link_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT, Locators.logout_link_linkText).click()
