from selenium.webdriver.common.by import By
from playwright.sync_api import Page, expect, TimeoutError as PlaywrightTimeoutError

class LoginPage:
    def __init__(self, page: Page):
        # Initialize the page instance and define locators for login elements
        self.page = page
        self.username_field = page.get_by_placeholder("Enter your mail")        # Username input field
        self.password_field = page.get_by_placeholder("Enter your password ")   # Password input field
        self.submit_button = page.locator("//button[@type='submit']")           # Submit/login button
        self.dashboard_element = page.locator("#profile-click-icon")            # Element that appears after successful login
        self.error_message = page.get_by_text("*Incorrect mail or password!")   # Error message on invalid login

    def goto(self):        
        self.page.goto("https://v2.zenclass.in/login")  # Navigate to the login page URL

    def login(self, username: str, password: str):
        """
        Perform login with given username and password.

        Raises:
            Exception: If login fields are not visible or interactable.
        """
        try:
            expect(self.username_field).to_be_visible()         # Wait until username field is visible
            expect(self.password_field).to_be_visible()         # Wait until password field is visible
            self.username_field.fill(username)                  # Enter the username
            self.password_field.fill(password)                  # Enter the password
            self.submit_button.click()                          # Click the login/submit button
        except PlaywrightTimeoutError:
            raise Exception("Login fields not found or not interactable")

    def validate_fields_present(self):
        """
        Validate that both username and password fields are visible.

        Returns:
            bool: True if both fields are visible, else False
        """
        return self.username_field.is_visible() and self.password_field.is_visible()

    def is_submit_clickable(self):
        """
        Check if the submit button is enabled/clickable.

        Returns:
            bool: True if button is enabled, else False
        """
        return self.submit_button.is_enabled()

    def get_error_message(self):
        """
        Fetch the error message text displayed on invalid login.

        Returns:
            str: The error message text
        """
        return self.error_message.inner_text()
    
    @staticmethod
    def safe_click(locator, timeout=5000):
        """
        Click an element safely by waiting until it is visible.

        Args:
            locator: The Playwright locator to be clicked.
            timeout (int): Maximum time to wait in milliseconds.

        Raises:
            Exception: If the element is not clickable or not visible in the given time.
        """
        try:
            locator.wait_for(state="visible", timeout=timeout)      # Wait for the element to become visible
            locator.click()                                         # Perform the click action
        except PlaywrightTimeoutError:
            raise Exception(f"Element {locator} not clickable or not visible")

