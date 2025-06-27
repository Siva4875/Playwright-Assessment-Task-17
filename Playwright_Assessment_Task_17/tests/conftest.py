import pytest
from playwright.sync_api import sync_playwright

# This fixture sets up the browser instance for the entire test session
@pytest.fixture(scope="session")
def browser():
    
    with sync_playwright() as p:                        # Start the Playwright context      
        browser = p.chromium.launch(headless=False)     # Launch a Chromium browser instance
        yield browser                                   # Yield the browser instance for use in tests
        browser.close()                                 # Close the browser after the session ends

# This fixture provides a fresh page (tab) for each test function
@pytest.fixture
def page(browser):                                      # Create a new browser context (isolated session)
    context = browser.new_context()                     # Open a new page within that context
    page = context.new_page()
    yield page                                          # Yield the page for test use
    context.close()                                     # Close the context after each test to clean up storage/cookies
