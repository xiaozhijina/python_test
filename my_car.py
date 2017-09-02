# coding:utf8

from random import randint

from car import  Car,ElectricCar,Battery

my_tesla = ElectricCar('tesla','model s','2017')
my_tesla.battery.describe_battery()
my_tesla.battery.battery_size = 85
my_tesla.battery.get_range()
my_tesla.odometer_reading = 23
my_tesla.read_odometer()
my_tesla.battery.get_range()
my_tesla.battery.describe_battery()

x = randint(1,6)
print(x)
