def login():
    username = input("Username : ")
    password = input("Password : ")
    if (username == "admin" and password == "1234"):
        return True
    else:
        return False
def showMenu():
    print("JJ.Cafe  ")
    print("1.Vat Calculator")
    print("2.Price Calculator")
def menuSelect():
    Selected = int(input("Enter 1 or 2 :" ))
    if  (Selected == 1 ):
        totalPrice = int(input("Total Price :"))
        vatCalculate(totalPrice)
    elif(Selected == 2 ):
        priceCalculate()
    else:
        print("Error : Please Enter number 1 - 2")
def vatCalculate(totalPrice):
    result  = totalPrice * 1.07
    return print("result is :",result)

def priceCalculate():
    price_1 = int(input("First product price    : "))
    price_2 = int(input("Second product price   : "))
    return "result is : ",vatCalculate(price_1 + price_2)

if (login()):
    showMenu()
    menuSelect()
else :
    print("Error : Invalid Username or Password")