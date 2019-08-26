from selenium.webdriver.common.by import By
from page_object_pattern.locators.locators import SearchHotelLocators

class SearchHotelPage:
    def __init__(self, driver):
        self.driver = driver
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
        self.driver.find_element(By.XPATH, self.search_hotel_span_xpath).click()
        self.driver.find_element(By.XPATH, self.search_hotel_input_xpath).send_keys(city)
        self.driver.find_element(By.XPATH, self.location_match_xpath).click()


    def set_date_range(self, check_in, check_out):
        self.driver.find_element(By.NAME, self.check_in_input_name).send_keys(check_in)
        self.driver.find_element(By.NAME, self.check_out_input_name).send_keys(check_out)

    def set_travellers(self, adults, child):
        self.driver.find_element(By.ID, self.travellers_input_id).click()
        self.driver.find_element(By.ID, self.adults_input_id).clear()
        self.driver.find_element(By.ID, self.adults_input_id).send_keys(adults)
        self.driver.find_element(By.ID, self.child_input_id).clear()
        self.driver.find_element(By.ID, self.child_input_id).send_keys(child)

    def perform_search(self):
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()