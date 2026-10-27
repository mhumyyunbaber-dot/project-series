# ----------------------------------------------------
# class Vehicle:
#     def __init__(self,name,max_speed,mileage):
#         self.name=name
#         self.max_speed=max_speed
#         self.mileage=mileage

# p1=Vehicle("Tesla","200kmh", "100k")
# print("Car Name",p1.name)
# print("Max Speed :  ",p1.max_speed)
# print("Mileage : " ,p1.mileage)

# ---------------------------------------------------

# class Rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def area(self):
#         return self.length * self.width
#     def perimeter(self):
#         return 2* (self.length + self.width)
# rect=Rectangle(10,4)
# print("Area =",rect.area())
# print("Perimeter =",rect.perimeter())

#  ---------------------------------------------

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
        
#     def average(self):
#         return sum(self.marks) / len(self.marks)
# result=Student("Ali",[85,67,70,90,50])
# print(f"{result.name} Average Grade is :{result.average()} ")

# -----------------------------------------------------

# class Product():
#     def __init__(self,name,price,quantity):
#         self.name=name
#         self.price=price
#         self.quantity=quantity
    
#     def total_value(self):
#         return self.price * self.quantity

# stock=Product("Laptop",500000,5)
# print(f"Total stock value of {stock.name}: {stock.total_value()}")

# -----------------------------------------------------

# class BanckAccount():
#     def __init__(self,balance):
#         self.balance=balance
        
#     def deposit(self, amount):
#         self.balance +=amount
#         print(f"Balance after deposit: {self.balance}")
#     def withdrawl(self,amount):
#         if amount < self.balance:
#             self.balance -= amount
#             print(f"Balance after withdrawl : {self.balance}")
#         else:
#             print(f"Insufficient Balance.current Balance :{self.balance}")

# account=BanckAccount(1000)
# account.deposit(500)
# account.withdrawl(200)
# account.withdrawl(2000)
    
    
# class BankAccount():
#     def __init__(self,balance):
#         self.balance=balance
    
#     def deposit(self,amount):
#         self.balance += amount
#         print(f"Total amount:{self.balance}")
    
#     def withdrawl(self,amount):
#         if self.balance >= amount:
#             print(f"Balance after withdrawl:{self.balance}")
#         else:
#             print(f"Insuffcient amount. \n your amount is:{self.balance}")
            
# Account=BankAccount(1000)
# Account.deposit(500)
# Account.withdrawl(300)
# Account.withdrawl(2000)

# --------------------------------------

class Light():
    def __init__(self):
        self.is_on=False
        
    def turn_on(self):
         self.is_on=True
    def turn_off(self):
        self.is_on=False
    def status(self):
        state="ON" if self.is_on else "OFF"
        print(f"Current status: {state}")

Light=Light()
Light.turn_on()
Light.status()
Light.turn_off()
Light.status