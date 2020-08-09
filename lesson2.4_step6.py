from selenium import webdriver
import time
  
link = "http://suninjuly.github.io/cats.html"

try:
    browser = webdriver.Chrome()
    # browser.implicitly_wait(5)   # неявное ожидание 5 сек
    browser.get(link)
    button = browser.find_element_by_id('button')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
