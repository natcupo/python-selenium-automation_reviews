from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):
    SEARCH_INPUT = (By.NAME, 'q')
    SEARCH_SUBMIT = (By.NAME, 'btnK')
    ORDERS_LINK = (By.ID, 'nav-orders')
    CART = (By.ID, 'nav-cart-count-container')
    ITEM = (By. CSS_SELECTOR, 'div.FourSalePromos__SectionHeading')

    def search_for_keyword(self, text):
        self.input_text(text, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_SUBMIT)

    def select_orders_link(self):
        self.click(*self.ORDERS_LINK)

    def select_cart_icon(self):
        self.click(*self.CART)

    def item_selection(self):
        self.click(*self.ITEM)


