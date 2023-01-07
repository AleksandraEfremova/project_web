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

    driver.get('https://www.ozon.ru/brand/now-78432126/')
    goods = driver.find_elements(By.CLASS_NAME, "l4m.lm5") 
    
    for product in goods:
        price = product.find_element(By.CLASS_NAME, '_33-a')         
        name = product.find_element(By.CLASS_NAME, 'tile-hover-target.kx7') 
        raiting = product.find_element(By.CLASS_NAME, 'dz3')
        print(f'{price.text}\n {name.text}\n {raiting.text}')
    
    driver.close()


if __name__ == '__main__':
    main()
