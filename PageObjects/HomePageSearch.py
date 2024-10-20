from selenium.webdriver.common.by import By


class HomePageSearch:
    def __init__(self, driver):
        self.driver = driver

    region_check = (By.ID,"glow-ingress-line2")
    search_request = (By.ID,"twotabsearchtextbox")
    search_butt = (By.ID,"nav-search-submit-button")
    def regionCheck(self):
        return self.region_check

    def searchRequest(self):
        return self.driver.find_element(*self.search_request)

    def searchButt(self):
        return self.driver.find_element(*self.search_butt)
