# coding:utf8
### file use ####

#with open('pi_digits.txt') as file_object:
#    contents = file_object.read()
#    print(contents.rstrip())
#    print(contents)
'''
path = r'my_file\pi_digits.txt'
with open(path) as file_object:
    contents = file_object.readlines()
pi_string = ''
for line in contents:
    pi_string += line.strip()
birthday = input('please input your birthday : ')
if birthday in pi_string:
    print('good')
else:
    print('bad')
'''
path1 = r'my_file\learning_python.txt'
learning_list = ''
with open(path1) as learning_python:
#    learning = learning_python.read()
#    print(learning)
    learnings = learning_python.readlines()
for i in learnings:
    print(i.replace('Python','C').strip())


