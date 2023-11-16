class AtmMachine:
    def __init__(self,amount):
        self.amount=amount
    def display_amout(self):
        print("Total Avaible balance is:-",self.amount)
    def witdrawal(self,A):
        if A==0 and A<500:
            print("Please enter amount greater than 500")
        elif A>self.amount:
            print("Not enough balane")
        else:
            self.amount=self.amount-A
            print("Thanks for vistintg please take your cash",A)
            print("Total Avaible balance is:-",self.amount)
    def fastwithdrawal(self,fw):
        if fw==0 and fw>5:
            print("Please enter valid number")
        elif fw==1:
            self.amount = self.amount-1000
            print("Thanks for vistintg please take your cash", 1000)
            print("Total Avaible balance is:-", self.amount)
        elif fw==2:
            self.amount = self.amount-5000
            print("Thanks for vistintg please take your cash", 5000)
            print("Avaible balance is:-", self.amount)
        elif fw==3:
            self.amount = self.amount-10000
            print("Thanks for vistintg please take your cash", 10000)
            print("Total Avaible balance is:-", self.amount)
        elif fw==4:
            self.amount = self.amount-20000
            print("Thank for vistintg please take your cash", 20000)
            print("Total Avaible balance is:-", self.amount)
        else:
            self.amount = self.amount-25000
            print("Thanks for vistintg please take your cash", 25000)
            print("Total Avaible balance is:-", self.amount)

while True:
    cash=AtmMachine(50000)
    uc=int(input('''
    Welcome to Demo Bank Ltd
      Select Action
      1. Input your pincode
      2. Exit
    enter here:- 
    '''))
    if uc==1:
        p=int(input("Enter Your Pincode:-"))
        if p==1994:
            n=int(input('''
            Select Action
            1.Check Avaible balance
            2. Cash Withdrawal
            3. Fast Withdrawal          
            '''))
            if n==1:
                cash.display_amout()
            elif n==2:
                c=int(input("Enter amount:-"))
                cash.witdrawal(c)
            elif n==3:
                fw=int(input('''
            Select Amount:-
                1. 1000
                2. 5000
                3. 10000
                4. 20000
                5. 25000              
                '''))
                cash.fastwithdrawal(fw)
        else:
            print("invalid pincode")
    else:
        break