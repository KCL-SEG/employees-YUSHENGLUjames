"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name,monthPay,month,hourPay,hour,commPay,comm,bonus):
        self.name = name
        self.monthPay = monthPay
        self.month = month
        self.hourPay = hourPay
        self.hour = hour
        self.commPay = commPay
        self.comm = comm
        self.bonus = bonus

    def get_pay(self):
        self.totalPay = self.monthPay*self.month + self.hourPay*self.hour + self.commPay*self.comm + self.bonus
        return self.totalPay

    def __str__(self):
        if(self.monthPay>0 and self.hourPay==0 and self.commPay==0 and self.bonus==0):
            print(self.name,"works on a monthly salary of "+str(self.monthPay)+". Their total pay is",str(self.totalPay)+".")
        if(self.monthPay==0 and self.hourPay>0 and self.commPay==0 and self.bonus==0):
            print(self.name,"works on a contract of",self.hour,"hours at "+str(self.hourPay)+"/hour. Their total pay is "+str(self.totalPay)+".")
        if(self.monthPay>0 and self.hourPay==0 and self.commPay>0 and self.bonus==0):
            print(self.name,"works on a monthly salary of",self.monthPay,"and receives a commission for",self.comm,"contract(s) at "+str(self.commPay)+"/contract. Their total pay is "+str(self.totalPay)+".")
        if(self.monthPay==0 and self.hourPay>0 and self.commPay>0 and self.bonus==0):
            print(self.name,"works on a contract of",self.hour,"hours at "+str(self.hourPay)+"/hour and receives a commission for",self.comm,"contract(s) at "+str(self.commPay)+"/contract. Their total pay is "+str(self.totalPay)+".")
        if(self.monthPay>0 and self.hourPay==0 and self.commPay==0 and self.bonus>0):
            print(self.name,"works on a monthly salary of",self.monthPay,"and receives a bonus commission of "+str(self.bonus)+". Their total pay is "+str(self.totalPay)+".")
        if(self.monthPay==0 and self.hourPay>0 and self.commPay==0 and self.bonus>0):
            print(self.name,"works on a contract of",self.hour,"hours at "+str(self.hourPay)+"/hour and receives a bonus commission of "+str(self.bonus)+". Their total pay is "+str(self.totalPay)+".")
        return self.name


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie',4000,1,0,0,0,0,0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie',0,0,25,100,0,0,0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee',3000,1,0,0,200,4,0)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',0,0,25,150,220,3,0)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie',2000,1,0,0,0,0,1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel',0,0,30,120,0,0,600)

billie.get_pay()
charlie.get_pay()
renee.get_pay()
jan.get_pay()
robbie.get_pay()
ariel.get_pay()
str(billie)
str(charlie)
str(renee)
str(jan)
str(robbie)
str(ariel)
