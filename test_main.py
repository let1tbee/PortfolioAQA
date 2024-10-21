import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Utilities.BaseClass import  BaseClass
from PageObjects.HomePageRegion import HomePageRegion
from PageObjects.HomePageSearch import HomePageSearch

region_zip = "64572"
region = "Büttelborn 64572‌"
search_input = "RTX 3060"
class TestAmazonSmoke(BaseClass):

    @pytest.mark.smoke
    def test_RegionChange(self):
        log = self.getLogger()
        home_page_region = HomePageRegion(self.driver)

        #If cookies acceptation requested - press accept and provide logs
        try:
            home_page_region.cookiesAccept().click()
            log.info("Cookies acceptation was shown and accepted")
        except:
            log.info("Cookies acceptation wasn't shown")


        #Changing region to Germany on Main page
        home_page_region.regionButt().click()
        home_page_region.zipCode().send_keys(region_zip)
        time.sleep(1)#wait time when some background magic happens
        home_page_region.applyZip().click()
        self.initWaiting()
        self.waitingVisible(home_page_region.regionCheck())#waits until next pop-up appears
        home_page_region.closeButt().click()

    @pytest.mark.smoke
    def test_Search(self):
        log = self.getLogger()
        #Main Page serach input
        home_page_search = HomePageSearch(self.driver)
        self.initWaiting()
        self.waitingText(home_page_search.regionCheck(),region)#waits until region changes
        home_page_search.searchRequest().send_keys(search_input)
        home_page_search.searchButt().click()

        log.info("Items from the search:")
        #Search  Page actions: select 3 Items from the page, grab Summary and price, add to cart
        for item in range(2,5):#should change according to ad presence
            if (item>2):#scroll down window to see 3rd item, potential problem for other resolution screen
                self.driver.execute_script("window.scrollBy(0,500)")
            try:
                textSummary = home_page_search.itemSum(item).text
                textPriceEuro = home_page_search.priceEuro(item).text
                textPriceCents = home_page_search.priceCents(item).text
                home_page_search.itemButt(item-1).click()#if ad is present put "item -1", if not "item"
                log.info(textSummary + " Price:" + textPriceEuro + "." + textPriceCents)
                self.waitingClick(home_page_search.itemButt(item-1))#if ad is present put "item -1", if not "item"
            except:
                log.info("Item #"+str(item)+" was not active")



    @pytest.mark.smoke
    def test_Basket(self):
        log = self.getLogger()
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.find_element(By.ID, "nav-cart").click()#go to the basketa[href='https://www.amazon.de/-/en/gp/cart/view.html?ref_=nav_cart
        #screenshoot placeholder
        self.driver.find_element(By.NAME, "proceedToRetailCheckout").click()#proceed to Checkout
    time.sleep(5)






