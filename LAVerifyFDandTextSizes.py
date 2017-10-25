from selenium import webdriver
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common import action_chains, keys
from selenium.webdriver.common.by import By
import xlrd
import time
import unittest
import os

# Test verifies the Future Info Toolbar buttons are fully functional

# Required Function For Working With Jenkins Virtual Machine
def AdjustResolution():
    display = Display(visible=0, size=(800, 800))
    display.start()


workbook = xlrd.open_workbook('DataLA.xlsx')
worksheet = workbook.sheet_by_index(0)
url = worksheet.cell(1, 0).value
adjustResolution = worksheet.cell(1, 3).value

if adjustResolution == True:
    AdjustResolution()

class Verify_Idaho_Links(unittest.TestCase):

    def test_Future_Info_Toolbar_Is_Active_Chrome(self):

        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.set_window_size(1800, 1100)
        driver.get(url)
        loginElement = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'timeFrameSelectorDiv')))

        driver.find_element_by_id('timeFrameSelectorDiv').click()

        assert driver.find_element_by_id('timeFrameSelectorDiv').is_enabled()

        assert driver.find_element_by_id('smallTextLnk').is_enabled()

        assert driver.find_element_by_id('normalTextLnk').is_enabled()

        assert driver.find_element_by_id('largeTextLnk').is_enabled()

        assert driver.find_element_by_id('textOnlySiteLinkSpan').is_enabled()

        driver.close()


    def test_Future_Info_Toolbar_Is_Active_Firefox(self):

        self.driver = webdriver.Firefox()
        driver = self.driver
        driver.set_window_size(1800, 1100)
        driver.get(url)
        loginElement = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'timeFrameSelectorDiv')))

        driver.find_element_by_id('timeFrameSelectorDiv').click()

        assert driver.find_element_by_id('timeFrameSelectorDiv').is_enabled()

        assert driver.find_element_by_id('smallTextLnk').is_enabled()

        assert driver.find_element_by_id('normalTextLnk').is_enabled()

        assert driver.find_element_by_id('largeTextLnk').is_enabled()

        assert driver.find_element_by_id('textOnlySiteLinkSpan').is_enabled()

        driver.close()


if __name__ == '__main__':
    unittest.main()

