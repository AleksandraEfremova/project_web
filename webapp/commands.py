import time

import click
from loguru import logger
from selenium import webdriver
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

    products = driver.find_elements(By.XPATH, "//*[@data-widget='searchResultsV2']/div[1]/div")

    for product in products:
        product_price = product.find_element(By.XPATH, './/div[1]/div[1]/div[1]')
        # product_name = product.find_element(By.CLASS_NAME, 'tile-hover-target.kx4')
        # product_link = product.find_element(By.TAG_NAME, 'a')
        # product_url = product_link.get_attribute('href')

        logger.info(product_price.text)

        # try:
        #     new_product = Vitamins(
        #         name=product_name,
        #         price=product_price,
        #         image=product_name,
        #         url=product_url
        #     )
        #     db.session.add(new_product)
        #     db.session.commit()
        # except Exception as e:
        #     logger.debug(e)

    driver.close()
