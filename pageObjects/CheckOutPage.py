from selenium.webdriver.common.by import By

from pageObjects.confirmCheckoutpage import ConfirmCheckOut


# self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    cards = (By.XPATH, "//button[text()='Add ']")
    checkout=(By.CSS_SELECTOR, "a[class*='btn-primary']")

    def cardsClick(self):
        totalCards = self.driver.find_elements(*CheckOutPage.cards)
        for card in totalCards:
            card.click()
        self.driver.find_element(*CheckOutPage.checkout).click()
        confirm_check_out = ConfirmCheckOut(self.driver)
        return confirm_check_out

