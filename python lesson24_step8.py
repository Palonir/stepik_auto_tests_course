from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
  link = "http://suninjuly.github.io/explicit_wait2.html"
  browser = webdriver.Chrome()
  browser.get(link)

  WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
  browser.find_element(By.ID, "book").click()

  browser.execute_script("window.scrollBy(0, 100);")

  x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
  x = x_element.text
  y = calc(x)
  input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
  input1.send_keys(y)

  button2 = browser.find_element(By.ID, "solve")
  button2.click()

  print(browser.switch_to.alert.text.split(': ')[-1])

finally:
 time.sleep(10)
 browser.quit()

