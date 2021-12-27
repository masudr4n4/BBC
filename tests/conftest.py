import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



@pytest.fixture
def driver(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    failed_before = request.session.testsfailed
    yield driver
    if request.session.testsfailed != failed_before:
        allure.attach(driver.get_screenshot_as_png(), name=request.node.name,
                      attachment_type=allure.attachment_type.PNG)
    driver.quit()

