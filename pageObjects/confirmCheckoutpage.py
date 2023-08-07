from selenium.webdriver.common.by import By

from pageObjects.purchasePage import PurchasePage


class ConfirmCheckOut:
    def __init__(self, driver):
        self.driver = driver

    confirm_button = (By.CSS_SELECTOR, "button[class*='btn-success']")

    def confirmButton(self):
        self.driver.find_element(*ConfirmCheckOut.confirm_button).click()
        purchase = PurchasePage(self.driver)
        return purchase


