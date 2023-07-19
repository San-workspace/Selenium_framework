import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Page_object.Homepage import Homepage
from TestData.HomepageData import HomepageData
from utilities.Baseclass import Baseclass


class TestHome(Baseclass):

    def test_home(self, getdata):
        log = self.getlogger()
        homepage = Homepage(self.driver)
        log.info("name is:" +getdata["name"])
        homepage.getname().send_keys(getdata["name"])
        homepage.getmail().send_keys(getdata["email"])
        log.info("mail :"+getdata["email"])
        homepage.getpw().send_keys("8870935744")
        self.SelectOptionBytext(homepage.getgender(), "Male")
        homepage.getemployment().click()
        homepage.dobfill().send_keys(getdata["dob"])
        homepage.submit_btn().click()

        alert_message = homepage.alertmsg().text
        assert "Success!" in alert_message
        print(alert_message, "- Test PASS")
        self.driver.refresh()

    #@pytest.fixture(params=HomepageData.Test_Home_Data)  # toget the data from hardcore varaiable
    @pytest.fixture(params=HomepageData.gettestdata("test2"))  #to get the data test2 data from xl
    def getdata(self, request):
        return request.param