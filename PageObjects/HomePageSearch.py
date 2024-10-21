from selenium.webdriver.common.by import By


class HomePageSearch:
    def __init__(self, driver):
        self.driver = driver

    region_check = (By.ID,"glow-ingress-line2")
    search_request = (By.ID,"twotabsearchtextbox")
    search_butt = (By.ID,"nav-search-submit-button")
    item_add_selector = (By.CSS_SELECTOR,)
    item_sum_1 = "div[data-cel-widget='search_result_"
    item_sum_2 = "'] a span[class='a-size-medium a-color-base a-text-normal']"
    item_price_euro_1 = "div[data-cel-widget='search_result_"
    item_price_euro_2 ="'] a span[class='a-price-whole']"
    item_price_cents_1 ="div[data-cel-widget='search_result_"
    item_price_cents_2 ="'] a span[class='a-price-fraction']"
    item_butt_1 ="button[id='a-autoid-"
    item_butt_2 ="-announce']"

    def regionCheck(self):
        return self.region_check

    def searchRequest(self):
        return self.driver.find_element(*self.search_request)

    def searchButt(self):
        return self.driver.find_element(*self.search_butt)

    def itemSum(self,item):
        return self.driver.find_element(*self.item_add_selector, self.item_sum_1 +str(item) + self.item_sum_2)
    def priceEuro(self,item):
        return self.driver.find_element(*self.item_add_selector, self.item_price_euro_1 +str(item) + self.item_price_euro_2)
    def priceCents(self,item):
        return self.driver.find_element(*self.item_add_selector, self.item_price_cents_1 +str(item) + self.item_price_cents_2)
    def itemButt(self,item):
        return self.driver.find_element(*self.item_add_selector, self.item_butt_1 +str(item) + self.item_butt_2)

