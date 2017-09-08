# coding:utf8

import csv
import matplotlib.pyplot as plt
from _datetime import  datetime

filename = 'a.csv'
with open(filename) as f:
    reader = csv.reader(f)
    # 读取一行数据
    header_row = next(reader)
#    for index,colunm_header in enumerate(header_row):
#        print(index,colunm_header)
    highs = []
    dates = []
    lows= []
#highs,dates,low = [],[],[] 上面的三个可以合成一个的形式
    #迭代的方式一行一行读取全部数据
    for row in reader:
        try:
            current_date = datetime.strptime(row[0],'%Y-%m-%d')
            high = int(row[1])
            low =int(row[2] )
        except ValueError:
            print(current_date,'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

#根据数据绘制图形
fig = plt.figure(dpi=64,figsize=(10,6))
# alpha 指定颜色的透明度
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
plt.title("Daily high temporary,July 2017",fontsize=24)
plt.xlabel('Date',fontsize=16)
#绘制斜的日期标签，以避免他们彼此重叠。
fig.autofmt_xdate()
plt.ylabel('Temperature(F)',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()
