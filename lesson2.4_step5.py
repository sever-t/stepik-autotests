from selenium import webdriver
import time
  
# link = "http://suninjuly.github.io/wait2.html"
link = "http://suninjuly.github.io/wait1.html"

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)   # неявное ожидание 5 сек
    browser.get(link)
    button = browser.find_element_by_id("verify")
    button.click()
    message = browser.find_element_by_id("verify_message")
    assert "successful" in message.text

finally:
    time.sleep(10)
    browser.quit()
