def vatInclude(price):
    total = price * 1.07
    return total
price = int(input("Price :"))
print(vatInclude(price))