import logging
import inspect
import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass():

    def initWaiting(self):
        self.wait = WebDriverWait(self.driver, 10)  # creates waiting timeout

    def waiting(self, tuple):
        self.wait.until(expected_conditions.visibility_of_element_located(tuple))
    def getLogger(self):
        loggerName = inspect.stack()[1][3]  # replacing name of the class to the name of the testcase which calls log
        logger = logging.getLogger(loggerName)  # catches test case name

        fileHandler = logging.FileHandler("logfile.log")  # creating object with file name
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")  # setting format of log according to our requirments
        fileHandler.setFormatter(formatter)  # connecting format with fileHolder which is used by logger.addHandler

        logger.addHandler(fileHandler)  # filehandler object, puts logs in file

        logger.setLevel(logging.DEBUG)  # setting logs to be wrotten, all log above will not be put into the file
        return logger