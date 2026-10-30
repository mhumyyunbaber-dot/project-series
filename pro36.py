class office():
    def __init__(self,name):
        self.name=name
    
    def cal_pay(self):
        return 0
    
class part_time(office):
    def __init__(self, name,hour_rate,hourly_worked):
        super().__init__(name)
        self.hour_rate=hour_rate
        self.hourly_worked=hourly_worked
        
    def cal_pay(self):
        return self.hour_rate * self.hourly_worked

class full_time(office):
    def __init__(self,name,anually_salary):
        super().__init__(name)
        self.anually_salary=anually_salary
        
    def cal_pay(self):
        return self.anually_salary/12
    
pt=part_time("Ali",500,10)
ft=full_time("lab",1200)

print(f"{pt.name}'s Monthly salary {pt.cal_pay()}")
print(f"{ft.name}'s Mnthly salary {ft.cal_pay()}")

class Animal():
    def speak(self):
        return "some one "
    
class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow!"
    
dog=Dog()
cat=Cat()    
print(dog.speak())
print(cat.speak())