# -*- coding: utf-8 -*-

import time
import time

import keyboard as kb
import pandas
import pyautogui as pg
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

listt = []

driver = webdriver.Chrome(ChromeDriverManager().install())
quantity_list = []
skladi = []
products_list = []
id = []
for i in range(610000, 700000):

    driver.get(f'https://www.wildberries.ru/seller/{i}')
    try:
        element = driver.find_element_by_xpath('/html/body/div[1]/main/div[2]/div/div/div[4]/div[1]/div[1]/div[2]/div[1]/span')
        element.click()

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        elemett = soup.find('div', class_='spa-tooltip tooltip-supplier').text
        quantity = soup.find('div', class_ = 'seller-details__parameter-item').text
        products = soup.find('div', class_ = 'seller-details__count-products').text
        listt.append(elemett)
        products_list.append(products)
        quantity_list.append(quantity)
        id.append(i)
        # sklad = driver.find_element_by_xpath('/html/body/div[1]/main/div[2]/div/div/div[6]/div[1]/div[4]/div/div/div[1]/div/a')
        # sklad.click()
        # sklad2 = soup.find('div', class_ = 'same-part-kt__delivery-row').text
        # skladi.append(sklad2)
        print(listt)
        print(quantity_list)
        #print(skladi)
        print(products_list)
        print(id)


    except:
        continue
df = pandas.DataFrame({'Название организации': listt, 'Количество проданного товара': quantity_list, 'Количество sku': products_list, 'ID': id})
df.to_excel('wb13.xlsx')

# print(len(listt))
# print(listt)
#
#
ogrn = []
for i in range(len(listt)):
    ogrn.append(listt[i].partition('ОГРН:')[2])
print(ogrn)
#
#
# for i in range(4, len(listt)):
#     time.sleep(2)
#     pg.click(x=285, y=25)
#     time.sleep(1)
#     pg.click(x=240, y=200)
#     time.sleep(2)
#     a = listt[i]
#     kb.write(a)
#     time.sleep(1)
#     pg.click(x=288, y=341)
#     time.sleep(4)
#     pg.click(x=441, y=498)
#     time.sleep(3)
#     kb.send('ctrl + a')
#     time.sleep(4)
#     kb.send('ctrl + insert')    #!!!!! <- внимание
#     time.sleep(2)
#     pg.click(x=1179, y=466)
#     time.sleep(2)
#     kb.send('ctrl + end')
#     time.sleep(1)
#     kb.send('ctrl + v')
#     time.sleep(2)
#     pg.click(x=74, y=26)
#     time.sleep(1)
#     pg.click(x=394, y=28)