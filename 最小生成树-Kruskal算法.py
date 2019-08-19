'''
最小生成树,Kruskal算法
'''
from math import inf


arr = [[0, 4, inf, inf, 8, 2],
       [4, 0, 2, inf, inf, 6],
       [inf, 2, 0, 6, inf, 4],
       [inf, inf, 6, 0, 7, 3],
       [8, inf, inf, 7, 0, 1],
       [2, 6, 4, 3, 1, 0]]

#创建边索引和权重的三元组列表
Edges = []
for i in range(5):
    for j in range(i+1,6):
        if arr[i][j] != inf:
            Edges.append((i,j,arr[i][j]))
            
Edges.sort(key=lambda x:x[2])#边按权值升序排列

flag_set = list(range(1,7))#初始化连通分量,各不相同

#字母数字对应表
ref_dict = {}
for i in range(6):
    ref_dict[i] = chr(i+65)#{0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}

Side_set = []#边集

tag_start = -1#初始化添加的连通分量所属连通flag,区别于未遍历的情况,所以为负数

while len(set(flag_set)) != 1:
    for items in Edges:
        tag1 = flag_set[items[0]]
        tag2 = flag_set[items[1]]
        if tag1 > 0 and tag2 > 0:#如果都没有所属连通分量
            flag_set[items[0]] = tag_start
            flag_set[items[1]] = tag_start
            Side_set.append(items)
            tag_start -= 1 #如果下一组连通分量不同于上一组,为区分,flag - 1

        elif tag1*tag2 < 0:#如果一个加入连通分量,另一个没有加入
            min_flag = min(flag_set[items[0]],flag_set[items[1]])
            flag_set[items[0]] = min_flag
            flag_set[items[1]] = min_flag
            Side_set.append(items)

        elif (tag1 < 0 and tag2 < 0) and tag1 != tag2:
            #如果所属连通分量不同,让所有的下一组连通分量的flag等于上一组的
            max_flag = max(flag_set[items[0]], flag_set[items[1]])
            min_flag = min(flag_set[items[0]],flag_set[items[1]])
            flag_set[items[0]] = max_flag
            flag_set[items[1]] = max_flag
            for i in range(6):
                if flag_set[i] == min_flag:
                    flag_set[i] = max_flag
            Side_set.append(items)


sum_distance = 0
path_side = []

for i in range(len(Side_set)):
    sum_distance += Side_set[i][2]
    path_side.append((ref_dict[Side_set[i][0]],ref_dict[Side_set[i][1]]))

print("最短总距离:",sum_distance)
print("路径集合:")
print(path_side)