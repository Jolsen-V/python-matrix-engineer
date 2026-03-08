
# proyecto un simple tienda

print()
print("=== My first store simple ===")
print()
product_1 = "apple"
product_2 = "soda"
product_3 = "eggs"
product_4 = "orange"
product_5 = "bread"


price_1 = 2.89
price_2 = 1.99
price_3 = 3.50
price_4 = 2.32
price_5 = 4.03

stock_1 = 10 
stock_2 = 4
stock_3 = 0
stock_4 = 2
stock_5 = 8

price_end = (f"""The product: {product_1}, price: $ {price_1} and stock: {stock_1} end.
The product: {product_2}, price: $ {price_2} and stock: {stock_2} end.
The product: {product_3}, price: $ {price_3} and stock: {stock_3} end.
The product: {product_4}, price: $ {price_4} and stock: {stock_4} end.
The product: {product_5}, price: $ {price_5} and stock: {stock_5} end.""")
             
print(price_end)
print(type(price_end))