import click
from loguru import logger
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from webapp.market.models import Vitamins
from . import db


@click.command()
def save_products():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )

    driver.get('https://www.ozon.ru/brand/now-78432126/')
    products = driver.find_elements(By.CLASS_NAME, "l1m.lm2")

    for product in products:
        product_price = product.find_element(By.CLASS_NAME, '_33-a0')
        product_name = product.find_element(By.CLASS_NAME, 'tile-hover-target.kx4')
        product_link = product.find_element(By.TAG_NAME, 'a')
        product_url = product_link.get_attribute('href')

        try:
            new_product = Vitamins(
                name=product_name,
                price=product_price,
                image=product_name,
                url=product_url
            )
            db.session.add(new_product)
            db.session.commit()
        except Exception as e:
            logger.debug(e)

    driver.close()
