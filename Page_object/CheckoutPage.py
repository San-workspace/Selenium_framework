from selenium.webdriver.common.by import By


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    titles = (By.XPATH, "//h4[contains(@class,'title')]")
    cart = (By.XPATH, "(//button[contains(@class,'info')])[4]")
    checkout = (By.XPATH, "//a[contains(@class,'btn-primary')]")
    totalcheckout= (By.XPATH, "(//button[contains(@class,'btn')])[3]")

    def Cart_titles(self):
        return self.driver.find_elements(*CheckOutPage.titles)

    def Add_to_cart(self):
        return self.driver.find_element(*CheckOutPage.cart)

    def Add_to_checkout(self):
        return self.driver.find_element(*CheckOutPage.checkout)

    def Checkout_final(self):
        return self.driver.find_element(*CheckOutPage.totalcheckout)
