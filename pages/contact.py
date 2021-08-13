"""
This module contains RodneyCodesContactPage,
the page object for Rodney.Codes Contact page.
"""


# ---------------------------------------------------------------
# Imports
# ---------------------------------------------------------------

from selenium.webdriver.common.by import By


# ---------------------------------------------------------------
# Classes
# ---------------------------------------------------------------

class RodneyCodesContact:

    # URL
    url = "http://rodney.codes/contact.php"

    # Locators
    NAME_INPUT = (By.ID, 'name')
    EMAIL_INPUT = (By.ID, 'email')
    PHONE_INPUT = (By.ID, 'phone')
    MESSAGE_INPUT = (By.NAME, 'message')

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    def load(self):
        self.browser.get(self.url)

    def contact(self, name, email, phone, message):

        # name
        name_input = self.browser.find_element(*self.NAME_INPUT)
        name_input.send_keys(name)

        # email
        email_input = self.browser.find_element(*self.EMAIL_INPUT)
        email_input.send_keys(email)

        # phone
        phone_input = self.browser.find_element(*self.PHONE_INPUT)
        phone_input.send_keys(phone)

        # message
        message_input = self.browser.find_element(*self.MESSAGE_INPUT)
        message_input.send_keys(message)
