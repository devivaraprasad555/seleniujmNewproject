from selenium.webdriver.common.by import By


class dummy_Ticket_home:
    click_Home_to_select = '//a[text()="Home"]'
    buy_ticket = '//a[@class="ffb-block-button-3-0 ffb-btn ffb-btn-v1 ffb-btn-link  btn-base-brd-slide btn-slide radius-3 btn-base-md    btn-w-full fg-text-dark ffb-button1-4-1"]/span'

    def __init__(self, driver):
        self.driver = driver

    def click_Home(self):
        self.driver.find_element(By.XPATH, self.click_Home_to_select).click()

    def select_ticket(self):
        self.driver.find_element(By.XPATH, self.buy_ticket).click()

