# coding:utf8
"""一个可用于表示汽车的类"""

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