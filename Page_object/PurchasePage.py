from selenium.webdriver.common.by import By


class PurchasePage:
    def __init__(self, driver):
        self.driver = driver

    sendkeys = (By.CSS_SELECTOR, "#country")
    country = (By.LINK_TEXT, "India")
    checkbox=(By.CSS_SELECTOR, ".checkbox")
    succbtn=(By.CSS_SELECTOR, ".btn-success")
    alert=(By.CLASS_NAME, "alert-success")

    def Send_keys(self):
        return self.driver.find_element(*PurchasePage.sendkeys)

    def Select_country(self):
        return self.driver.find_element(*PurchasePage.country)

    def Checkbox(self):
        return self.driver.find_element(*PurchasePage.checkbox)

    def Button_success(self):
        return self.driver.find_element(*PurchasePage.succbtn)

    def Alert_success(self):
        return self.driver.find_element(*PurchasePage.alert)


