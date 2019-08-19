'''
最短路径 Dijkstra算法
'''
from math import inf

Node_dict = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H'}

Distance_martix = [[0,4,inf,2,inf,inf,inf,inf],
                   [inf,0,7,inf,inf,inf,5,inf],
                   [inf,inf,0,inf,2,1,inf,inf],
                   [inf,inf,inf,0,3,6,inf,inf],
                   [inf,inf,inf,inf,0,inf,inf,4],
                   [inf,inf,inf,inf,inf,0,6,inf],
                   [inf,inf,inf,inf,inf,inf,0,3],
                   [inf,inf,inf,inf,inf,inf,inf,0]]
Distance_dict = [{2:7,6:5},{4:2,5:1},{4:3,5:6},{7:4},{6:6},{7:3}]#每个点连接的边
start_node = 0
path_list = {0:[0,0]}#起始点添加到路径中,访问过的点的字典
no_path_list = {}#未访问的点路径字典
for i in range(1,8):
    no_path_list[i] = [0,i]

while len(no_path_list) > 0:
    min_node = 0
    min_value = inf
    min_path = []#初始化离起点最近的点

    for items in  no_path_list.items():
        #寻找离起点最近的点
        temp_node = items[0]
        temp_path = items[1]
        temp_value = Distance_martix[0][temp_node]
        if temp_value < min_value:
            min_node = temp_node
            min_value = temp_value
            min_path = temp_path

    path_list.update({min_node:min_path})#将最近的点加入访问过的路径字典
    no_path_list.pop(min_node)#未访问过的路径字典中删除该点


    try:#try的作用,如果某一点没有下一连接边,直接跳过
        #依次访问与当前点相连的边,更新到原点的距离
        for items in Distance_dict[min_node - 1].items():
            new_node = items[0]
            new_node_value = items[1]
            new_temp_value = new_node_value + min_value
            if Distance_martix[0][new_node] > new_temp_value:
                Distance_martix[0][new_node] = new_temp_value

                final_node = no_path_list[new_node].pop()

                no_path_list[new_node] = min_path.copy()
                no_path_list[new_node].append(final_node)
    except:
        pass

def transform(dict,arr):
    return [dict[i] for i in arr]

for item in path_list:
    path_list[item] = transform(Node_dict,path_list[item])

for items in path_list.items():
    print('路径:',items[1],'最短距离',Distance_martix[0][items[0]])
