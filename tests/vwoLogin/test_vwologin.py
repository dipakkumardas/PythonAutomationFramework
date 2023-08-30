import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging
from src.pageObjects.loginPage import LoginPage


class TestVWOLogin:

    @pytest.fixture()
    def driver(self):
        driver = webdriver.Chrome()
        driver.get("https://app.vwo.com")
        #driver.maximize_window()
        #time.sleep(5)
        yield driver
        driver.quit()

    @allure.feature("VWO Login")
    @allure.id(1)
    @allure.story("Positive Test case in VWO Login")
    @allure.description("Verify that the valid email , pass we are able to login")
    @pytest.mark.positive
    def test_vwologin(self, driver):
        # SeleniumAPI - Creste session
        loginPage = LoginPage(driver)
        loginPage.login_to_vwo("contact+augg@thetestingacademy.com", "Wingify@123")
        time.sleep(5)
        assert "Dashboard" in driver.title
        time.sleep(2)
