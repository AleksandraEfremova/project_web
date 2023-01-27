import time
import uuid
import random
import requests
from loguru import logger
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait




def main():
    #options = Options()
    #options.add_argument("--headless")
    #options.add_argument("--window-size=1920x1080")
    

    driver = webdriver.Chrome(
        #options=options,
        service=ChromeService(ChromeDriverManager().install())
    )

    driver.get('https://www.ozon.ru/brand/now-78432126/')
    goods = driver.find_elements(By.CLASS_NAME, "l1m.lm2") 
    logger.info(len(goods))

    SCROLL_PAUSE_TIME = random.randint(0, 200) * 0.01

    # Get scroll height
    full_height = driver.execute_script("return document.body.scrollHeight")
    window_height = driver.execute_script("return window.innerHeight")

    logger.info(full_height)
    logger.info(window_height)

    while True:
        # Scroll down to bottom
        scroll_size = random.randint(100, 1000)
        driver.execute_script(f"window.scrollTo(0, window.scrollY + {scroll_size})")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return window.scrollY") + window_height

        logger.info(new_height)

        if new_height >= full_height:
            break

        element_present = expected_conditions.presence_of_all_elements_located((By.TAG_NAME, "img"))
        WebDriverWait(driver, 50).until(element_present)
        #print(goods)
    for product in goods:
        price = product.find_element(By.CLASS_NAME, '_33-a0')         
        name = product.find_element(By.CLASS_NAME, 'tile-hover-target.kx4')

        #image = product.find_element(By.CLASS_NAME, 'k3y')
        url = product.find_element(By.TAG_NAME, "a")
        #print(type(price))
        print(price.text)
        #print(f'{url.get_attribute("href")}\n {price.text}\n {name.text}')
        #print(url.get_attribute('href'))
    
    driver.close()


if __name__ == '__main__':
    main()
