from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_order_basket(browser):
    browser.get(link)
	# browser.implicitly_wait(4)   # время ожидания загрузки элементов страницы как альтернатива time.sleep
    time.sleep(30)
    button = browser.find_element_by_class_name('btn-add-to-basket')
    assert len(button.text) > 0, 'Кнопка добавления товара в корзину отсутсвует'
	# assert button != 'null', 'Кнопка добавления товара в корзину отсутсвует'  # еще вариант assert
	# assert button.is_displayed(), 'Кнопка добавления товара в корзину отсутсвует'  # еще вариант assert
