# coding:utf8
##在函数中修改列表

'''
completed_models = ['lokk']
def print_models(eunprinted_designs,completed_models):
    while eunprinted_designs:
        current_design = eunprinted_designs.pop()
        print('Printing model: ' + current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    print('\nThe follwing models have been printd:')
    for completed_model in completed_models:
        print(completed_model)
eunprinted_designs = ['iphone case','robot pendant','dodecahedxon']
print_models(eunprinted_designs[:],completed_models)
show_completed_models(completed_models)
print(eunprinted_designs)
'''
### 练习8-9-10
'''
famous_magician = []
def show_magicians(magician_list):
    for magician in magician_list:
        print(magician)
def make_great(magician_list):
    while magician_list:
        current_magician = magician_list.pop()
        famous_magician.append('The Great ' + current_magician)
#    print(famous_magician)
#make_great(['xiaoming','xiaodong','xiaozhi'])
magician_list = ['xiongkousuidashi','dulongzhuang','daoguajingou']
make_great(magician_list[:])
show_magicians(magician_list)
show_magicians(famous_magician)
'''
# 位置实参和任意数量实参
'''
def para_num(size,**topping):
    print('The following is : ')
    for i,k in topping.items():
        print('- ' + str(size) + i + k)
para_num(13,location='xiao',user='zhi')
def sanmingzhi(*topping):
    print('custom love topping is following :')
    for i in topping:
        print("\t" + i)
sanmingzhi('peigen','chiken')
def cars(producers,types,**car_info):
    cars_info = {}
    cars_info['producers'] = producers
    cars_info['type'] = types
    for i,j in car_info.items():
        cars_info[i] = j
    return cars_info
car = cars('subaru','outback',color='blue',tow_package='low')
for k,l in car.items():
    print('my car ' + k + ' is : '+  l)
print(car['producers'])
'''
#### 导入模块和模块中的函数 ###
'''
from test import get_formatted_name,user_list,build_person
boy = build_person('jimi','san',5)
print(boy)
user_list(['xiaozhijian'])
from test import user_list as t
t(['xiao'])'
import test as t
t.user_list(['good'])
'''
