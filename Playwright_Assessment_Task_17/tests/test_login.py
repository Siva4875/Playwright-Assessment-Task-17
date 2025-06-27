from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

# Test cases for ZenClass login functionality
# Below are the test cases for the ZenClass Sucessful login Functionality
def test_successful_login(page):
    login = LoginPage(page)
    dashboard = DashboardPage(page)
    login.goto()                                            # Navigate to the login page
    login.login("validuser@gmail.com", "validpassword@1")   # Perform login # Replace with actual valid credentials
    assert dashboard.is_logged_in()                         # Assert that dashboard is visible (login successful)

# Below are the test cases for the ZenClass Unsucessful login Functionality
def test_unsuccessful_login(page):
    login = LoginPage(page)
    login.goto()                                            # Navigate to login page
    login.login("invaliduser@gmail", "wrong_pass")          # Attempt login with invalid data
    assert "Incorrect" in login.get_error_message()         # Verify the error message is shown

    # Below are the test cases for the ZenClass login page elements to Validate the Username and Password inputbox
def test_validate_input_fields(page):
    login = LoginPage(page)
    login.goto()
    page.wait_for_timeout(1000)                             # Give time for elements to load (optional)
    assert login.validate_fields_present()                  # Check if both fields are visible

# Below are the test cases for the ZenClass login page elements to Validate the Submit button
def test_submit_button(page):
    login = LoginPage(page)
    login.goto()
    assert login.is_submit_clickable()                      # Confirm that the login button is clickable

# Below are the test cases for the ZenClass login page elements to Validate the Logout button
def test_logout_functionality(page):
    login = LoginPage(page)
    dashboard = DashboardPage(page)
    login.goto()                                            # Go to login page
    login.login("validuser@gmail.com", "validpassword@1")   # Perform login # Replace with actual valid credentials
    page.wait_for_url("**/dashboard", timeout=10000)        # Wait for redirect to dashboard
    assert page.url.endswith("/dashboard")                  # Confirm navigation success
    page.wait_for_timeout(1000)                             # Optional: give page some breathing room
    assert dashboard.is_logged_in()                         # Confirm dashboard is loaded
    page.wait_for_timeout(1000)                             # Close any modal/pop-up that might block logout
    try:
        # Look for and click the modal's close button (update selector as per actual DOM)
        close_button = page.locator("button[aria-label='Close popup']")
        close_button.wait_for(state="visible", timeout=5000)
        close_button.click()
    except:
        # Fallback: if modal close button not found, press Escape to close
        page.keyboard.press("Escape")
    dashboard.logout()                                      # Proceed with logout
    page.wait_for_timeout(1000)
    assert page.url.endswith("/login")                      # Verify that the user has been redirected back to login page

