from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium_basics.components.base import Base

class LeftFilter(Base):
    LOCATOR = "//*"
    def __init__(self, driver):
        super().__init__(driver)

    def select_brand(self, option, visible=False):
        xpath_locator = '//div[@class="srp-rail__left"]//h3[text()="Brand"]/../../..//ul/li//span[text()="' + option + '"]/../../..//span'
        Base.click(self, (By.XPATH, xpath_locator))
