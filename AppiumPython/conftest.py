import os
import pytest
import sauceclient
from appium import webdriver
from commons.test_data import TestData

@pytest.fixture(scope="class")
def driver_get(request):
    driver = None
    data = TestData.read_test_data_file()

    apk_path = helper_path = os.path.abspath(os.path.join(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__)))))+os.sep+"AppiumPython"+os.sep+"targets"+os.sep+data['app']

    target = os.environ["target"]

    desired_caps = {}

    appium_hub=""
    if target=="saucelabs" :
        desired_caps['platformName'] = data['sauce_labs_platformName']
        desired_caps['platformVersion'] = data['sauce_labs_platformVersion']
        desired_caps['phoneOnly'] = data['sauce_labs_phoneOnly']
        desired_caps['tabletOnly'] = data['sauce_labs_tabletOnly']
        desired_caps['privateDevicesOnly'] = data['sauce_labs_privateDevicesOnly']
        appium_hub = data['sauce_labs_appiumhub']
        desired_caps['testobject_api_key'] = os.environ["sauce_labs_testobject_api_key"]

    else :
        desired_caps['platformName'] = data['platformName'] #'Android'
        desired_caps['deviceName'] = data['deviceName'] #'LHBDU17921000275'
        desired_caps['app'] = apk_path
        desired_caps['appPackage'] = data['appPackage'] #'com.iconology.comics'
        desired_caps['appActivity'] = data['appActivity'] #'com.iconology.ui.navigation.RouterActivity'
        appium_hub = data['appiumhub']

    driver = webdriver.Remote(appium_hub, desired_caps)
    request.cls.driver = driver

    yield
    driver.quit()

    return driver

@pytest.fixture(scope="class")
def driver_ios_get(request):
    driver = None
    data = TestData.read_test_data_file()

    ios_path = helper_path = os.path.abspath(os.path.join(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__)))))+os.sep+"AppiumPython"+os.sep+"targets"+os.sep+data['iosapp']

    desired_caps = {}
    desired_caps['platformName'] = data['iosplatformName'] #'iOS'
    desired_caps['platformVersion'] = data['iosplatformVersion']  # '13.3'
    desired_caps['deviceName'] = data['iosdeviceName'] #'iPhone 8 Plus'
    desired_caps['app'] = ios_path #/Users/testeruser/Library/Developer/Xcode/DerivedData/MySuperCoolApp-aywnvwgtroyznscaysfxzrxgkjrd/Build/Products/Debug-iphonesimulator/MySuperCoolApp.app
    driver = webdriver.Remote(data['appiumhub'], desired_caps) #'http://localhost:4723/wd/hub', desired_caps)

    request.cls.driver = driver

    yield
    driver.quit()

    return driver
