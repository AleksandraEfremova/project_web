import uuid
import click
import requests
#from requests.exceptions import MissingSchema
from loguru import logger
from selenium import webdriver
from selenium.common import NoSuchElementException
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from flask.cli import with_appcontext


from webapp.market.models import Vitamins
#import config
from . import db


#@click.command()
def save_products():
    #options = Options()
    #options.add_argument("--headless")
    #options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(
        #options=options,
        service=ChromeService(ChromeDriverManager().install())
    )


    driver.get('https://www.ozon.ru/brand/now-78432126/')
    products = driver.find_elements(By.CLASS_NAME, "l1m.lm2") 
    
    for product in products:
        product_price = product.find_element(By.CLASS_NAME, '_33-a0')         
        product_name = product.find_element(By.CLASS_NAME, 'tile-hover-target.kx4')

        #try:
        product_link = product.find_element(By.TAG_NAME, 'a')
        #except NoSuchElementException:
           # continue
        #try:
        #product_image = product.find_element(By.CLASS_NAME, 'yk')
        #except NoSuchElementException:
            #continue
        

        product_url = product_link.get_attribute('href')    
        #product_image_url = product_image.get_attribute("src")
        #product_image_content = requests.get(product_image_url).content
        #product_image_dir = config.MEDIA_DIR
        #product_image_filename = f'{uuid.uuid4().hex}.jpg'

        #with open(f"{product_image_dir}/{product_image_filename}", 'wb') as f:
            #f.write(product_image_content)

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
