import os
import unittest
from appium import webdriver

from commons.test_data import TestData


class EnvironmentSetup(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        data = TestData.read_test_data_file()

        currentPath = helper_path = os.path.abspath(os.path.join(os.path.dirname(
            os.path.dirname(os.path.abspath(__file__)))))

        desired_caps = {}
        desired_caps['platformName'] = data['platformName'] #'Android'
        desired_caps['deviceName'] = data['deviceName'] #'LHBDU17921000275'
        desired_caps['app'] = currentPath + data['app'] #currentPath
        desired_caps['appPackage'] = data['appPackage'] #'com.iconology.comics'
        desired_caps['appActivity'] = data['appActivity'] #'com.iconology.ui.navigation.RouterActivity'
        self.driver = webdriver.Remote(data['appiumhub'], desired_caps) #'http://localhost:4723/wd/hub', desired_caps)
        self.comic_detail_page = None

    @classmethod
    def tearDownClass(self):
        self.driver.quit()