from behave import given, when, then
from context.config import settings
from context.driver import driver


@given(u'I load the page')
def load_website(context):
    driver.navigate(settings.url)
