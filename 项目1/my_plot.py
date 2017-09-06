# coding:utf8


import matplotlib.pyplot as plt
'''
input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.plot(input_values,squares,linewidth=5)

# 设置图表标题，并给坐标轴加上标签
plt.title('squares Numbers',fontsize=24)
plt.xlabel('Value',fontsize=14)
plt.ylabel('Square of Value',fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both',labelsize=14)
plt.show()
'''
'''
## 简单散点图
x_value = [1,2,3,4,5]
y_value = [1,4,9,16,25]
plt.scatter(x_value,y_value,s=200)
#设置图表标题，并给坐标轴加上标签
plt.title('Squares Numbers',fontsize=24)
plt.xlabel('Value',fontsize=14)
plt.ylabel('Square Of Value',fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both',which='major',labelsize=14)
plt.show()
'''
'''
# 自动计算数据

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
#自定义设置点的颜色，越接近0颜色越深，越接近1颜色越浅
#plt.scatter(x_values,y_values,c=(0.1,0.3,0),edgecolors='none',s=40)
# 使用颜色映射
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolors='none',s=40)
plt.title('Squares Number',fontsize=24)
plt.xlabel('Value',fontsize=14)
plt.ylabel('Square Of Value',fontsize=14)
# 设置每个坐标轴的取值范围
plt.axis([0,1100,0,1100000])
plt.savefig('squares_plot.png',bbox_inches='tight')
'''
# 练习15
x_values = list(range(1,5001))
y_values = [x**3 for x in x_values]

plt.title('Squares Numbers',fontsize=24)
plt.xlabel('Value',fontsize=14)
plt.ylabel('Square Of Value',fontsize=14)
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolor='none',s=20)
plt.tick_params(axis='both',which='major',labelsize=14)
plt.show()