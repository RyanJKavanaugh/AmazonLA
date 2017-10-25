# coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common import action_chains, keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
import unittest
import xlrd
from pyvirtualdisplay import Display
# -*- coding: utf-8 -*-

# /Users/ryankavanaugh/Desktop/AmazonLA/

# Required Function For Working With Jenkins Virtual Machine
def AdjustResolution():
    display = Display(visible=0, size=(800, 800))
    display.start()


# Pull link and user credentials from excel spreadsheet
workbook = xlrd.open_workbook('LA CARS 5 Links.xlsx')
worksheet = workbook.sheet_by_index(0)
url = worksheet.cell(1, 0).value
username = worksheet.cell(1, 1).value
password = worksheet.cell(1, 2).value
adjustResolution = worksheet.cell(1, 3).value

if adjustResolution == True:
    AdjustResolution()


class Verify_LA_Cars_5(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)

    def test_Login(self):
        driver = self.driver

#        driver.maximize_window()
        driver.set_window_size(1800, 1100)

       # Login
        loginElement = driver.find_element_by_id('loginForm:usernameInput')
        passwordElement = driver.find_element_by_id('loginForm:passwordInput')
        loginElement.send_keys(username)
        passwordElement.send_keys(password)
        passwordElement.send_keys(Keys.ENTER)

        # Create an event
        mainPageWait = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'topbar-create-event')))
        createEventButton = driver.find_element_by_id('topbar-create-event')
        createEventButton.click()

        time.sleep(4)

        # Move to the middle of the Map and right click on the page
        createEventWait = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'eventEditingScreenForm:routePointFromGrid')))

        item = driver.find_element_by_class_name('gm-style-pbc')

#        hoverAndRightClick = ActionChains(driver).move_to_element(item).context_click(item)

        hoverAndRightClick = ActionChains(driver).move_to_element_with_offset(item, 1000, 500).context_click(item)

        hoverAndRightClick.perform()

        time.sleep(4)

        hover = ActionChains(driver).move_to_element_with_offset(item, -50, -55).context_click(item)

        hover.perform()


        time.sleep(10)


if __name__ == '__main__':
    unittest.main()


            # login to CARS 5
# try to grab an icon
# 1. create an event (try moving mouse to middle of the page and then clicking on it)
# 2. assert event exist
# 3. Also, think about checking buttons are enabled and that security settins work, think of little nuances to grow test coverage...











