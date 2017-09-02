# coding:utf8

##### 类的学习####
'''
class  Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print('love name: ' + self.restaurant_name + ' love type: ' + self.cuisine_type)
    def open_restarant(self):
        print(' restaurant openning')
my_restarunat = Restaurant('xiao','big')
my_restarunat.describe_restaurant()
my_restarunat.open_restarant()
'''
class User():

    def __init__(self,first_name,last_name,*user_info):
        self.first_name = first_name
        self.last_name = last_name
        self.user_info = user_info
        self.login_attempts = 0
    def describe_user(self):
        self.full_name = self.first_name + self.last_name
        for i in self.user_info:
            print(self.full_name.title() + ' age is: ' + str(i) + ' login_attempt is ' + str(self.login_attempts))
    def great_user(self):
        print('Hello ' + self.full_name)
    def increment_login_attempts(self):
        self.login_attempts += 1
#        print('login number is: ' + str(self.login_attempts))
    def reset_login_attempts(self):
        self.login_attempts = 0
        print('login number is: ' + str(self.login_attempts))
#my = User('xiao','zhijian',['26','df'])
#my.describe_user()
#my.great_user()
#my.increment_login_attempts()
#my.increment_login_attempts()
#my.increment_login_attempts()
#my.describe_user()
#my.reset_login_attempts()
#my.describe_user()
##################################
'''
class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 60
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):
        self.odometer_reading += miles
#        self.odometer_reading = self.odometer_reading + miles
class Battery():
    def __init__(self,model,battery_size=70):
        self.battery_size = battery_size
        self.model = model
    def describe_battery(self):
        print('This electric car has a ' + str(self.battery_size) + ' -Kwh battery.')
    def get_range(self):
        if self.battery_size == 70 and self.model == 'model s':
            range = 240
            print('This car ' + self.model.title() + ' can go approximately ' + str(range) + ' miles on a full charge')
        elif self.battery_size == 85 and self.model == 'audi':
            range = 270
            print('This car ' + self.model.title() + ' can go approximately ' + str(range) + ' miles on a full charge')
        else:
            range = 100
            print('This other car can go approximately ' + str(range) + ' miles on a full charge')
    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        """将实例用作属性"""
        self.battery = Battery('model s')
my_tesla = ElectricCar('tesla','model s','2017')
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.battery_size = 85
my_tesla.battery.get_range()
my_tesla.battery.model = 'audi'
my_tesla.battery.get_range()
my_tesla.battery.battery_size = 30
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
'''
########################## 练习9-7-8
class Admin(User):
    def __init__(self,first_name,last_name,*user_info):
        super().__init__(first_name,last_name,*user_info)
        self.privilege = Privileges()
class Privileges():
    def __init__(self):
        self.privileges = ['can add post','can delete post','can add user']
    def show_privileges(self):
        print('Admin can do following things ; ' )
        num = 1
        for i in self.privileges:
            print('\t' +str(num) +  ' ' + iv
            num += 1
my_admin = Admin('xiao','zhijian',23)
my_admin.privilege.show_privileges()
my_admin.privilege.privileges = ['xiao','zhi','jian']
my_admin.privilege.show_privileges()
####################导入类################

