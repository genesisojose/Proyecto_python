

from behave import *
from src.page.PageLogin import PageLogin

use_step_matcher('parse')

@given("the user navigates to the login page")
def step_access_page(context):
    """
    Initializes the PageLogin object and stores it in the context.
    """
    context.login_page = PageLogin(context.driver, context.wait)
























"""

@given('a set of specific users')
def step_impl(context):
    for row in context.table:
        model.add_user(name=row['name'], department=row['department'])"""

