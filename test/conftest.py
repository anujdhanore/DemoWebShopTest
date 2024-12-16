import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def setUp(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(), options=options)
    driver.implicitly_wait(10)
    driver.get("https://demowebshop.tricentis.com/")
    driver.maximize_window()
    if request.cls is not None:
        request.cls.driver = driver
    yield
    driver.quit()
