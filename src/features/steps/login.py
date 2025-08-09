from behave import *
from src.page.PageLogin import PageLongin

use_step_matcher('parse')

@given("user accesses the page")
def verify_page(context):
    context.longin = PageLongin(context.driver, context.wait)


























"""

@given('a set of specific users')
def step_impl(context):
    for row in context.table:
        model.add_user(name=row['name'], department=row['department'])"""

