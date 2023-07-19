from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

import pytest

driver = None



# To select browser option in run time
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    global driver  # to ensure global driver
    if browser_name == "chrome":
        chrome_service = Service("C:/Users/DEEPTHA/Desktop/Sankar/Selenium-Python/chromedriver/chromedriver.exe")
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    elif browser_name == "Firefox":
        firefox_service = Service(
            "C:/Users/DEEPTHA/Desktop/Sankar/Selenium-Python/geckodriver-v0.32.0-win64/geckodriver.exe")
        driver = webdriver.Firefox(service=firefox_service)

    elif browser_name == "IE":
        edge_service = Service("C:/Users/DEEPTHA/Desktop/Sankar/Selenium-Python/edgedriver_win64/msedgedriver.exe")
        driver = webdriver.Edge(service=edge_service)

    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


    # to capture the screnshot if test fail ,in html report
    @pytest.mark.hookwrapper
    def pytest_runtest_makereport(item):
        """
            Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
            :param item:
            """
        pytest_html = item.config.pluginmanager.getplugin('html')
        outcome = yield
        report = outcome.get_result()
        extra = getattr(report, 'extra', [])
        print(driver)

        if report.when == 'call' or report.when == "setup":
            xfail = hasattr(report, 'wasxfail')
            if (report.skipped and xfail) or (report.failed and not xfail):
                file_name = report.nodeid.replace("::", "_") + ".png"
                _capture_screenshot(file_name)
                if file_name:
                    html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                           'onclick="window.open(this.src)" align="right"/></div>' % file_name
                    extra.append(pytest_html.extras.html(html))
            report.extra = extra


    def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)