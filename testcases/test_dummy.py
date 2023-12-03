from selenium import webdriver

from pageobjects.dummy_Ticket_home import dummy_Ticket_home
from utilities.readproperties import ReadConfig


class Test_home:
    newBase = ReadConfig.get_url()

    # baseURL = "https://www.dummyticket.com/"

    def test_home_page(self, setup):
        self.driver = setup
        self.driver.get(self.newBase)
        self.driver.Home = dummy_Ticket_home(self.driver)
        self.driver.Home.click_Home()
        self.driver.Home.select_ticket()
        self.driver.close()
