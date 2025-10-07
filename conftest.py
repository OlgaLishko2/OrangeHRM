import pytest
from requests import options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function", autouse=True)     #scope="function" - open browser for every test separately
def driver(request):    #фикстура инициалиэирует driver for tests
    options = Options()
    #options.add_argument("--headless")     #чтобы запускать тесты в CI, Docker
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options) # инициалиэируем driver
    request.cls.driver = driver #create driver object inside of tests classes (tests)
    yield driver #возвращаю driver
    driver.quit() #close browser

