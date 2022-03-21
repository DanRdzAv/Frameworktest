from multiprocessing.connection import wait
from context.driver import driver
from pages.locators import PracticepageLocator
from pages.Basepage import Basepage
from selenium.webdriver.common.keys import Keys
import time


class PracticePage(Basepage):
    instance = None


    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = PracticePage()
        return cls.instance

    def __init__(self):
        super().__init__()

    def search(self, search):
        element = super().get_element(PracticepageLocator.SuggestionClassExampleTxtBox)
        element.clear()
        element.send_keys(search)
        self.wait(10)

    def clickResult(self, country):
        PracticepageLocator.countryresult.parameterize(country)
        element = super().get_element(PracticepageLocator.countryresult)
        element.click()


    def verifyResults(self, country):
        PracticepageLocator.countryresult.parameterize(country)
        assert super().element_exists(PracticepageLocator.countryresult) is True, (
            "Expected search result was not found"
        )

    def selectOption(self, option):
        PracticepageLocator.DropdownOption.parameterize(option)
        element2= super().get_element(PracticepageLocator.DropdownExampleSelection)
        element = super().get_element(PracticepageLocator.DropdownOption)
        element2.click()
        time.sleep(2)
        element.click()
        time.sleep(2)

    def verifyResultsOption(self, country):
        PracticepageLocator.DropdownOption.parameterize(country)
        assert super().element_exists(PracticepageLocator.DropdownOption) is True, (
            "Expected search result was not found"
        ) 
        
    def openWindow(self):
        window_before = self.driver.window_handles[0]
        element = super().get_element(PracticepageLocator.optionWindown)
        element.click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)

    def verifyResultsWindow(self):
         assert super().element_exists(PracticepageLocator.moneybacktext) is True, (
            "Expected search result was not found"
        ) 

    def openTab(self):
        window_before = self.driver.window_handles[0]
        element = super().get_element(PracticepageLocator.openTab)
        element.click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        time.sleep(7)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.driver.save_screenshot('Verifynewtab.png')

    def sendAlertName(self, alert):
        element = super().get_element(PracticepageLocator.alertTxt)
        element.clear()
        element.send_keys(alert)
        time.sleep(2)

    def clickAlert(self):
        element = super().get_element(PracticepageLocator.alertBtn)
        element.click()
        self.driver.switch_to.alert.accept()

    def clickConfirm(self):
        element = super().get_element(PracticepageLocator.alertConfirmtxt)
        element.click()
        self.driver.switch_to.alert.accept()    


PracticePage = PracticePage.get_instance()
