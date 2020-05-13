usernameInput = input("Username : ")
passwordInput = input("Password : ")

if usernameInput == "admin" and passwordInput == "1234" :

    item_name_1   = str("Hot Cafe LATTE")
    item_name_2   = str("Hot Chocolate")
    item_name_3   = str("Hot Americano")

    item_price_1   = int(35)
    item_price_2   = int(40)
    item_price_3   = int(50)

    item_price_unit = str(" THB")

    print("Welcome to JJ.CAFE")
    print("1." , item_name_1 ,     item_price_1  ,item_price_unit)
    print("2." , item_name_2 ,     item_price_2  ,item_price_unit)
    print("3." , item_name_3 ,     item_price_3  ,item_price_unit)


    item_select = int(input("Select item (1-3) :"))
    item_qty    = int(input("how many qty do you need ? "))
    item_sum    = str("Total Price :")

    if item_select == 1:
        print(item_sum , item_qty * item_price_1, item_price_unit)

    elif item_select == 2:
        print(item_sum , item_qty * item_price_2, item_price_unit)

    elif item_select == 3:
        print(item_sum , item_qty * item_price_3, item_price_unit)

    else:
        print("Error : please select item 1-3")

else :
    print("Error : Invalid username or password")