from selenium.webdriver.common.by import By
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

class DashboardPage:
    def __init__(self, page: Page):
        self.page = page
        
        # Locator for profile icon which opens the dropdown menu
        self.profile_button = page.locator("#profile-click-icon")
        
        # Locator for the 'Log out' button in the profile dropdown
        self.logout_button = page.locator('text=Log out')

    # Method to verify if the user is logged in by checking the visibility of profile icon
    def is_logged_in(self):
        try:
            expect(self.profile_button).to_be_visible()
            return True
        except:
            return False

    # Method to perform logout by clicking the profile icon and then clicking 'Log out'
    def logout(self):
        try:      
            LoginPage.safe_click(self.profile_button)       # Click the profile button to open the dropdown
            expect(self.logout_button).to_be_visible()      # Wait until 'Log out' button is visible   
            LoginPage.safe_click(self.logout_button)        # Click the 'Log out' button
        except:
            raise Exception("Logout failed")                # Raise exception if any step fails

