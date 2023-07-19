import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from Page_object.Homepage import Homepage
from TestData.HomepageData import HomepageData


@pytest.mark.usefixtures("setup")
class Baseclass:
    #logging handling
    def getlogger(self):
        loggerName = inspect.stack()[1][3]  # to get exact testcase name in log
        logger = logging.getLogger(loggerName)

        filehandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)

        logger.setLevel(logging.DEBUG)  # print the log in all the level
        return logger
    #verify the text link by explicit wait to handle dynamic dropdown
    def VerifyLinkPresence(self,text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))
    #static dropdown handlig
    def SelectOptionBytext(self,locator,text):
        sel = Select(locator)
        sel.select_by_visible_text(text)
    pass
