import pytest
import allure
from page_object_pattern.pages.search_hotel import SearchHotelPage
from page_object_pattern.pages.search_results import SearchResultsPage
from page_object_pattern.utils.read_excel import ExcelReader




@pytest.mark.usefixtures("setup")
class TestHotelSearch:

    @allure.title("Search hotel test")
    @allure.description("Setting city, date range, and number of travellers and compare searching hotel results with expected")
    @pytest.mark.parametrize("data", ExcelReader.get_data())
    def test_hotel_search(self):
        self.driver.get("http://www.kurs-selenium.pl/demo/")
        search_hotel_page = SearchHotelPage(self.driver)
        search_hotel_page.set_city(data.city)
        search_hotel_page.set_date_range(data.check_in, data.check_out)
        search_hotel_page.set_travellers(data.adults, data.child)
        search_hotel_page.perform_search()
        search_results = SearchResultsPage(self.driver)
        hotel_names = search_results.get_hotel_names()
        price_values = search_results.get_hotel_prices()

        assert hotel_names[0] == "Jumeirah Beach Hotel"
        assert hotel_names[1] == "Oasis Beach Tower"
        assert hotel_names[2] == "Rose Rayhaan Rotana"
        assert hotel_names[3] == "Hyatt Regency Perth"

        assert price_values[0] == '$22'
        assert price_values[1] == '$50'
        assert price_values[2] == '$80'
        assert price_values[3] == '$150'



