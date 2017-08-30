__author__ = 'xiaozhijian'
# coding:utf8
import os
'''
print("hello world")
print('it is very good')

name = "xiaozhijian"
print(name.upper())
print(os.system('cd c:\Python34'))
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print("hello," + full_name.title() + "!")
print(last_name.islower().bit_length())
print("\tpython")
print("languages:\n\tpython\n\tjavascript")
favorite_lanuages = " python "
print(favorite_lanuages.rstrip())
print(favorite_lanuages.lstrip())
print(favorite_lanuages.strip())
you_name = input("please input your name:")
print("hello %s,would you like to learn some python today?"%you_name)
print("hello",you_name,"would you like to learn some python today?")
print(you_name.title())
'''
'''
famous_name = " albert einstein "
message1 = "once said"
message2 = "a"
message = '"person who never made a mistake never tried anything new."'
print(name.title() + " " + message1 + "," + message2.upper() + " " + message)
message = 'once said,"A person who never made a mistake never tried anything now"'
print(famous_name.title() + " " + message)
print(famous_name.lstrip().title() + " " + message)
print(famous_name.rstrip().title() + " " + message)
print(famous_name.strip().title() + " " + message)
name = "xiao"
age = 26
message = "happy" + " " + name + " " + str(age) + "rd birtyday!"
print(message)
print("my name is",name)
#jisuan
print(4+4)
print(10-2)
print(2*4)
print(16/2)
like_number = 66
print("my love number is",like_number)
import this
'''
'''
name = ['xiaoming','xiaodong','xiaohua']
print(name[0].title())
messages = "my name is " + name[0].title() + "."
messages1 = "my name is " + name[1].title() + "."
print(messages)
print(messages1)
print(name)
name[0] = "xiaohei"
print(name)
name.append('xiaoming')
print(name)
'''
#列表的使用
'''
motocycle = []
motocycle.append('honda')
motocycle.append('yamaha')
motocycle.append('suzuki')
motocycle.insert(0,'ducati')
print(motocycle)
'''
'''del motocycle[0]
print(motocycle)
popped_motocycle = motocycle.pop()
print(popped_motocycle)
kk = motocycle.pop()
print(kk)
print(motocycle)
motocycle.remove('suzuki')
print(motocycle)
'''
'''
name = ['xiaoming','xiaodong','xiaoxi']
print(name)
print("无法出席的名单:" + name[0])
name[0] = "xiaozhi"
print(name)
print("我找到了更大的餐桌，所以想多邀请三个人")
name.insert(0,"xiaohong")
name.insert(2,"xiaoli")
name.append("xiaoke")
print(name)
print("由于餐具的原因，我现在只能邀请两个人参加宴会。")
gg = name.pop(0)
print(name)
print("我很抱歉，不能邀请你了:" + gg)
name.pop()
print(name)
name.pop()
print(name)
name.pop(2)
print(name)
print("恭喜你参加本次的聚餐：" + name[0] + "和" + name[1])
del name[0]
del name[0]
print(name)
number = [1,2,3]
print(number)
del number[1]
print(number)
'''
'''
car = ['bmw','toyata','audi']
car.sort()
print(car)
car.append('cobber')
print(car)
car.sort(reverse=True)
print(car)
print(sorted(car))
car.reverse()
print(car)
car.reverse()
print(car)
print(len(car))
print(car[-1])
'''
'''
love = ['xiaohong','xiaoru','xiaojia']
for i in love:
    print("my love is:",i.title())
message = "good luck"
print(message)
for number in range(1,6):
    print(number)
'''
#number_list = list(range(1,6))
#print(number_list)
'''
squares = []
for value in range(1,11):
#    square = value**2
    squares.append(value**3)
print(squares)
print(max(squares))
print(sum(squares))
print(min(squares))
test_list = [i for i in range(1,1000001)]
test = [i for i in range(1,21,3)]
print(test)
double_number = []
for i in range(3,31,3):
    double_number.append(i)
print(double_number)
x_list = [ i**3 for i in range(1,11)]
print(x_list)
print(x_list[0:3])
print(x_list[-4:-1])
'''
'''
my_food = ["cake","pizza","cook"]
friend_food = my_food[:]
print(my_food)
print(friend_food)
first_food = my_food.copy()
print(friend_food)
my_food.append('xigua')
print(my_food)
first_food.append('langua')
print(first_food)
messages = "The first three items in the list are:"
print(messages[:3])
for i in my_food:
    print(i)
'''
#### 元组
'''
foods = ("mogan",'xigua','putao','lizhi')
for i in foods:
    print(i)
foods = ('df','fdasf','gdvc')
for i in foods:
    print(i)
'''
## if 语句
'''
cars = ['bmw','audi','subaru']
for i in cars:
    if i == 'bmw':
        print(i.upper())
    else:
        print(i.title())
'''
######
'''
car = 'subaru'
print("is car == 'subaaru'? I predict True.")
print(car == 'subaru')
var_list = "my name is xiaozhijian"
var_list1 = "my sister name is xiaozhijian"
print(var_list == var_list1)
name = "Xiao"
print(name.lower() == 'xiao')
name_list = ['xiaohong','xiaoming']
if 'xiaodong' in name_list:
    print(True)
else:
    print(False)
if 'xiaoming' in name_list:
    print('good')
if 'xiaozhi' not in name_list:
    print('luck')
'''
'''
number = 0
number1 = []
number2 = []
alien_color = ['green','green','yellow','red','black']
for i in alien_color:
    if i == 'green':
        number1.append(number + 5)
    else:
        number2.append(number + 10)
print(sum(number1))
print(sum(number2))
'''
'''
yonghu = ['admin','guest','xiaoming','xiaoming','xiaozhi']
#yonghu = []
#### 判断列表是否为空 #########
if yonghu:
    for i in yonghu:
        if  i == 'admin':
            print('hello admin, would you like to see a status report?')
        else:
            print('hello Eric,thank you for logging in gagin.')
else:
    print('we need to find some users!')
'''
##### 使用多个列表 #############
'''
current_users = ['xiaozhi','xiaohong','xiaozhijian','xiaoru','xiaohu']
new_users = ['Xiaozhi','xiaohong','xiaoli','xiaomo','xiaokai']
for user in new_users:
    if user.lower() in current_users:
        print('please other name')
    else:
        print('this name is good')
'''
'''
number_list = list(range(1,10))
print(number_list)
for number in number_list:
    if number == 1:
        print('1st')
    elif number == 2:
        print('2nd')
    elif number == 3:
        print('3rd')
    else:
        print(str(number) + 'th')
'''
#### 字典 ####
'''
hoby = {'color':'yellow','sport':'basketball','foumas':'fbb'}
print(hoby['color'])
hoby['love'] = 'dog'
print(hoby)
name = ['c','b']
name.sort()
print(name)
alien_o = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x_positon: " + str(alien_o['x_position']))

if alien_o['speed'] == 'slow':
    x_increment = 1
elif alien_o['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_o['x_position'] = alien_o['x_position'] + x_increment
print("New x_positon: " + str(alien_o['x_position']))
alien_o['speed'] = 'fast'
print(alien_o)
del hoby['color']
print(hoby)
'''
'''
favorite_languages = {
    'jen': 'Python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'Python',
}
'''
'''
friend = ['phil','sarah']
for name,language in favorite_languages.items():
    print(name.title())
    if name in friend:
        print("Hi " + name.title() + ", I see your favorite language is " + language.title())
for name,language in favorite_languages.items():
    print(name.title() + "s faveorite language is " + language.title())
for name in sorted(favorite_languages.keys()):
    print(name.title())
for language in favorite_languages.values():
    print(language)

for language in set(favorite_languages.values()):
    print(language.title())
friend = ['jen','jake','maria']
for name in friend:
    if name in favorite_languages.keys():
        print(name.title() +  ' thank you')
    else:
        print(name.title() + ' i miss you')
aliens = []
for alien_number in range(20):
    new_alien = {'color': 'green','point': 5,'speed': 'medium'}
    aliens.append(new_alien)
for alien in aliens[:3]:
    if  alien['color'] == 'green':
        alien['color'] = 'black'
        alien['point'] = 12
        alien['medium'] = 'fast'
for alien in aliens[:5]:
    print(alien)
people1 = {'guo':'laili','san':'wuli','ha':'keli'}
people2 = {'ai':'huo','ke':'shen','zhzng':'ni'}
people = []
people.append(people1)
people.append(people2)
for people in people:
    print(people)
animal ={
    'baozi':['cat','me'],
    'louki':['dog','xiaoming'],
    'keke':['laohu','xiaodong']
}
for pet,people in animal.items():
    print("pet name is:" + pet + " ,master is:" + people[1])
'''
'''
cities = {
    'xiamen':{'country':'china','population':'1000w','fact':'beacutiful'},
    'beijing':{'country':'china','population':'2000w','fact':'weida'},
    'jinan':{'country':'china','population':'500w','fact':'silian'}
}
for city,detail in cities.items():
    print("my city is:" + city  + " details is:")
    for kk,gg in detail.items():
        if kk == 'country':
            print('\tmy country is ' + gg)
        elif kk == 'population':
            print('\tpopulation is ' + gg)
        elif kk == 'fact':
            print('\tfact is ' + gg)
'''
### 用户的输入与while循环
'''
prompt = "If you tell us who you are , we can personalize the messages you see."
prompt = prompt +  "\nWhat is your first name ?"
name = input(prompt)
print('\nHello,' + name.title())
while True:
    age = int(input('How old are you;'))
    if age == 18:
        print('you are so good')
        exit()
    elif age > 18:
        print('you are so old')
    else:
        print('you are a child')
'''
#### 7-3练习 ---求模运算符
'''
number = int(input('input you number: '))
if number%10 == 0:
    print('it is 10 double number')
else:
    print('it is not 10 double number')
curent_number = 1
while curent_number <=5:
    print(curent_number)
#    curent_number = curent_number + 1
    curent_number += 1
'''
### 标志位
'''
active = True
while active:
    name = input('please input your name: ')
    if name == 'xiaozhijian':
        print(name)
        active = False
    elif name == 'xiaozhi':
        print(name)
        active = False
    else:
        print(name)
'''
## continue-------不继续旧循环下的语句，继续新一轮的循环
'''
current_number = 0
while  current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
'''
'''
foods = []
active = True
while active:
    food = input('please input you like food: ')
    if food == 'quit':
        active = False
        print('my love food is :')
        for some_food in foods:
            print('\t' + some_food)
    else:
        foods.append(food)
'''
###  用while循环处理字典和列表
'''
unconfirmed_users = ['barry','alice','brian']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
#    print('verity user: ' + current_user.title())
    confirmed_users.append(current_user)
print('\nThe followingg users have been confirmed:')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
pets = ['dog','cat','dog','cat','rabbit','goldfish']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)
'''
'''
reponses = {}
#polling_active = True
#while polling_active:
while True:
    name = input('input your name :')
    reponse = input('Which mountain would you like to  climb someday?')
    reponses[name] = reponse
    repeat = input('would you like to let another person respond? (yes/no)')
    if repeat == 'no':
#        polling_active = False
        break
print('\n ``` Polling Results ```')
for name,reponse in reponses.items():
    print(name.title() + ' would like to climb ' + reponse.title() + '.')
'''
### 函数 #######
'''
def great_user(username):
    print('Hello, ' + username.title() + '!')
great_user('keli')
def make_shirt(size,word='I love Python'):
    print('you need sie is:' + size.title())
    print('you need word is:' + word.title())
make_shirt('34')
make_shirt(size='23',word='zhi')
def describe_city(city,country='china'):
    print(city.title() + ' is in ' + country.title())
describe_city('jinan')
describe_city(city='xiamen',country='fujian')
'''
#### 函数返回值####
'''
def get_formatted_name(first_name,last_name='jian'):
    full_name = first_name + ' ' +  last_name
#    print(full_name)
    return full_name.title()
musician = get_formatted_name('jimi','zhi')
print(musician)
while True:
    print('Please tell me your name: ')
    print('\nenter q to quit:')
    f_name = input('First name: ')
    if f_name == 'q':
        break
    l_name = input('Last name: ')
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(first_name = f_name,last_name = l_name )
    print('Hello, ' + formatted_name.title() + '!')
#musician = get_formatted_name('jimi','hendrix')
#print(musician)
def build_person(first_name,last_name,age=''):
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    return person
luck_boy = build_person('jimi','san',13)
print(luck_boy)
'''
'''
songs = {}
def make_album(signer,song,num=''):
    if num:
        song1 = {}
        song1['singer'] = signer
        song1['song']= song
        song1['num'] = num
        songs['zhuangji1'] = song1
    else:
        song2 = {}
        song2['signer'] = signer
        song2['song'] = song
        songs['zhuangji2'] = song2
#   return  songs1
while True:
    love_singers = input('please input your love singer is : ')
    if love_singers == 'quit':
        break
    love_songs = input('please input your love song is : ')
    if love_songs == 'quit':
        break
    love_nums = input('please input your love num is : ')
    if love_nums == 'quit':
        break
    make_album(love_singers,love_songs,love_nums)
#make_album('zhoujielun','daoxiang','3')
#make_album('mayun','only you')
print(songs)
'''
def user_list(username):
    for user in username:
        print('Hello, ' + user.title())
username = ['xiaozhi','zhidong','xiaoming']
user_list(username)



