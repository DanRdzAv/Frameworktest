from context.config import settings
from context.driver import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Basepage:
    def __init__(self):
        self.driver = driver.get_driver()

    def _execute_with_wait(self, condition):
        return WebDriverWait(self.driver, settings.driver_timeout).until(condition)

    def wait(self,time):
        self.driver.implicitly_wait(time)
    

    def element_exists(self, locator):
        try:
            self._execute_with_wait(
                ec.presence_of_element_located(
                    (locator.l_type, locator.selector))
            )
            return True
        except TimeoutException:
            return False

    def get_element(self, locator):
        if not self.element_exists(locator):
            raise NoSuchElementException("Could not find {locator.selector}")

        return self.driver.find_element(locator.l_type, locator.selector)
