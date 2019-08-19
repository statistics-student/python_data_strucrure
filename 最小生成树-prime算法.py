'''
最小生成树,Prime算法
'''
from math import inf
from functools import reduce

arr = [[0, 4, inf, inf, 8, 2],
       [4, 0, 2, inf, inf, 6],
       [inf, 2, 0, 6, inf, 4],
       [inf, inf, 6, 0, 7, 3],
       [8, inf, inf, 7, 0, 1],
       [2, 6, 4, 3, 1, 0]]

ref_dict = {}#字母数字对应表
for i in range(6):
    ref_dict[i] = chr(i+65)#{0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}

start = 0
V = [start]#已经访问集合
NV = [1,2,3,4,5]#未访问集合
Side_set = []#边集
while len(V) < 6:
    start_distance = inf
    node_Twain = ()#初始化最小边
    #遍历找到最小边
    for point in V:
        for i in NV:
            if arr[point][i] < start_distance and arr[point][i]!=0:
                start_distance = arr[point][i]
                node_Twain = (point,i)
    #根据是否该点访问加入边集合
    if node_Twain[1] not in V:
        V.append(node_Twain[1])
        NV.remove(node_Twain[1])
        Side_set.append(node_Twain)

def transform(ref_dict,num_arr):
    for i,item in enumerate(num_arr):
        num_arr[i] = (ref_dict[item[0]],ref_dict[item[1]])

path_arr = Side_set.copy()

sum_distance = reduce(lambda x,y:x+y,[arr[item[0]][item[1]] for item in Side_set])

transform(ref_dict,path_arr)

print("最短总距离:",sum_distance)
print("路径集合:")
print(path_arr)
