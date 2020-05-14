class Customer:
    name = ""
    lastName = ""
    age= 0

    def addCart(self):
        print("Added to", self.name, self.lastName + "'s cart")

customer1 = Customer()
customer1.name = "Chatchai"
customer1.lastName = "B"
customer1.addCart()

customer2 = Customer()
customer2.name = "Prapimparn"
customer2.lastName = "N"
customer2.addCart()

customer3 = Customer()
customer3.name = "Peranut"
customer3.lastName = "J"
customer3.addCart()

customer4 = Customer()
customer4.name = "Jittarawadee"
customer4.lastName = "S"
customer4.addCart()