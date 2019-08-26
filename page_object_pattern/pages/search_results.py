from selenium.webdriver.common.by import By
from page_object_pattern.locators.locators import SearchResultsLocators
import logging
import allure
from allure_commons.types import AttachmentType

class SearchResultsPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.hotel_names_xpath = SearchResultsLocators.hotel_names_xpath
        self.hotel_prices_xpath = SearchResultsLocators.hotel_prices_xpath

    @allure.step("Checking results")
    def get_hotel_names(self):
        hotels = self.driver.find_elements(By.XPATH, SearchResultsLocators.hotel_names_xpath)
        names = [hotel.get_attribute("textContent") for hotel in hotels]
        allure.attach(self.driver.get_screenshot_as_png(), name="Results", attachment_type=AttachmentType.PNG)
        self.logger.info("Availabe hotels are: ")
        for name in names:
            self.logger.info(name)
        return names

    def get_hotel_prices(self):
        prices = self.driver.find_elements(By.XPATH, SearchResultsLocators.hotel_prices_xpath)
        hotel_prices = [price.get_attribute("textContent") for price in prices]
        self.logger.info("Hotel prices are: ")
        for price in hotel_prices:
            self.logger.info(price)
        return hotel_prices