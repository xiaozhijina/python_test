
import requests

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
print(plat)
for i in plat:
        if i['pname'] == 'yy':
            exist1 = str(i['sname'])
            with open('plat_svr_list','r') as plist:
               lines = plist.readlines()
            for i in lines:
                   if exist1 in i:
                       print()
#                   if line == exist1:
#                       print('server id exist')
                   else:
                        with open('plat_svr_list','a+') as plist1:
                            plist1.write('1 ' + i['sname'] + '\n')
        elif i['pname'] == 'swjoy':
            exist2 = i['sname']
            with open('plat_swjoy_list','a+') as swjoy_list:
                for line1 in swjoy_list.read():
                    if line1 == exist2:
                        pass
                    else:
                        swjoy_list.write('2 ' + i['sname'] + '\n')
        elif i['pname'] == '4366':
            with open('plat_4366_list','a+') as p_4366_list:
                p_4366_list.write('2 ' + i['sname'] + '\n')
        elif i['pname'] == 'yaodou':
            with open('plat_yaodou_list','a+') as yaodou_list:
                yaodou_list.write('2 ' + i['sname'] + '\n')
#order_lists = response_dict['']
