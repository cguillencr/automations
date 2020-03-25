import os
import pytest
from appium import webdriver
from commons.test_data import TestData

@pytest.fixture(scope="class")
def driver_get(request):
    driver = None
    data = TestData.read_test_data_file()

    apk_path = helper_path = os.path.abspath(os.path.join(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__)))))+os.sep+"AppiumPython"+os.sep+"targets"+os.sep+data['app']

    desired_caps = {}
    desired_caps['platformName'] = data['platformName'] #'Android'
    desired_caps['deviceName'] = data['deviceName'] #'LHBDU17921000275'
    desired_caps['app'] = apk_path
    desired_caps['appPackage'] = data['appPackage'] #'com.iconology.comics'
    desired_caps['appActivity'] = data['appActivity'] #'com.iconology.ui.navigation.RouterActivity'
    driver = webdriver.Remote(data['appiumhub'], desired_caps) #'http://localhost:4723/wd/hub', desired_caps)

    request.cls.driver = driver

    yield
    driver.quit()

    return driver