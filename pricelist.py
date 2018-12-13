class Customer:
    price = None

    def __init__(self):
        self.discount = 0
        self.price = 0
        self.totalprice = 0

    def get_price(self):
        return self.price

    def set_price(self, price):
        if price >= 10000:
            self.discount = price * 0.10
            self.totalprice = price - self.discount
        else:
            self.totalprice = price
        self.price = price

    def __str__(self):
        receipt = """
Heild:          {OriginalPrice} 
Afsláttur:      {Discount}
-----------------------------------
Til greiðslu:   {TotalPrice}            


        """
        output = receipt.format(OriginalPrice=self.price, Discount=self.discount, TotalPrice=self.totalprice)
        return output

def main():
    print("-------Your store--------")
    price = 0

    n = 0
    while n != "q":
        price += int(n)
        n = input("Enter a price like (5995) and press(q to calculate): ")

    customer = Customer()
    customer.set_price(price)
    print(customer)


main()





