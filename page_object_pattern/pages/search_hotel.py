from selenium.webdriver.common.by import By
from page_object_pattern.locators.locators import SearchHotelLocators
import logging

class SearchHotelPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.search_hotel_span_xpath = SearchHotelLocators.search_hotel_span_xpath
        self.search_hotel_input_xpath = SearchHotelLocators.search_hotel_input_xpath
        self.location_match_xpath = SearchHotelLocators.location_match_xpath
        self.check_in_input_name = SearchHotelLocators.check_in_input_name
        self.check_out_input_name = SearchHotelLocators.check_out_input_name
        self.travellers_input_id =  SearchHotelLocators.travellers_input_id
        self.adults_input_id =  SearchHotelLocators.adults_input_id
        self.child_input_id = SearchHotelLocators.child_input_id
        self.search_button_xpath = SearchHotelLocators.search_button_xpath

    def set_city(self, city):
        self.logger.info("Setting city {}.".format(city))
        self.driver.find_element(By.XPATH, self.search_hotel_span_xpath).click()
        self.driver.find_element(By.XPATH, self.search_hotel_input_xpath).send_keys(city)
        self.driver.find_element(By.XPATH, self.location_match_xpath).click()


    def set_date_range(self, check_in, check_out):
        self.logger.info("Setting check in: {checkin} and check out: {checkout} dates".format(checkin=check_in, checkout=check_out))
        self.driver.find_element(By.NAME, self.check_in_input_name).send_keys(check_in)
        self.driver.find_element(By.NAME, self.check_out_input_name).send_keys(check_out)

    def set_travellers(self, adults, child):
        self.logger.info("Setting travellers adults: {adults} and child: {kids}".format(adults=adults, kids=child))
        self.driver.find_element(By.ID, self.travellers_input_id).click()
        self.driver.find_element(By.ID, self.adults_input_id).clear()
        self.driver.find_element(By.ID, self.adults_input_id).send_keys(adults)
        self.driver.find_element(By.ID, self.child_input_id).clear()
        self.driver.find_element(By.ID, self.child_input_id).send_keys(child)

    def perform_search(self):
        self.logger.info("Performing search")
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()