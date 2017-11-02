# coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common import action_chains, keys
from selenium.webdriver.common.by import By
import time
import unittest
import xlrd
from pyvirtualdisplay import Display
# -*- coding: utf-8 -*-

def AdjustResolution():
    display = Display(visible=0, size=(800, 800))
    display.start()


workbook = xlrd.open_workbook('DataLA.xlsx')
worksheet = workbook.sheet_by_index(0)
url = worksheet.cell(1, 0).value
username = worksheet.cell(1, 1).value
password = worksheet.cell(1, 2).value
adjustResolution = worksheet.cell(1, 3).value

if adjustResolution == 1:
    AdjustResolution()


class Verify_Save_Place(unittest.TestCase):

    # def setUp(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.maximize_window()

    def test_login_route_creation_and_deletion(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        driver = self.driver
        driver.get(url)

        searchButonWait = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'searchBtn')))
        driver.find_element_by_id('searchBtn').click()

        placeNameTxtWait = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'placeNameTxt')))
        placeNameTxtElem = driver.find_element_by_id('placeNameTxt')
        placeNameTxtElem.send_keys('Alexandria, LA, United States')
        placeNameTxtElem.send_keys(Keys.RETURN)

        saveAreaLinkWait = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "saveAreaLink")))

        time.sleep(3)

        testList = driver.find_element_by_id('leftPanelContent')
        # print testList
        # print testList.text

        saveLink = driver.find_element_by_xpath("//*[contains(text(), 'Save')]")

        print saveLink
        print saveLink.get_attribute('src')
        print saveLink.get_attribute('OuterHTML')
        # for item in testList:
        #     item.click()

        # The work around I have surrendered to thus far
        driver.find_element_by_xpath('//*[@id="leftPanelContent"]/div/div[3]/a').click()

        #images/favorites/star_icon_yellow.png
        # #leftPanelContent > div > div:nth-child(4) > a


        time.sleep(40)

    # def tearDown(self):
    #     print '\n' + "Test Completed"
    #     self.driver.quit()


if __name__ == '__main__':
    unittest.main()

# //*[@id="leftPanelContent"]/div/div[3]/a/text()