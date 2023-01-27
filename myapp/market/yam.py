from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def main():
    #options = Options()
    #options.add_argument("--headless")
    #options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(
        #options=options,
        service=ChromeService(ChromeDriverManager().install())
    )

    driver.get('https://market.yandex.ru/search?vendorId=9282801&viewtype=grid&suggest_text=NOW&allowCollapsing=1&local-offers-first=0&glfilter=7893318%3A9282801')
    goods = driver.find_elements(By.CLASS_NAME, '_1nO7x.uG_0s') 
    
    for product in goods:
        price = product.find_element(By.CLASS_NAME, '_2dGOi')         
        name = product.find_element(By.CLASS_NAME, '_2f75n._24Q6d.cia-cs') 
        raiting = product.find_element(By.CLASS_NAME, '_2qvOO._19m_j._1Cjcb.cia-cs')
        print(f'{price.text}\n {name.text}\n {raiting.text}')
        #print(price.text)
    driver.close()


if __name__ == '__main__':
    main()