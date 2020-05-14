menuList = []
priceList = []
def showBill():
    print("------- My Food ------")
    for number in range(len(menuList)):
        print(menuList[number], ":", priceList[number], "THB")
        total = 0
        for price in priceList:
            total += price
    print("----------------------")
    print("Total =", total, "THB")
while True:
    menuName = input("Please Enter Menu : ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = int(input("Price : "))
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()