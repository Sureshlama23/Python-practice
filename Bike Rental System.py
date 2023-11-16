class BikeRent:
    def __init__(self,stock):
        self.stock=stock
    def displaystockbike(self):
        print(""
              "Total avaible stoke bike",self.stock)
    def renrbike(self,q):
        if q<=0:
            print("Enter the greater than 0 amount")
        elif q>self.stock:
            print("Sorry the stock is not avaible")
        else:
            self.stock=self.stock-q
            print("Total order amount is:-",q*100)
            print("Avaible total bikes:-",self.stock)




while True:
    bike=BikeRent(100)
    uc=int(input('''
        1. Total Avaible Bikes
        2. Rent a Bike
        3. Exit
        
        
        '''))
    if uc==1:
            bike.displaystockbike()
    elif uc==2:
            n=int(input("Enter the quntity:-"))
            bike.renrbike(n)
    else:
        break


