product_price='- 2 444 ₽'
#print(type(product_price))
product_num = product_price.strip("-₽")
product_num = product_num.strip()

#product_num=int(product_num)
print(product_num)
#price_number
#print(product_num)
#product_price=[letter for letter in product_price if letter.isnumeric()]
#price_number=''.join(product_price)
#price=int(price_number)
#print(price)