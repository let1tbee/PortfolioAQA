import time
import pytest

from Utilities.BaseClass import  BaseClass
from PageObjects.HomePageRegion import HomePageRegion
from PageObjects.HomePageSearch import HomePageSearch
from PageObjects.BasketPage import Basket


class TestAmazonSmoke(BaseClass):

    @pytest.mark.smoke
    def test_RegionChange(self,regionData):
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
        home_page_region.zipCode().send_keys(regionData[0])
        time.sleep(1)#wait time when some background magic happens
        home_page_region.applyZip().click()
        self.initWaiting()
        self.waitingVisible(home_page_region.regionCheck())#waits until next pop-up appears
        home_page_region.closeButt().click()

    @pytest.mark.smoke
    def test_Search(self,searchData,regionData):
        log = self.getLogger()
        #Main Page serach input
        home_page_search = HomePageSearch(self.driver)
        self.initWaiting()
        self.waitingText(home_page_search.regionCheck(),regionData[1])#waits until region changes
        home_page_search.searchRequest().send_keys(searchData)
        home_page_search.searchButt().click()

        log.info("Items from the search:")
        #Search  Page actions: select 3 Items from the page, grab Summary and price, add to cart
        for item in range(2,4):#should change according to ad presence
            if (item>2):#scroll down window to see 3rd item, potential problem for other resolution screen
                self.driver.execute_script("window.scrollBy(0,500)")
            try:
                textSummary = home_page_search.itemSum(item).text
                textPriceEuro = home_page_search.priceEuro(item).text
                textPriceCents = home_page_search.priceCents(item).text
                home_page_search.itemButt(item-1).click()#if ad is present put "item -1", if not "item"
                log.info(textSummary + " Price:" + textPriceEuro + "." + textPriceCents)
                self.waitingClick(home_page_search.itemButt(item-1))#if ad is present put "item -1", if not "item"
                self.writeData(textSummary, textPriceEuro, textPriceCents)
            except:
                log.info("Item #"+str(item)+" was not active")

        self.driver.execute_script("window.scrollTo(0,0)")
        home_page_search.searchRequest().clear()#clat search for the next iteration


    @pytest.mark.smoke
    def test_Basket(self):
        log = self.getLogger()
        basket_page = Basket(self.driver)
        basket_page.basketGo().click()#go to the basket
        self.takeScreen()
        log.info("Screenshot created")
        basket_page.checkoutButt().click()#proceed to Checkout
        log.info("Checkout page reached")
        time.sleep(5)






