from pickle import TRUE
from behave import given, when, then
from pages.PracticePage import PracticePage



@when(u'I put for "{search}"')
def search(context, search):
    PracticePage.search(search)


@when(u'I select "{country}"')
def results(context, country):
    PracticePage.clickResult(country)

@then(u'I view "{country}"')
def results(context, country):
    PracticePage.verifyResults(country)

@when(u'I select in the dropdown "{option}"')
def results(context, option):
    PracticePage.selectOption(option)    


@when(u'I click on Switch Window Example')
def results(context):
    PracticePage.openWindow()       

@then(u'I see the the expected message')
def results(context):
    PracticePage.verifyResultsWindow()

@when(u'I click on open tab')
def results(context):
    PracticePage.openTab()   

@then(u'I verify the bottom')
def results(context):
    return TRUE
    

@then(u'I see the "{option}"')
def results(context, option):
    PracticePage.verifyResultsOption(option)

@when(u'I send the name of alert "{alert}"')
def search(context, alert):
    PracticePage.sendAlertName(alert)

@then(u'I click on alert')
def search(context):
    PracticePage.clickAlert()   

@then(u'I click on confirm')
def search(context):
    PracticePage.clickConfirm()   