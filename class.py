# coding:utf8

##### 类的学习####

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

class User():

    def __init__(self,first_name,last_name,*user_info):
        self.first_name = first_name
        self.last_name = last_name
        self.user_info = user_info
    def describe_user(self):
        self.full_name = self.first_name + self.last_name
        for i in self.user_info:
            print(self.full_name.title() + ' age is: ' + str(i))
    def great_user(self):
        print('Hello ' + self.full_name)
my = User('xiao','zhijian',['26','df'])
my.describe_user()
my.great_user()