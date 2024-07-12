from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


browser = webdriver.Chrome()
browser.get('https://playmon.ru/counterstrike?')
browser.find_element(By.CSS_SELECTOR, "span[class='icon-search']").click()
# browser.find_element(By.XPATH, "//span[@class='icon-search']").click()
browser.find_element(By.ID, 'typeSearch').click()

sleep(5)
