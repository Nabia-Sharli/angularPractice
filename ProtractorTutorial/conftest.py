import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setup(request):
    service_obj = Service("C:/Users/DELL/Downloads/chromedriver_win32/chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj);
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.close()
