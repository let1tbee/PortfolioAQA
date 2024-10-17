import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.BaseClass import  BaseClass
from PageObjects.HomePage import HomePage

class TestAmazonSmoke(BaseClass):


    def test_RegionChange(self):
        log = self.getLogger()
        home_page = HomePage(self.driver)

        #If cookies acceptation requested - press accept and provide logs
        try:
            home_page.cookiesAccept().click()
            log.info("Cookies acceptation was shown and accepted")
        except:
            log.info("Cookies acceptation wasn't shown")


        #Changing region to Germany on Main page
        home_page.regionButt().click()
        home_page.zipCode().send_keys("64572")
        time.sleep(1)#wait time when some background magic happens
        home_page.applyZip().click()
        self.initWaiting()
        self.waiting(home_page.regionCheck())#waits until next pop-up appears
        home_page.closeButt().click()

    def test_Search(self):
        log = self.getLogger()
        #Main Page serach input
        wait = WebDriverWait(self.driver,20)
        wait.until(expected_conditions.text_to_be_present_in_element((By.ID,"glow-ingress-line2"),"Büttelborn 64572‌"))#waits until region changes
        self.driver.find_element(By.ID,"twotabsearchtextbox").send_keys("RTX 3060")
        self.driver.find_element(By.ID,"nav-search-submit-button").click()

        log.info("Items from the search:")
        #Search  Page actions: select 3 Items from the page, grab Summary and price, add to cart
        for item in range(1,4):#should change according to ad presence
            locatorSummary = "div[data-cel-widget='search_result_"+str(item)+"'] a span[class='a-size-medium a-color-base a-text-normal']" #creates locator for first 3 items in the list
            locatorPriceEuro = "div[data-cel-widget='search_result_"+str(item)+"'] a span[class='a-price-whole']"
            locatorPriceCents = "div[data-cel-widget='search_result_"+str(item)+"'] a span[class='a-price-fraction']"
            if (item>2):#scroll down window to see 3rd item, potential problem for other resolution screen
                self.driver.execute_script("window.scrollBy(0,500)")
            try:
                textSummary = self.driver.find_element(By.CSS_SELECTOR, locatorSummary).text
                textPriceEuro = self.driver.find_element(By.CSS_SELECTOR, locatorPriceEuro).text
                textPriceCents = self.driver.find_element(By.CSS_SELECTOR, locatorPriceCents).text
                locatorButton ="button[id='a-autoid-"+str(item)+"-announce']"
                self.driver.find_element(By.CSS_SELECTOR, locatorButton).click()  # adding item to the cart
                log.info(textSummary + " Price:" + textPriceEuro + "." + textPriceCents)
                wait = WebDriverWait(self.driver, 20)
                wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"div[data-cel-widget='search_result_" + str(item) + "'] strong[class='a-size-small']")))  # waits for item to be added to the cart
            except:
                log.info("Item #"+str(item)+"Was not active")



        self.driver.find_element(By.CSS_SELECTOR, "a[class = 'a-button-text']").click()#go to the basket #TO REDO

    def test_Basket(self):
        log = self.getLogger()
        #screenshoot placeholder
        self.driver.find_element(By.NAME, "proceedToRetailCheckout").click()#proceed to Checkout
    time.sleep(5)






