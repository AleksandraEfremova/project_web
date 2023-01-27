from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def main():
    # options = Options()
    # options.add_argument("--headless")
    # options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(
        # options=options,
        service=ChromeService(ChromeDriverManager().install())
    )

    driver.get('https://www.wildberries.ru/brands/now')
    goods = driver.find_elements(By.CLASS_NAME, 'product-card.j-card-item.j-good-for-listing-event')

    for product in goods:
        price = product.find_element(By.CLASS_NAME, 'price__lower-price')
        name = product.find_element(By.CLASS_NAME, 'goods-name')
        rating = product.find_element(By.CLASS_NAME, 'product-card__rating stars-line star5')
        print(f'{price.text}\n {name.text}\n {rating.text}')

    driver.close()


if __name__ == '__main__':
    main()
