
class Raliwaypayment:
    def transcation(self,n,price):
        self.n=n
        self.price=price
    def print(self):
       if self.n*self.price==250*self.n:
           return 1
       elif self.n*self.price==500*self.n:
           return 1
       elif self.n*self.price==100*self.n:
           return 1
       else:
            return 0
class Raliwaystation(Raliwaypayment):
            def numberoftickets(self, n):
                self.n = n
            def priceofeachticket(self,price):
                self.price=price
            def display(self):
                print("Plese process payment")
                super().transcation(self.n,self.price)
            def prints(self):
                    if super().print()==1:
                        print("Tickets Book Succesfull")
                    else:
                        print("Tickets not Booked")

class customer:
    n=int(input("Enter the number of Tickets"))
    price=int(input("Enter the price of each Ticket"))
    r=Raliwaystation()
    r.numberoftickets(n)
    r.priceofeachticket(price)
    r.display()
    r.prints()


