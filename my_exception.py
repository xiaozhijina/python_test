# coding:utf8

""" 练习10 ，进行except的处理
"""
'''
while True:
    num1 = input('please input first number:')
    if num1 == 'q':
        break
    num2 = input('please input second number:')
    if num2 == 'q':
        break
    try:
        answer = int(num1) + int(num2)
    except ValueError:
        print('please input number ,it is not string')
    else:
        print(answer)
'''
with open('my_file\cats.txt','w+') as my_pets:
    my_pets.write('hashiqi\n')
    my_pets.write('xiaohei\n')
    my_pets.write('erha\n')
with open('my_file\dogs.txt','w+' ) as my_dogs:
    my_dogs.write('baozi\n')
    my_dogs.write('sanhei\n')
    my_dogs.write('erhua\n')
file_name = ['cats.txt','dogs.txt']
for file in file_name:
    try:
        with open('my_file\\' + file) as my_files:
            contents = my_files.read()
    except FileNotFoundError:
        print('file not exist')
    else:
        print('file name is',file + ' count is',contents.lower().count('xiao'))
