from selenium.webdriver.common.by import By

from Page_object.CheckoutPage import CheckOutPage
from selenium.webdriver.support.select import Select
import pytest


class Homepage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "//a[contains(@href,'shop')]")
    name = (By.XPATH, "(//input[@name='name'])[1]")
    mail = (By.XPATH, "//input[@name='email']")
    pw = (By.CSS_SELECTOR, "#exampleInputPassword1")
    Gender = (By.ID, "exampleFormControlSelect1")
    employement = (By.CSS_SELECTOR, "#inlineRadio2")
    dob = (By.XPATH, "//input[@name='bday']")
    submit = (By.CSS_SELECTOR, ".btn-success")
    message = (By.CSS_SELECTOR, ".alert-success")

    # def shopitems(self):
    #     return self.driver.find_element(*Homepage.shop)

    # Page object mechanism-Optimization
    def shopitems(self):
        self.driver.find_element(*Homepage.shop).click()
        checkout = CheckOutPage(self.driver)
        return checkout

    def getname(self):
        return self.driver.find_element(*Homepage.name)

    def getmail(self):
        return self.driver.find_element(*Homepage.mail)

    def getpw(self):
        return self.driver.find_element(*Homepage.pw)

    def getgender(self):
        return self.driver.find_element(*Homepage.Gender)

    def getemployment(self):
        return self.driver.find_element(*Homepage.employement)

    def dobfill(self):
        return self.driver.find_element(*Homepage.dob)

    def submit_btn(self):
        return self.driver.find_element(*Homepage.submit)

    def alertmsg(self):
        return self.driver.find_element(*Homepage.message)

