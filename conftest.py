import pytest
import json
import urllib.parse

from playwright.sync_api import sync_playwright
from settings import *


# Função para criar a configuração de capabilities
def get_capabilities(browser):
    capabilities = CAPABILITY.copy()
    capabilities['browserName'] = browser
    #capabilities['LT:Options']['platform'] = browser_name["platformName"]
    capabilities['LT:Options']['playwrightClientVersion'] = PLAYWRIGHT_VERSION
        
    return capabilities

@pytest.fixture(params=["Chrome"])
def web_name(request):
    return request.param
    
@pytest.fixture
def browser(web_name, request):
    capabilities = get_capabilities(web_name)
    capabilities["LT:Options"]["name"] = request.node.name
    capabilities_parser = urllib.parse.quote(json.dumps(capabilities))  
    
    with sync_playwright() as p:          
        browser = p.chromium.connect(LAMBDA_WSS+capabilities_parser, timeout=120000)
        context = browser.new_context(base_url=BASE_URL_TEST)
        yield context
        browser.close() 