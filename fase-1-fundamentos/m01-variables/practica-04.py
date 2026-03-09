# Mi tienda simple en la ciudad
print()
print("====== MY CLOTHING STORE ======")

order_1 = input("Choose your garment one: ")
order_2 = input("Choose your garment two: ")
order_3 = input("Choose your garment three: ")

product_1 = order_1
product_2 = order_2
product_3 = order_3

price_1 = 30.50
price_2 = 45.00
price_3 = 61.70

descount = 10 #se descuenta al precio original
iva_igv  = 18 # se agraga al precio original

des_final_1 = price_1 * (1 - descount/100) * (1 + iva_igv/100)
des_final_2 = price_2 * (1 - descount/100) * (1 + iva_igv/100)
des_final_3 = price_3 * (1 - descount/100) * (1 + iva_igv/100)

subtotal = des_final_1 + des_final_2 + des_final_3

price_final_1 = f"{product_1} $: {des_final_1:.2f}"
price_final_2 = f"{product_2} $: {des_final_2:.2f}"
price_final_3 = f"{product_3} $: {des_final_3:.2f}"

print("----YOUR FINAL PURCHASE-----")
print(f"price of first product is:  {price_final_1}")
print(f"price of second product is: {price_final_2}")
print(f"price of three product is:  {price_final_3}")

print("---------------------------------------------------")
print("==== DISCOUNTS + IGV APPLIED ====")

print(f"product: {product_1} → $: {des_final_1:.2f}")
print(f"product: {product_2} → $: {des_final_2:.2f}")
print(f"product: {product_3} → $: {des_final_3:.2f}")

print("---------------------------------------------------------------")
print("====== TOTAL PURCHASE =====")

print(f"first pledge payment:  {product_1} $: {des_final_1:.2f}")
print(f"second pledge payment: {product_2} $: {des_final_2:.2f}")
print(f"three pledge payment:  {product_3} $: {des_final_3:.2f}")

print("---------")
print("*** TOTAL TO PAY ***")
print("--------------")
print()

print(f"pay total $: {subtotal:.2f}")