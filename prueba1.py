from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest

#--------------------------------------------------------------------#
# Esto es para internet explorer options = webdriver.IeOptions()
# Esto también driver = webdriver.Ie(service=service, options=options)
#--------------------------------------------------------------------#

def test_setup():
    global driver
    service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    # yield 
    # time.sleep(30)
    # driver.close()
    # driver.quit()
    # print("Test completed")

def test_google_search():
    driver.get("https://www.google.com")
    driver.find_element(By.NAME, "q").send_keys("youtube")
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "btnK")))
    button.click()

def test_youtube_search():    
    youtube_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'youtube.com')]")))
    youtube_link.click()
    driver.find_element(By.NAME, "search_query").send_keys("never gonna give you up")
    youtube_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='search-icon-legacy']")))
    youtube_button.click()

def test_first_video_click():
    first_result = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a#video-title")))
    first_result.click()

def test_teardown():
    time.sleep(15)
    driver.close()
    driver.quit()
    print("Test completed")

