from selenium.webdriver.common.by import By


class Locator:
    def __init__(self, l_type, selector):
        self.l_type = l_type
        self.selector = selector

    def parameterize(self, *args):
        self.selector = self.selector.format(*args)


class PracticepageLocator:
    SuggestionClassExampleTxtBox = Locator(By.XPATH, "//input[@id='autocomplete']")
    countryresult = Locator(By.XPATH, "//div[@class='ui-menu-item-wrapper'][text()='{}']")
    DropdownExampleSelection = Locator(By.XPATH, "//select[@name='dropdown-class-example']")
    DropdownOption = Locator(By.XPATH, "//option[@value='{}']")
    optionWindown = Locator(By.XPATH,"//button[@id='openwindow']")
    moneybacktext = Locator(By.XPATH,"//*[text()='30 day Money Back Guarantee']")
    openTab = Locator(By.XPATH,"//a[@id='opentab']")
    alertTxt = Locator(By.XPATH,"//input[@id='name']")
    alertBtn = Locator(By.XPATH,"//input[@id='alertbtn']")
    alertConfirmtxt = Locator(By.XPATH,"//input[@id='confirmbtn']")