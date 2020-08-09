from selenium import webdriver
import os 
import time
  
link = "http://suninjuly.github.io/file_input.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_name('firstname')
    input1.send_keys('N')
    input2 = browser.find_element_by_name('lastname')
    input2.send_keys('F')
    input3 = browser.find_element_by_name('email')
    input3.send_keys('my@mail.ru')
    element = browser.find_element_by_id('file')
    current_dir = os.path.abspath(os.path.dirname(__file__))    
    file_path = os.path.join(current_dir, 'Primer.txt')          
    element.send_keys(file_path)
    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
