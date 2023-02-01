import time

import click
from loguru import logger
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from webapp.market.models import Vitamins
from . import db


@click.command()
def save_products():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )

    driver.get('https://www.ozon.ru/brand/now-78432126/')

    scroll_pause_time = 0.1
    full_height = driver.execute_script('return document.body.scrollHeight')
    window_height = driver.execute_script('return window.innerHeight')

    while True:
        scroll_size = 500
        driver.execute_script(f'window.scrollTo(0, window.scrollY + {scroll_size})')
        time.sleep(scroll_pause_time)
        new_height = driver.execute_script('return window.scrollY') + window_height

        if new_height >= full_height or new_height:
            break

    element_present = expected_conditions.presence_of_all_elements_located((By.TAG_NAME, "img"))
    WebDriverWait(driver, 50).until(element_present)

    products = driver.find_elements(By.CLASS_NAME, 'lm1.m1l')
    #logger.info(products)
    for product in products:
        product_price = product.find_element(By.CLASS_NAME, '_33-a0')
        product_price=product_price.text
        product_price_str = [letter for letter in product_price if letter.isnumeric()]
        product_price_number=''.join(product_price_str)
        product_price_number=int(product_price_number)
    
        product_name = product.find_element(By.CLASS_NAME, 'tile-hover-target.x3k')
        product_link = product.find_element(By.TAG_NAME, 'a')
        product_url = product_link.get_attribute('href')

        try:
            product_image = product.find_element(By.TAG_NAME, 'img')
        except NoSuchElementException as e: 
            logger.error(e)
        product_image_url = product_image.get_attribute("src")

        try:
            new_product = Vitamins(
            name=product_name.text,
            price=product_price_number,
            image=product_image_url,
            url=product_url
            )
            db.session.add(new_product)
            db.session.commit()
        except Exception as e:
            logger.debug(e)

    driver.close()

@click.command()
def save_productswb():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )

    driver.get('https://www.wildberries.ru/brands/now#c140253535')

    scroll_pause_time = 0.1
    full_height = driver.execute_script('return document.body.scrollHeight')
    window_height = driver.execute_script('return window.innerHeight')

    while True:
        scroll_size = 500
        driver.execute_script(f'window.scrollTo(0, window.scrollY + {scroll_size})')
        time.sleep(scroll_pause_time)
        new_height = driver.execute_script('return window.scrollY') + window_height

        if new_height >= full_height or new_height:
            break

    element_present = expected_conditions.presence_of_all_elements_located((By.TAG_NAME, "img"))
    WebDriverWait(driver, 50).until(element_present)

    products = driver.find_elements(By.CLASS_NAME, 'product-card__wrapper')
    #logger.info(products)
    for product in products:
        product_price = product.find_element(By.CLASS_NAME, 'product-card__price.price.j-cataloger-price')
        product_price=product_price.text
        product_price_str = [letter for letter in product_price if letter.isnumeric()]
        product_price_number=''.join(product_price_str)
        product_price_number=int(product_price_number)
    
        product_name = product.find_element(By.CLASS_NAME, 'product-card__brand-name')
        product_link = product.find_element(By.TAG_NAME, 'a')
        product_url = product_link.get_attribute('href')

        try:
            product_image = product.find_element(By.TAG_NAME, 'img')
        except NoSuchElementException as e: 
            logger.error(e)
        product_image_url = product_image.get_attribute("src")
        print(product_price)
        print(product_name.text)
        print(product_image_url)
        print(product_url)
        #try:
            #new_product = Vitamins(
            #name=product_name.text,
            #price=product_price_number,
            #image=product_image_url,
            #url=product_url
            #)
            #db.session.add(new_product)
            #db.session.commit()
        #except Exception as e:
            #logger.debug(e)

    driver.close()