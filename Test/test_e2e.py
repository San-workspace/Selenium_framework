import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Page_object.CheckoutPage import CheckOutPage
from Page_object.Homepage import Homepage
from Page_object.PurchasePage import PurchasePage
from Test.Test_Home import TestHome
from TestData.HomepageData import HomepageData
from utilities.Baseclass import Baseclass


class Testone(Baseclass):

    def test_e2e(self):

        log = self.getlogger()   #log inserting from baseclass
        homepage = Homepage(self.driver)
        # homepage.shopitems().click()

        checkout = homepage.shopitems()
        log.info("click shop items")
        # self.driver.find_element(By.XPATH, "//a[contains(@href,'shop')]").click()

        # checkout=CheckOutPage(self.driver)
        products = checkout.Cart_titles()
        log.info("Cart_titles are get as products")
        # products = self.driver.find_elements(By.XPATH, "//h4[contains(@class,'title')]")

        # #By using list ,how to get an item from list
        # # product_list=[]
        # for i in products:
        #     # product_list.append(i.text)
        #     # print(product_list)
        #     # if "Blackberry" in product_list:

        for i in products:
            if i.text == "Blackberry":
                checkout.Add_to_cart().click()
                log.info("products is ready to c/o:" +i.text)
                # self.driver.find_element(By.XPATH, "(//button[contains(@class,'info')])[4]").click()
        checkout.Add_to_checkout().click()
        # self.driver.find_element(By.XPATH, "//a[contains(@class,'btn-primary')]").click()
        checkout.Checkout_final().click()
        log.info("final checkout")
        # self.driver.find_element(By.XPATH, "(//button[contains(@class,'btn')])[3]").click()

        purchasepage = PurchasePage(self.driver)

        purchasepage.Send_keys().send_keys("Ind")
        log.info("entering country as IND")
        # self.driver.find_element(By.CSS_SELECTOR, "#country").send_keys("ind")

        self.VerifyLinkPresence("India")

        # wait = WebDriverWait(self.driver, 10)
        # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

        purchasepage.Select_country().click()

        # self.driver.find_element(By.LINK_TEXT, "India").click()

        purchasepage.Checkbox().click()
        # self.driver.find_element(By.CSS_SELECTOR, ".checkbox").click()

        purchasepage.Button_success().click()
        # self.driver.find_element(By.CSS_SELECTOR, ".btn-success").click()

        alert = purchasepage.Alert_success()
        # alert_text = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        alert_text = alert.text
        log.info("The message is:" + alert_text)
        assert "Success" in alert_text


