'''
动态规划背包问题
max_weigth: 10
N:5
重量W分别为:
2 2 6 5 4
价值W分别为:
6 3 5 4 6

[[6, 6, 6, 6, 6, 6, 6, 6, 6], 
[6, 6, 9, 9, 9, 9, 9, 9, 9], 
[6, 6, 9, 9, 9, 9, 11, 11, 14], 
[6, 6, 9, 9, 9, 10, 11, 13, 14], 
[6, 6, 9, 9, 12, 12, 15, 15, 15]]
'''

arr_W = [2,2,6,5,4]#各物品重量
arr_value = [6,3,5,4,6]#各物品价值


max_weight = 10
n = 5

min_w = min(arr_W)#最轻的那个物品重量
martix_value = []

#初始化
for i in range(n):
    martix_value.append([0]*(max_weight + 1 - min_w))
#如果能够承受该物品重量则加入价值否则为0
martix_value[0] = [arr_value[0] if i >= arr_W[0] else 0 for i in range(min_w,max_weight + 1)]

for i in range(1,n):
    for j in range(min_w,max_weight + 1):#最小值 == martix_value最小下标0 + min_w
        temp_w = j - arr_W[i] #新的袋子多余的重量
        # 多余的重量如果小于min_w，则该列该行最大价值等于现加入物品价值+ 0
        if temp_w < min_w:
            temp_value = arr_value[i] + 0#下标差了min_w，上面有解释
        else:
            #否则价值就等于现加入物品价值+上一行多余重量处的价值
            temp_value = arr_value[i] + martix_value[i-1][temp_w-min_w]#下标差了min_w，上面有解释
        #最终最大值等于上一行和这一行temp_value的值的最大值
        martix_value[i][j-min_w] = max(temp_value,martix_value[i-1][j-min_w])

max_value = martix_value[-1][-1]

select_set = []#最终背包里面的物品重量集合


i = n - 1
now_weight = max_weight
while i > 0:
    if martix_value[i][now_weight-min_w] > martix_value[i-1][now_weight-min_w]:
        select_set.append((i+1,arr_W[i]))
        now_weight = now_weight - arr_W[i]
        i -= 1
    else:
        i -= 1
if now_weight >= arr_W[0]:
    select_set.append((1,arr_W[0]))

print("最大重量：",max_value)
print("最终选择物品重量集：","\n",select_set)
print("状态转移矩阵：","\n",martix_value)