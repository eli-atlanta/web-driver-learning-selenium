from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.ebay.com/")
wait = WebDriverWait(driver, 5)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'vl-feedback__survey')))
get_url = driver.current_url
print("The current url is:" + str(get_url))
search = driver.find_element(By.XPATH, "//div[@id='gh-ac-box2']/input")
search.send_keys("women watch")
button = driver.find_element(By.XPATH, "//td[@class='gh-td gh-sch-btn']/input")
button.click()
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'srp-controls__count-heading')))
var = driver.find_element(By.XPATH, "//h1[@class=‘srp-controls__count-heading’]/span[2]").text
assert var == "women watch"
driver.quit()