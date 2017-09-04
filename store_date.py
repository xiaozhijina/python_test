# coding:utf8

"""使用json模块进行数据的存储"""

import json
'''
number = input('what is your favorite number ?')
with open('love_number.json','w') as my_number:
    json.dump(number,my_number)
with open('love_number.json') as kk:
    favorite_number = json.load(kk)
    print('I know your favorite number! it is ' + favorite_number)

username = input('whar is your name:')
filename = 'username.json'

try:
    with open(filename,'r') as my_user:
        username2 = json.load(my_user)
except FileNotFoundError:
    username1 = input('what are you name?')
    with open(filename,'w') as current_user:
        json.dump(username,current_user)
        print('We will remember you when you come back, ' + username1 + ' !')
else:
    print('Welcome back, ' + username + ' !')
'''

def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as my_username:
            username3 = json.load(my_username)
    except FileNotFoundError:
        return None
    else:
        return username3

def get_new_username():
    """提示用户输入用户名"""
    username = input('What is your name? ')
    filename = 'username.json'
    with open(filename,'w') as my_username:
        json.dump(username,my_username)
    return username

def greet_user():
    username1 = get_stored_username()
    username2 = input('what is your name? ')
    if username2 == username1:
        print('Welcome back ' + username1)
    else:
        print('please correct username in the following: ')
        name = get_new_username()
        print('We will remember you when you come back, ' + name + ' !')
greet_user()

"""
使用json.dumps 将 json 格式的数据写到文件里
"""

measurements = [
    {'weight': 392.3, 'color': 'purple', 'temperature': 33.4},
    {'weight': 34.0, 'color': 'green', 'temperature': -3.1},
    ]

def store(measurements):
    import json
    with open('measurements.json', 'w') as f:
        f.write(json.dumps(measurements))

if __name__ == "__main__":
    store(measurements)

