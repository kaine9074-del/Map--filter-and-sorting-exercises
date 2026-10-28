prices = [25.00, 50.00, 75.00, 100.00, 150.00]

def sale_price(price):
    return f"{(price - (price * 0.2)):.2f}" 
sale = map(sale_price, prices)

print("Original:")
print(prices)
print("Off sale:")
print(list(sale))