# coding:utf8

import matplotlib.pyplot as plt
from random import choice

class RandomWalk():

    def __init__(self,num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """不断的漫步，直到列表达到指定的长度"""
        while len(self.x_values) < self.num_points:
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance
            #拒绝原地踏步，当x与y都等于0的时候，重新开始循环
            if x_step == 0 and y_step == 0:
                continue
            #计算下一个点的x与y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

#    def fill_walk(self):

#        x_step = self.get_step()
#        y_step = self.get_step()

while True:
    rw = RandomWalk(50000)
    rw.get_step()
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolor='none',s=1)
    # 模拟花粉在水滴表面的运动路径
    # plt.plot(rw.x_values,rw.y_values,linewidth=24)
    # 突出起点和终点
    plt.scatter(0,0,c='green',edgecolors='none',s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)
    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    # 设置绘图窗口的尺寸,单位为英寸,dpi设置分辨率
    #plt.figure(dpi=128,figsize=(10,6))
    plt.show()
    ##保存图片
    #plt.savefig('random_walk.png',bbox_inches='tight')
    keep_running = input('Make another walk?(y/n): ')
    if keep_running == 'n':
        break