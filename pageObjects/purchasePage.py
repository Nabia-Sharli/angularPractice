from selenium.webdriver.common.by import By


class PurchasePage:
    def __init__(self, driver):
        self.driver = driver
    country_input = (By.ID, "country")
    countries = (By.XPATH, "//div/ul/li/a")
    checkbox = (By.CSS_SELECTOR, "div[class*='checkbox-primary']")
    purchaseButton = (By.XPATH, "//input[@value='Purchase']")
    alert = (By.CSS_SELECTOR, "div[class*='alert-success']")

    def countryInput(self):
        return self.driver.find_element(*PurchasePage.country_input)

    def selectCountries(self):
        countries = self.driver.find_elements(*PurchasePage.countries)
        return countries

    def clickCheckbox(self):
        return self.driver.find_element(*PurchasePage.checkbox)

    def clickPurchaseButton(self):
        return self.driver.find_element(*PurchasePage.purchaseButton)

    def alertMessage(self):
        alert_message = self.driver.find_element(*PurchasePage.alert)
        return alert_message




