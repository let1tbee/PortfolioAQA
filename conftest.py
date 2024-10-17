import pytest
from selenium import webdriver

driver = None

def pytest_addoption(parser): #deafult pytest method to parse commands from command line calle commandline hook
    parser.addoption(
       "--n", action="store", default = "c" #n -  browser name, c - chrome, f - firefox, e - explore
    )
@pytest.fixture(scope = "class") #scope class to be executed only once before executionf tests withim the class
def setup(request):
    global driver
    browser_name = request.config.getoption("n")
    if browser_name == "c":
        driver = webdriver.Chrome()
    #elif browser_name == "f":
    #invoke firefox code *** TO BE IMPLEMENTEED ***
    elif browser_name == "e":
        driver = webdriver.Edge()

    driver.get("https://www.amazon.de/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver #using request to return driver object to class because "return" cannot be used with yield

    yield #actions that will be performed after tests
    driver.close()
'''
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra'''


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)