from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_INPUT = (By. ID, 'twotabsearchtextbox')
CLICK_SEARCH_ICON = (By.ID, 'nav-search-submit-button')
SELECT_PRODUCT = (By. CSS_SELECTOR, "a[href*='Wrangler-Authentics-Classic-5-Pocket-Twilight']")
TITLE = (By. ID, 'titleSection')
COLOR_OPTIONS = (By. CSS_SELECTOR, 'ul.a-declarative')
SELECTED_COLORS = (By.ID, 'color_name_0')


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Enter {search_word} into search field')
def enter_text(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)
    sleep(4)


@when('Click on search button')
def click_icon(context):
    context.driver.find_element(*CLICK_SEARCH_ICON).click()
    sleep(1)


@when('Select Product')
def select_product(context):
    context.driver.find_element(*SELECT_PRODUCT).click()


@then('Verify colors are available')
def loop_colors(context):
    expected_colors = ['Black Rinse', 'Blue Lagoon Wash', 'Kings of Leon Md', 'OutsidersWash', 'Vintage Dark']
    color_web_elements = context.driver.find_element(*COLOR_OPTIONS)
    for i in color_web_elements:
        i.click()
        actual_color = context.driver.find_element(*SELECTED_COLORS).text
        print('The actual color is: ', actual_color, '.')
        assert actual_color == expected_colors[color_web_elements.index(i)]
