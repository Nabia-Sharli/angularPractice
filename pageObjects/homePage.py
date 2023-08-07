from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.CheckOutPage import CheckOutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    name = (By.NAME, "name")
    email =(By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    status = (By.ID, "inlineRadio1")
    dob = (By.NAME, "bday")
    submitButton = (By.XPATH, "//input[@value='Submit']")
    successMessage = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
    shop = (By.LINK_TEXT, "Shop")

    def userName(self):
        return self.driver.find_element(*HomePage.name)

    def userEmail(self):
        return self.driver.find_element(*HomePage.email)

    def userPassword(self):
        return self.driver.find_element(*HomePage.password)

    def checkboxClick(self):
        return self.driver.find_element(*HomePage.checkbox)

    def selectGender(self):
        return Select(self.driver.find_element(*HomePage.gender))

    def selectStatus(self):
        return self.driver.find_element(*HomePage.status)

    def DateOfBirth(self):
        return self.driver.find_element(*HomePage.dob)

    def submitButtonClick(self):
        return self.driver.find_element(*HomePage.submitButton)

    def shopClick(self):
        self.driver.find_element(*HomePage.shop).click()
        check_out_page = CheckOutPage(self.driver)
        return check_out_page


