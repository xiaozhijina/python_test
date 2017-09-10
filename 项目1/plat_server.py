# coding:utf8

import requests
import datetime

#a = datetime.datetime.fromtimestamp(1503716400).strftime("%Y-%m-%d %H:%M:%S")
#print(a)
#获得工单里面的开服信息
url = 'http://testqxm.cqms.nw175.com:10049/serverOp/getOrderlist'
file_location = 'plat.list'
r = requests.get(url)
print('status code',r.status_code)
response_dict = r.json()
plat = []
for response in response_dict:
    plat_server = {}
    plat_server['sname'] = response['svrname']
    plat_server['pname'] = response['pname']
    plat.append(plat_server)
#########################
###设置文件路径
file_local = '/data/yfsh/'
#### 获取已存在开服区服的信息存入列表中
yy = []
try:
    with open('plat_svr_list','r') as plist:
        for list in plist:
            yy.append(list)
except FileNotFoundError:
    with open('plat_svr_list','a+') as plist:
        for list in plist:
            yy.append(list)
################################
swjoy = []
try:
    with open('plat_swjoy_list','r') as plist2:
        for list in plist2:
            swjoy.append(list)
except FileNotFoundError:
     with open('plat_swjoy_list','a+') as plist2:
        for list in plist2:
            swjoy.append(list)
##################################
f_4366 = []
try:
    with open('plat_4366_list','r') as plist3:
        for list in plist3:
            f_4366.append(list)
except FileNotFoundError:
    with open('plat_4366_list','a+') as plist3:
        for list in plist3:
            f_4366.append(list)
####################################
yaodou = []
try:
    with open('plat_4366_list','r') as plist4:
        for list in plist4:
            yaodou.append(list)
except FileNotFoundError:
    with open('plat_4366_list','a+') as plist4:
        for list in plist4:
            yaodou.append(list)
### 过滤判断区号是否存在，属于哪个区服，填入对应的文件中
sname = []
for name in plat:
    sname.append(name['sname'])
for i in plat:
    if i['pname'] == 'yy':
        exist1 =  '1 ' +  i['sname'] + '\n'
        if exist1  in yy:
            print(' districk id exist')
        else:
            with open('plat_svr_list','a+') as plist1:
                for x in sname:
                    if x[2] == 's' or x[2] == 't':
                        new_name = x[0] + x[2:]
                        plist1.write('1 ' + new_name + '\n')
                    else:
                        plist1.write('1 ' + i['sname'] + '\n')
    elif i['pname'] == 'swjoy' or i['pname'] == 'swjoys':
            exist2 = '2 ' + i['sname'] + '\n'
            if exist2 in swjoy:
                print('bad')
            else:
                with open('plat_swjoy_list','a+') as swjoy_list:
                    swjoy_list.write('2 ' + i['sname'] + '\n')
    elif i['pname'] == '4366':
            exist3 = '3 ' + i['sname'] + '\n'
            if exist3 in f_4366:
                print('districk id is exist')
            else:
                with open('plat_4366_list','a+') as p_4366_list:
                    p_4366_list.write('3 ' + i['sname'] + '\n')
    elif i['pname'] == 'yaodou':
            exist4 = '4 ' + i['sname'] + '\n'
            if exist4 in yaodou:
                print('districk id is exist')
            else:
                with open('plat_yaodou_list','a+') as yaodou_list:
                    yaodou_list.write('4 ' + i['sname'] + '\n')