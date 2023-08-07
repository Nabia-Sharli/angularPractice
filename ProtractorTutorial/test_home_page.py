import pytest

from pageObjects.homePage import HomePage
from utilities.baseClass import BaseClass
from utilities.homePageData import HomePageData


class TestUserRegistration(BaseClass):
    def test_home_page(self, registration_data):
        log = self.loggin()
        homePage = HomePage(self.driver)
        homePage.userName().send_keys(registration_data["name"])
        log.info(registration_data["name"])
        homePage.userEmail().send_keys(registration_data["email"])
        log.info(registration_data["email"])
        homePage.userPassword().send_keys(registration_data["password"])
        log.info(registration_data["password"])
        homePage.checkboxClick().click()
        homePage.selectGender().select_by_visible_text(registration_data["gender"])
        log.info(registration_data["gender"])
        homePage.selectStatus().click()
        homePage.DateOfBirth().send_keys(registration_data["dob"])
        log.info(registration_data["dob"])
        homePage.submitButtonClick().click()
        check_out_page = homePage.shopClick()
        confirm_check_out = check_out_page.cardsClick()
        purchase = confirm_check_out.confirmButton()
        purchase.countryInput().send_keys("Ban")
        # time.sleep(10)
        self.verifySearchItem("Bangladesh")
        countries = purchase.selectCountries()
        for country in countries:
            if country.text == "Bangladesh":
                country.click()
                break

        purchase.clickCheckbox().click()
        purchase.clickPurchaseButton().click()
        alert_message = purchase.alertMessage().text
        assert "Success!" in alert_message

    @pytest.fixture(params=HomePageData.data)
    def registration_data(self, request):
        return request.param









