import numpy as np
import matplotlib.pyplot as plt
import random as rd

color=['r','black','y','g','blue','pink','tan','brown','gray','cyan','peru','m','c','indigo','hotpink']*2
x_data=[i for i in range(1,31)]
height=np.random.randint(1,1000,30)
data_color=dict()
for i in range(0,30):
    data_color[height[i]]=color[i]
def quick_sort(array, data_color,x_data,l,r):
    if l >= r:
        return
    stack = []
    stack.append(l)
    stack.append(r)
    plt.ion()#开启交互模式
    while stack:
        low = stack.pop(0)
        high = stack.pop(0)
        if high - low <= 0:
            continue
        x = array[high]
        i = low-1
        for j in range(low, high):
            if array[j] <= x:
                i += 1
                array[i], array[j] = array[j], array[i]
                color=[data_color[i] for i in array]
                plt.cla()#清除上一幅图
                plt.bar(x_data,height=array,color=color)
                plt.pause(0.1)
        array[i + 1], array[high] = array[high], array[i + 1]
        color = [data_color[i] for i in array]
        plt.cla()#清除上一幅图
        plt.bar(x_data, height=array, color=color)
        plt.pause(0.1)
        stack.extend([low, i, i + 2, high])
    plt.ioff()#关闭交互模式
    plt.show()
    return array

quick_sort(height,data_color,x_data,0,29)

#quick_sort([10,9,20,11,7,5,2,3,2,4],{5:'r',4:'pink',3:'y',2:'g',1:'b',10:'r',9:'pink',20:'y',11:'g',7:'b'},[1,2,3,4,5,6,7,8,9,10],0,9)












