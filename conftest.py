import pytest
from settings import *

@pytest.fixture
def setup(playwright):
    browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
    context = browser.new_context(base_url=BASE_URL_TEST)
    
    page = context.new_page()
    
    yield page
    
    browser.close()
    