products = [ 

    {"name": "Keyboard", "price": 45}, 

    {"name": "Monitor", "price": 180}, 

    {"name": "Mouse", "price": 25}, 

    {"name": "Headphones", "price": 75}, 

    {"name": "USB Drive", "price": 15}, 

    {"name": "Webcam", "price": 60} 
]

fifty_lower = list(filter(lambda prices: prices["price"] <= 50, products))
print("Products Under $50: ")
for products in fifty_lower:
    print(f"{products["name"]} - ${products["price"]}")