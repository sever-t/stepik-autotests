from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link1 = "http://suninjuly.github.io/selects1.html"
link2 = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    # browser.get(link1)
    browser.get(link2)
    num1 = browser.find_element_by_id('num1')
    num2 = browser.find_element_by_id('num2')
    s =  str(int(num1.text) + int(num2.text))
    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_value(s)
    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    time.sleep(5)
    browser.quit()
