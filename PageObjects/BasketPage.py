from selenium.webdriver.common.by import By


class Basket():
    def __init__(self,driver):
        self.driver = driver

    basket = (By.ID, "nav-cart")
    checkout = (By.NAME, "proceedToRetailCheckout")

    def basketGo(self):
        return self.driver.find_element(*self.basket)

    def checkoutButt(self):
        return self.driver.find_element(*self.checkout)