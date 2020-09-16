from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_order_basket(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_element_by_class_name('btn-add-to-basket')
    assert len(button.text) > 0, 'Кнопка добавления товара в корзину отсутсвует'
	
