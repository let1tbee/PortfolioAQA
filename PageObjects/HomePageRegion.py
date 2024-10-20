from selenium.webdriver.common.by import By


class HomePageRegion:
    def __init__(self, driver):
        self.driver = driver

    cookies = (By.ID, "sp-cc-accept")
    region = (By.ID,"nav-global-location-popover-link")
    zip = (By.ID,"GLUXZipUpdateInput")
    apply = (By.XPATH,"//input[@aria-labelledby='GLUXZipUpdate-announce']")
    region_check = (By.ID,"GLUXHiddenSuccessSubTextAisEgress")
    close_butt = (By.XPATH,"//button[@aria-label='Close']")
    def cookiesAccept(self):
        return self.driver.find_element(*self.cookies)

    def regionButt(self):
        return self.driver.find_element(*self.region)

    def zipCode(self):
        return  self.driver.find_element(*self.zip)

    def applyZip(self):
        return self.driver.find_element(*self.apply)

    def regionCheck(self):
        return self.region_check

    def closeButt(self):
        return self.driver.find_element(*self.close_butt)