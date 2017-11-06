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
from LaVariables import workbookNameData
# -*- coding: utf-8 -*-

def AdjustResolution():
    display = Display(visible=0, size=(800, 800))
    display.start()


workbook = xlrd.open_workbook(workbookNameData)
worksheet = workbook.sheet_by_index(0)
url = worksheet.cell(1, 0).value
username = worksheet.cell(1, 1).value
password = worksheet.cell(1, 2).value
adjustResolution = worksheet.cell(1, 3).value


if adjustResolution == 1:
    AdjustResolution()


class Verify_Save_Place(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()


    def test_login_route_creation_and_deletion(self):
        driver = self.driver
        driver.get(url)

        # HEAD TO THE SEARCH MENU AND SAVE A PLACE
        try:
            searchButonWait = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'searchBtn')))
        except:
            searchButonWait = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'searchBtn')))

        driver.find_element_by_id('searchBtn').click()

        placeNameTxtWait = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'placeNameTxt')))
        placeNameTxtElem = driver.find_element_by_id('placeNameTxt')
        placeNameTxtElem.send_keys('Alexandria, LA, United States')
        placeNameTxtElem.send_keys(Keys.RETURN)

        saveAreaLinkWait = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "saveAreaLink")))

        # 777 MAYBE TALK TO DEV ABOUT THIS ONE: The work around I have surrendered to thus far
        driver.find_element_by_xpath('//*[@id="leftPanelContent"]/div/div[3]/a').click()

        # LOGIN FOR SAVING THE ROUTE
        pageLoadWait = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'userAccountEmail')))
        driver.find_element_by_id('userAccountEmail').send_keys(username) # Login
        driver.find_element_by_id('userAccountPassword').send_keys(password)
        driver.find_element_by_id('userAccountPassword').submit()

        time.sleep(4)

        driver.find_element_by_xpath('//*[@id="leftPanelContent"]/div/div[3]/a').click()

        time.sleep(4)

        driver.find_element_by_xpath('//*[@id="saveAreaForm"]/button').click()  # Clicking the submit button

        assert driver.find_element_by_xpath("//*[contains(text(),'Alexandria, LA, United States')]").is_displayed()

        time.sleep(8)

        driver.find_element_by_xpath('//*[@title="Customize and control Your 511"]').click()

        time.sleep(3)

        try:
            driver.find_element_by_xpath("//*[contains(text(), 'Delete this route')]").click()
        except:
            driver.find_element_by_class_name('deleteFavorite').click()

        alert = driver.switch_to.alert.accept()

        assert (driver.find_element_by_xpath("//*[contains(text(), 'Delete this route')]").is_displayed == False)


        # There seems to be some kind of eror after this, looks like it occurs when a place is already saved to the user's
        # places area

        time.sleep(10)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()