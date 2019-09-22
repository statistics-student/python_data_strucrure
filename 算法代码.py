360分金子.py
nums=int(input())
for j in range(1,nums+1):
    len_=int(input())
    arr=[int(i) for i in input().split()]
    A_list=[]
    B_list=[]
    def devide(role_list,arr):
        left=(max(arr[1],arr[-1])-arr[0])
        right=(max(arr[0],arr[-2])-arr[-1])
        if left<right:
            role_list.append(arr[0])
            arr=arr[1:]
        elif left>right:
            role_list.append(arr[-1])
            arr=arr[:-1]
        else:
            temp_l=arr[1:]
            if (max(temp_l[1],temp_l[-1])-temp_l[0])<(max(temp_l[0],temp_l[-2])-temp_l[-1]):
                max_l=max(temp_l[1],temp_l[-1])
            else:
                max_l=max(temp_l[0],temp_1[-2])
            temp_r=arr[:-1]
            if (max(temp_r[1],temp_r[-1])-temp_r[0])<(max(temp_r[0],temp_r[-2])-temp_r[-1]):
                max_r=max(temp_r[1],temp_r[-1])
            else:
                max_r=max(temp_r[0],temp_r[-2])
            if max_l>=max_r:
                role_list.append(arr[0])
                arr=arr[1:]
            else:
                role_list.append(arr[-1])
                arr=arr[:-1]
        return role_list,arr
    for i in range(len_):
        if len_-i>=3:
            if i%2==0:
                A_list,arr=devide(A_list,arr)
            else:
                B_list,arr=devide(B_list,arr)
        else:
            if i%2==0:
                A_list.append(max(arr))
                B_list.append(min(arr))
                break
            else:
                B_list.append(max(arr))
                A_list.append(min(arr))
                break
    print('Case #{}: {} {}'.format(j,sum(A_list),sum(B_list)))
======================================================
binary_search.py
'''
二分查找，返回下标
'''
def binary_search(arr,aim):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if aim==arr[mid]:
            return mid
        elif aim<arr[mid]:
            high=mid-1
        else:
            low=mid+1
    return None

if __name__=='__main__':
    arr=list(map(int,input().split()))
    aim=int(input())
    find_num=binary_search(arr,aim)
    if find_num!=None:
        print('找到了，下标是：{}'.format(find_num))
    else:
        print('该数不在列表里面!')
======================================================
Graph_class.py
class Graph:
    '''
    创建一个图的类
    '''
    '''
    mat邻接矩阵，vnum顶点的个数，unconn无关联时提供的值
    '''
    def __init__(self,mat,unconn=0):
        vnum=len(mat)
        for x in mat:
            if len(x)!=vnum:
                raise ValueError("Argument for 'Graph'.")
        self._mat=[mat[i][:] for i in range(vnum)]
        self._unconn=unconn
        self._vnum=vnum

    def vertex_num(self):
        return self._vnum
    '''
    当新增顶点时报错
    '''
    def _invalid(self,v):
        return 0 > v or v >= self._vnum
    def add_vertex(self):
        raise ValueError(
            "Adj-Matrix does not support 'add_vertex'."
        )
    '''
    添加一个边的权
    '''
    def add_edge(self,vi,vj,val=1):
        if self._invalid(vi) or self._invalid(vj):
            raise ValueError(str(vi)+'or'+str(vj)+
                             "is not a valid vertex.")
        self._mat[vi][vj]=val
    '''
    获得一个边的权
    '''
    def get_edge(self,vi,vj):
        if self._invalid(vi) or self._invalid(vj):
            raise ValueError(str(vi)+'or'+str(vj)+
                             "is not a valid vertex.")
        return self._mat[vi][vj]
    @staticmethod
    def _out_edges(row,unconn):
        edges=[]
        for i in  range(len(row)):
            if row[i]!=unconn:
                edges.append((i,row[i]))
        return edges
    '''
    获得出边的节点
    '''
    def out_edges(self,vi):
        if self._invalid(vi):
            raise ValueError(str(vi) +
                             "is not a valid vertex.")
        return self._out_edges(self._mat[vi],self._unconn)
    def __str__(self):
        return ",\n".join(map(str,self._mat))\
                +"\nUnconnected:"+str(self._unconn)
======================================================
KMP.py
'''
KMP算法相当于两个寻找Nextjarray列表的过程
'''
#nextjarray数组函数
def find_nextj(T_str):

    length = len(T_str)
    arr_start = [None for _ in range(length)]

    k = -1
    j = 0
    arr_start[j] = -1 #初始位置-1

    while j < length-1:
        #如果碰到相同字母+1
        if k == -1 or T_str[j] == T_str[k]:
            k += 1
            j += 1
            if T_str[j] != T_str[k]:
        #防止aaaa这种情况重复次数,相同字母nextj数组与前面相同
                arr_start[j] = arr_start[k]
            else:
                arr_start[j] = k
        else:
            k = arr_start[k]#遇到不同则回退
    return arr_start

def IndexKMP(obj_str,pattern_str):
    Nextjarray = find_nextj(pattern_str)
    i = 0
    j = 0
    length = len(pattern_str)
    while i < len(obj_str) and j < length:
        #第一个字母就不匹配时目标串后移一个位置,所以有'j == -1'
        if j == -1 or obj_str[i] == pattern_str[j]:
            i += 1
            j += 1
        else:
            j = Nextjarray[j]
    if j == length:
        print("匹配成功!匹配成功的位置是: {}".format(i - length))
    else:
        print("匹配失败!")

#Test
T_str = "aaabaaaab"

IndexKMP(T_str,"aaaa")
======================================================
select_sort.py
'''
选择排序
'''
def find_smallest(arr):
    smallest=arr[0]
    smallest_index=0
    for i in range(len(arr)):
        if smallest>arr[i]:
            smallest=arr[i]
            smallest_index=i
    return smallest_index

def select_sort(arr):
    new_arr=[]
    for i in range(len(arr)):
        small_est_index=find_smallest(arr)
        new_arr.append(arr[small_est_index])
        arr.pop(small_est_index)#pop传入位置
    return new_arr

if __name__=="__main__":
    arr=list(map(int,input().split()))
    print(select_sort(arr))
======================================================
乒乓球赛程安排-分治.py
n=int(input())
arr=list(range(1,n+1))
def days_d(arr):
    start_list=[]
    if len(arr)==2:
        start_list=[arr[1],arr[0]]
    if len(arr)>2:
        start_list=days_d(arr[0:len(arr)//2])+days_d(arr[len(arr)//2:])
    return start_list
def days_m(start_list):
    out_list=[]
    if len(start_list)<=4:
        for j in range(1,len(start_list)):
            if j==1:
                out_list.append(start_list)
            elif j==len(start_list)//2:
                out_list.append(sorted(start_list)[len(start_list)//2:]+sorted(start_list)[0:len(start_list)//2])
            else:
                out_list.append(out_list[len(start_list)-j-1][len(start_list)//2:]+out_list[len(start_list)-j-1][0:len(start_list)//2])
        return out_list
    else:
        out_list=[]
        mid_l=days_m(start_list[0:len(start_list)//2])
        mid_r=days_m(start_list[len(start_list)//2:])
        for i in range(len(start_list)//2-1):
            out_list.append(mid_l[i]+mid_r[i])
        out_list.append(sorted(start_list)[len(start_list)//2:]+sorted(start_list)[0:len(start_list)//2])
        for i in range(len(start_list)//2-1):
            out_list.append(mid_r[i]+mid_l[i])
        return out_list
days_m(days_d(arr))
n=int(input())
arr=list(range(1,n+1))
def days_d(arr):
    start_list=[]
    if len(arr)==2:
        start_list=[arr[1],arr[0]]
    if len(arr)>2:
        start_list=days_d(arr[0:len(arr)//2])+days_d(arr[len(arr)//2:])
    return start_list
def days_m(start_list):
    out_list=[]
    if len(start_list)<=4:
        for j in range(1,len(start_list)):
            if j==1:
                out_list.append(start_list)
            elif j==len(start_list)//2:
                out_list.append(sorted(start_list)[len(start_list)//2:]+sorted(start_list)[0:len(start_list)//2])
            else:
                out_list.append(out_list[len(start_list)-j-1][len(start_list)//2:]+out_list[len(start_list)-j-1][0:len(start_list)//2])
        return out_list
    else:
        out_list=[]
        mid_l=days_m(start_list[0:len(start_list)//2])
        mid_r=days_m(start_list[len(start_list)//2:])
        for i in range(len(start_list)//2-1):
            out_list.append(mid_l[i]+mid_r[i])
        out_list.append(sorted(start_list)[len(start_list)//2:]+sorted(start_list)[0:len(start_list)//2])
        for i in range(len(start_list)//2-1):
            out_list.append(mid_r[i]+mid_l[i])
        return out_list
out_=days_m(days_d(arr))
for i in range(0,n+1):
    for j in range(0,n):
        if i==0:
            if j==0:
                print('编号',end=' ')
            elif j==n-1:
                print('第%d天'%j,end='\n')
            else:
                print('第%d天'%j,end=' ')
        else:
            if j==0:
                print(i, end='     ')
            elif j==n-1:
                print(out_[j-1][i-1],end='\n')
            else:
                print(out_[j-1][i-1],end='    ')
======================================================
二叉树存储及遍历.py
'''
编一个程序，读入用户输入的一串先序遍历字符串，根据此字符串建立一个二叉树（以指针方式存储）。
例如如下的先序遍历字符串： ABC##DE#G##F### 其中“#”表示的是空格，空格字符代表空树。建立起此
二叉树以后，再对二叉树进行中序遍历，输出遍历结果。
example:
abc##de#g##f###
c b e g d f a 
'''

while True:
    try:
        str_list = list(input())[::-1]
        class BiTree(object):
            def __init__(self):
                self.data = "#"
                self.leftNode = None
                self.rightNode = None
        def CreateBiT(str_list):
            Temp = BiTree()
            if len(str_list) == 0:
                return Temp
            else:
                temp = str_list.pop()
                if temp == "#":
                    pass
                else:
                    Temp.data = temp
                    Temp.leftNode = CreateBiT(str_list)
                    Temp.rightNode = CreateBiT(str_list)
                return Temp
        def preorder(T):
            if T.data != "#":
                preorder(T.leftNode)
                print(T.data,end=" ")
                preorder(T.rightNode)
        preorder(CreateBiT(str_list))
    except:
        break
======================================================
冒泡排序.py
def mp_arrange(input_list):
	m=len(input_list)-1
	while m>=1:
		i=0
		while i<m:
			if input_list[i]>input_list[i+1]:
				bf=input_list[i]
				input_list[i]=input_list[i+1]
				input_list[i+1]=bf
			i+=1
		m-=1
	return(input_list)
======================================================
分土地.py
'''
分土地问题，将一块矩形土地均匀分为若干方形土地，
使得该小块方形土地是最大的能够分拆成的最大土地
'''
def devide(length,width):
    if length%width == 0:
        return width
    else:
        temp = length-length//width*width
        length = max(temp,width)
        width = min(temp,width)
        return devide(length,width)
======================================================
动态规划-背包问题.py
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
======================================================
华为-字符串重复输出.py
'''
华为编程：数字出现在字符串前面表示重复的次数
example：
abc3(A)
AAAcba
'''
while True:
    try:
        a=input()
        out_s=''
        zhan_=[]
        big_=0
        mid_=0
        small_=0
        for i in range(len(a)):
            if a[i].isalpha():
                if big_ == 0 and mid_ == 0 and small_ == 0:
                    out_s=out_s+a[i]
                else:
                    zhan_.append(a[i])
            if a[i].isnumeric():
                zhan_.append(a[i])
            if a[i]=='{':
                zhan_.append(a[i])
                big_+=1
            if a[i]=='[':
                zhan_.append(a[i])
                mid_+=1
            if a[i]=='(':
                zhan_.append(a[i])
                small_+=1
            if a[i]==')':
                if mid_==0:
                    str_temp=''
                    while len(zhan_)>0:
                        pop_=zhan_.pop()
                        if pop_.isalpha():
                            str_temp+=pop_
                        if pop_.isnumeric():
                            str_temp=int(pop_)*str_temp[::-1]
                        if pop_=='(':
                            small_-=1
                    out_s+=str_temp
                else:
                    zhan_.append(a[i])
            if a[i]==']':
                if big_==0:
                    str_temp=''
                    while len(zhan_)>0:
                        pop_=zhan_.pop()
                        if pop_.isalpha():
                            str_temp+=pop_
                        if pop_.isnumeric():
                            str_temp=int(pop_)*str_temp[::-1]
                        if pop_=='(':
                            small_-=1
                        if pop_==')':
                            pass
                        if pop_=='[':
                            mid_-=1
                    out_s += str_temp
                else:
                    zhan_.append(a[i])
            if a[i]=='}':
                str_temp = ''
                while len(zhan_) > 0:
                    pop_ = zhan_.pop()
                    if pop_.isalpha():
                        str_temp += pop_
                    if pop_.isnumeric():
                        str_temp= int(pop_) * str_temp[::-1]
                    if pop_ == '(':
                        small_ -= 1
                    if pop_ == ')':
                        pass
                    if pop_ == '[':
                        mid_ -= 1
                    if pop_ == ']':
                        pass
                    if pop_ =='{':
                        big_-=1
                out_s += str_temp
        out_s_T=''
        for i in sorted(out_s):
            out_s_T+=i
        out_s_T=out_s_T[::-1]
        for i in range(len(out_s_T)):
            if out_s_T[i].isupper():
                out_s_T=out_s_T[i:]+out_s_T[:i]
                break
        print(out_s_T)
    except:
        break




======================================================
华为数组题.py
'''
华为：第一行输入切割的长度
后面几行输入数组
轮流按长度切割数组加入一个大数组
like:
input:
3
1,2,3,4,5,6
1,2,3,4,5
out_put:
1,2,3,1,2,3,4,5,6,4,5
'''
while True:
    try:
        len_=int(input())
        arr=[]
        out_list=[]
        while True:
            s=input()
            if s!='':
                arr.append([int(i) for i in s.split(',')])
            else:
                break
        while True:
            for i in range(0,len(arr)):
                if len(arr[i])>=3:
                    for j in arr[i][0:3]:
                        out_list.append(j)
                    arr[i]=arr[i][3:]
                else:
                    for j in arr[i]:
                        out_list.append(j)
                    del arr[i]
            if len(arr) == 0:
                break
        for i in range(len(out_list)):
            if i !=len(out_list)-1:
                print(out_list[i],end=',')
            else:
                print(out_list[i])
    except:
        break
======================================================
回溯法-迷宫问题.py

deriction = [(0,-1),(0,1),(-1,0),(1,0)]#四个方向

stack = []#初始栈

def find_out(matrix,start_position,end_position):
    if start_position == end_position:
        stack.append(end_position)
        print(stack)
        return True
    matrix[start_position[0]][start_position[1]] = 2#访问过的标记为2
    stack.append(start_position)#访问的进栈
    while len(stack) > 0:
        find_eps = False#标志是否四个方向都不可走
        start_position = stack[-1]#每次读取栈顶
        for i in range(4):
            try:
                next_position = start_position[0] + deriction[i][0],start_position[1] + deriction[i][1]#防止下越界
            except:
                continue
            if next_position[0] < 0 or next_position[1] < 0:#防止上越界
                continue
            if next_position == end_position:
                stack.append(end_position)
                print(stack)
                return True
            elif matrix[next_position[0]][next_position[1]] == 0:
                find_eps = True#方向走通就改变状态
                matrix[next_position[0]][next_position[1]] = 2
                stack.append(next_position)
                break
        if find_eps == False:
            stack.pop()#方向走不通就出栈
    return False

'''
测试
'''
matrix = [[1,0,0,1,0,1,0],[0,0,0,1,1,1,1],[0,1,1,0,0,0,0],[0,0,0,1,0,1,1],[1,1,0,0,0,1,1]]

if find_out(matrix,(0,2),(2,6)):
    print('success!')
else:
    print('fail!')

======================================================
子数组最大和.py
'''
求当前序列的子序列和的最大值，例如：
1，-2，3，10，-4，7，2，-5的
最大子序列为3，10，-4，7，2，最大和为18，
要求时间复杂度为O(n)
'''
while True:
    try:
        if len(arr)==1:
            print(arr[0])
        else:
            Max=arr[0]#记录当前最大值
            Max_=arr[0]#记录连接最大值
            for i in arr[1:]:
                '''根据加减之后的大小判断是否截断之前的连接'''
                if Max_+i>i:
                    Max_=Max_+i
                    Max=max(Max,Max_)
                else:
                    Max_=i
                    Max=max(Max,i)
            print(Max)
    except:
        break

======================================================
希尔排序-改进版.py
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 12:20:18 2019

@author: Lenovo
"""

def sort_xier1(arr1):
    len_arr1=len(arr1)
    intervel=len(arr1)//3+1
    while intervel>1:
        arr_blank=[]
        index_blank=[]
        for k in range(0,intervel):
            m=k
            while k<=len_arr1-1:
                arr_blank.append(arr1[k])
                index_blank.append(k)
                k=k+intervel
                #print('k-',k)
            arr_blank.sort()
            for i,j in zip(index_blank,arr_blank):
                arr1[i]=j
            arr_blank=[]
            index_blank=[]
        #print(arr1)
        intervel=intervel//3+1
    arr1.sort()
    return(arr1)
    
start=time.time()
sort_xier1(e)
print(time.time()-start)
======================================================
希尔排序-未改进.py
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 22:08:49 2019

@author: Lenovo
"""

def sort_xier(arr1):
    def sort_insert(arr2):
        i=0
        for j in range(1,len(arr2)):
            a=arr2[j]
            while i>=0:
                if a>=arr2[i]:
                    arr2[i+1]=a
                    break
                else:
                    arr2[i+1]=arr2[i]
                    arr2[i]=a
                i=i-1
            i=j
        return(arr2)
    len_arr1=len(arr1)
    intervel=len(arr1)//3+1
    while intervel>1:
        arr_blank=[]
        index_blank=[]
        for k in range(0,intervel):
            m=k
            while k<=len_arr1-1:
                arr_blank.append(arr1[k])
                index_blank.append(k)
                k=k+intervel
                #print('k-',k)
            sort_insert(arr_blank)
            for i,j in zip(index_blank,arr_blank):
                arr1[i]=j
            arr_blank=[]
            index_blank=[]
        #print(arr1)
        intervel=intervel//3+1
    sort_insert(arr1)
    return(arr1)

start=time.time()
sort_xier(e)
print(time.time()-start)

start=time.time()
e.sort()
print(time.time()-start)
======================================================
广义优先遍历-岛屿个数.py
'''
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。
输入:
11110
11010
11000
00000

输出: 1

输入:
11000
11000
00100
00011

输出: 3
'''


from queue import Queue
class Solution:
    def numIslands(self,grid):
        nums=0
        q=Queue()
        while True:
            exist = False
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j]=="1":
                        q.put((i,j))
                        grid[i][j]="0"
                        nums+=1
                        exist=True
                        break
                if exist:
                    break

            if exist==False:
                break
            while not q.empty():
                u=q.get()
                if u[0]+1<=len(grid)-1:
                    if grid[u[0]+1][u[1]]=="1":
                        q.put((u[0]+1,u[1]))
                        grid[u[0] + 1][u[1]]="0"
                if u[0]-1>=0:
                    if grid[u[0]-1][u[1]]=="1":
                        q.put((u[0]-1,u[1]))
                        grid[u[0]-1][u[1]]="0"
                if u[1]+1<=len(grid[0])-1:
                    if grid[u[0]][u[1]+1]=="1":
                        q.put((u[0],u[1]+1))
                        grid[u[0]][u[1]+1]="0"
                if u[1]-1>=0:
                    if grid[u[0]][u[1]-1]=="1":
                        q.put((u[0],u[1]-1))
                        grid[u[0]][u[1]-1]="0"
        print(nums)
sol=Solution()
grid=[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]

sol.numIslands(grid)

======================================================
广度优先遍历.py
from queue import Queue

def bfs(graph,node):
    visted=set()
    visted.add(node)
    q=Queue()
    q.put(node)
    while not q.empty():
        u=q.get()
        print(u)
        for v in graph.get(u):
            if v not in visted:
                visted.add(v)
                q.put(v)


graph = {1: [2,3], 2: [1, 4,5], 3: [1,6], 4: [2],5:[2],6:[3]}
bfs(graph, 2)



======================================================
循环队列.py
"""
设计你的循环队列实现。 循环队列是一种线性数据结构，其操作表现基于 FIFO（先进先出）原则并且队尾被连接在队首之后以形成一个循环。它也被称为“环形缓冲器”。

循环队列的一个好处是我们可以利用这个队列之前用过的空间。在一个普通队列里，一旦一个队列满了，我们就不能插入下一个元素，即使在队列前面仍有空间。但是使用循环队列，我们能使用这些空间去存储新的值。

你的实现应该支持如下操作：

MyCircularQueue(k): 构造器，设置队列长度为 k 。
Front: 从队首获取元素。如果队列为空，返回 -1 。
Rear: 获取队尾元素。如果队列为空，返回 -1 。
enQueue(value): 向循环队列插入一个元素。如果成功插入则返回真。
deQueue(): 从循环队列中删除一个元素。如果成功删除则返回真。
isEmpty(): 检查循环队列是否为空。
isFull(): 检查循环队列是否已满。
实例：
MyCircularQueue circularQueue = new MycircularQueue(3); // 设置长度为 3

circularQueue.enQueue(1);  // 返回 true

circularQueue.enQueue(2);  // 返回 true

circularQueue.enQueue(3);  // 返回 true

circularQueue.enQueue(4);  // 返回 false，队列已满

circularQueue.Rear();  // 返回 3

circularQueue.isFull();  // 返回 true

circularQueue.deQueue();  // 返回 true

circularQueue.enQueue(4);  // 返回 true

circularQueue.Rear();  // 返回 4
"""


class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.length = k
        self.rear = -1
        self.front = -1
        self.array = [None] * k

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.rear < self.length - 1:
            if self.rear == -1:
                self.array[self.rear + 1] = value
                self.rear += 1
                self.front += 1
                return True
            else:
                if self.array[self.rear + 1] != None:
                    return False
                else:
                    self.array[self.rear + 1] = value
                    self.rear += 1
                    return True
        else:
            if self.array[0] == None:
                self.rear = 0
                self.array[self.rear] = value
                return True
            else:
                return False

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.front == -1:
            return False
        else:
            self.array[self.front] =None
            if self.front + 1 == self.length:
                if self.array[0] != None:
                    self.front = 0
                else:
                    self.front = -1
                    self.rear = -1
            else:
                if self.array[self.front + 1] != None:
                    self.front += 1
                else:
                    self.front = -1
                    self.rear = -1
            return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        else:
            return self.array[self.front]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        else:
            return self.array[self.rear]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if self.rear == -1:
            return True
        else:
            return False

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if self.rear == self.length - 1 and self.front == 0:
            return True
        else:
            if self.front - self.rear == 1:
                return True
            else:
                return False

======================================================
快速排序.py
'''
快速排序版本1，思想简单费空间
'''
def quicksort_1(arr):
    if len(arr) < 2:
        return arr
    else:
        arr_len = len(arr)
        mid = len(arr)//2
        temp = arr[mid]
        left = []
        right = []
        for i in range(arr_len):
            if i == mid:
                pass
            else:
                if arr[i] <= temp:
                    left.append(arr[i])
                else:
                    right.append(arr[i])
        return quicksort_1(left) + [temp] + quicksort_1(right)

'''
快排版本2，占用空间更小
'''
def quicksort_2(arr):
    #每一次排序的移动操作
    def quickmove(arr,low,hight):
        left = low
        right = hight
        temp = arr[left]
        #left左侧始终小于right右侧
        while left < right:
            while left < right:
                if arr[right] >= temp:
                    right -= 1
                else:
                    #遇到小于基准的数移到左侧
                    arr[left] = arr[right]
                    break
            while left < right:
                if arr[left] <= temp:
                    left += 1
                else:
                    arr[right] = arr[left]
                    break
        arr[left] = temp
        return left
    #递归多趟排序
    def quicksort(arr,low,hight):
        if low < hight:
            left = quickmove(arr,low,hight)
            quicksort(arr,low,left-1)
            quicksort(arr,left+1,hight)    
    if len(arr) < 2:
        return arr
    else:
        low = 0
        hight = len(arr) - 1
        quicksort_2(arr,low,hight)
        return arr
======================================================
快速排序动图展示.py
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













======================================================
插入排序.py
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def sort_insert(arr):
    i=0
    for j in range(1,len(arr)):
        a=arr[j]
        while i>=0:
            if a>=arr[i]:
                arr[i+1]=a
                break
            else:
                arr[i+1]=arr[i]
                arr[i]=a
            i=i-1
        i=j
    return(arr)
                
e=np.random.randint(-100000,100000,1000000)
start=time.time()
sort_insert(e)
print(time.time()-start)
======================================================
携程-求解唯一解的方程组.py
while True:
    try:
        X_=eval(input())
        Y_=eval(input())
        def solve_fx(x,y):
            #正求解
            r_len=len(x)
            c_len=len(x[0])
            i,j=0,0
            while True:
                if x[i][j]==0:
                    for k in range(1,len(x)):
                        if x[k][j]!=0:
                            x[i],x[k]=x[k],x[i]
                            y[i],y[k]=y[k],y[j]
                c_num_1=x[i][j]
                for p in range(i+1,r_len):
                    c_num_2=(-x[p][j])
                    y[p]=y[p]+y[i]*(c_num_2)/c_num_1
                    for q in range(j,c_len):
                        x[p][q]=x[p][q]+x[i][q]*c_num_2/c_num_1
                i+=1
                j+=1
                if j==c_len-1:
                    break
            #逆求解
            remain_x=[]
            remain_y=[]
            for k in range(r_len):
                if x[k].count(0)!=c_len:
                    remain_x.append(x[k])
                    remain_y.append(y[k])
            x=remain_x[:c_len]
            y=remain_y[:c_len]
            i,j=len(x)-1,c_len-1
            while True:
                c_num_1=x[i][j]
                for p in range(i-1,-1,-1):
                    c_num_2=-x[p][j]
                    x[p][j]=0
                    y[p]=y[p]+y[i]*c_num_2/c_num_1
                i-=1
                j-=1
                if i==0:
                    break
            out_list=[y[i]/x[i][i] for i in range(len(x))]
            return [i if len(str(i)[2:])<=5 else round(i,5) for i in out_list]
        print(solve_fx(X_,Y_))
    except:
        break
======================================================
最小生成树-Kruskal算法.py
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
======================================================
最小生成树-prime算法.py
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

======================================================
最短路径-Dijkstra算法.py
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

======================================================
最长递增子序列.py
"""
最长递增子序列
"""

while True:
    try:
        arr=list(map(int,input().split(',')))
        n=len(arr)
        lis_arr=[1]*n#每个位置当前最长递增子序列长度设为1
        if n==1:
            print(arr)
        else:
            for i in range(1,n):
                for j in range(0,i):
                    if arr[j]<=arr[i]:
                        lis_arr[i]=max(lis_arr[i],lis_arr[j]+1)
        """
        比较当前位置的递增子序列的长度和比较位置长度+1的最大长度
        """
            max_i=0
            max_value=lis_arr[0]
            for i in range(n):
                if lis_arr[i]>=max_value:
                    max_value=lis_arr[i]
                    max_i=i
            lis_out_arr=[arr[max_i]]
            for j in range(max_i,-1,-1):
                if lis_arr[j]==max_value-1:
                    max_value=lis_arr[j]
                    lis_out_arr.append(arr[j])
            print(lis_out_arr[::-1])
        """
        构造输出
        """
    except:
        break
======================================================
深度优先遍历.py
def dfs(graph, start):
    visted=set()
    stack=[[start,0]]
    print(start)
    while stack:
        (v,next_node_idx)=stack[-1]
        if v not in graph or next_node_idx>=len(graph[v]):
            stack.pop()
            continue
        next_node=graph[v][next_node_idx]
        stack[-1][1]+=1
        if next_node not in visted:
            visted.add(next_node)
            print(next_node)
            stack.append([next_node,0])

graph = {1: [2, 3], 2: [4, 5], 3: [6]}
dfs(graph, 1)

======================================================
百度乘法表.py
while 1:
    s=input()
    if s!='':
        nums=s.split()
        n=int(nums[0])
        m=int(nums[1])
        k=int(nums[2])
        start_list=set()
        out_list=[]
        for i in range(1,n+1):
            for j in range(1,m+1):
                start_list.add(i*j)
        temp=0
        o_temp=0
        for i in start_list:
            for j in range(1,n+1):
                temp=temp+i//j
            out_list+=[i]*(temp-o_temp)
            o_temp=temp
            temp=0
        print(out_list[k-1])
    else:
        break
======================================================
百度行数转换.py
while 1:
    s=input()
    trans_dict={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,
               'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,
                'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,
                'V':22,'W':23,'X':24,'Y':25,'Z':26}
    trans_dict_t={1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',
               9:'I',10:'J',11:'K',12:'L',13:'M',14:'N',15:'O',
                16:'P',17:'Q',18:'R',19:'S',20:'T',21:'U',
                22:'V',23:'W',24:'X',25:'Y',26:'Z'}
    if s!='':
        nums=int(s)
        for i in range(0,nums):
            s1=input()
            test=''
            for i in s1:
                if i.isalpha():
                    test+=i
                else:
                    break
            if len(test)>1:
                cloumns=0
                trans_num=0
                for i in test[::-1]:
                    cloumns+=trans_dict[i]*(26**(trans_num))
                    trans_num+=1
                print('R'+s1[len(test):]+'C'+str(cloumns))
            else:
                if test=='R' and ('C' in s1):
                    rows=s1[1:].split('C')[0]
                    columns=int(s1[1:].split('C')[1])
                    columns_str=''
                    if columns<=26:
                        columns_str+=trans_dict_t[columns]
                    else:
                        while columns>26:
                            mod=columns%26
                            if mod!=0:
                                columns_str+=trans_dict_t[mod]
                            columns=columns//26
                        columns_str+=trans_dict_t[columns]
                    print(columns_str[::-1]+rows)
                else:
                    print('R'+s1[1:]+'C'+str(trans_dict[s1[1]]))
    else:
        break
======================================================
腾讯-最大回文数.py
def lcs(x,y):
    x_len=len(x)
    y_len=len(y)
    web=[[0 for i in range(x_len+1)] for i in range(y_len+1)]
    out_str=''
    r_local=[]
    c_local=[]
    for i in range(1,y_len+1):
        for j in range(1,x_len+1):
            if y[i-1]==x[j-1]:
                web[i][j]=web[i-1][j-1]+1 
            else:
                web[i][j]=max(web[i-1][j],web[i][j-1])
    return web

def print_lcs(web,x,y,x_len,y_len):
    s=''
    while (x_len>=0 and y_len>=0):
        if x[x_len]==y[y_len]:
            s=s+x[x_len]
            x_len=x_len-1
            y_len=y_len-1
        else:
            if web[y_len][x_len+1]>=web[y_len+1][x_len]:
                y_len=y_len-1
            else:
                x_len=x_len-1
    return s[::-1]
======================================================
腾讯打印最小数.py
def f(arr,k):
    start_time=time.time()
    arr=sorted(set(arr))
    if len(arr)==1 and arr[0]==0:
        print(0)
    else:
        if arr[0]==0:
            arr=arr[1:]
        len_=len(arr)
        start=0
        for i in range(k):
            print(arr[i]-start)
            start=arr[i]
            if i+1==len_:
                break
        print(time.time()-start_time)
======================================================
迷宫问题.py
'''
迷宫问题
0表示可以到达
1表示不可以到达
'''

from queue import Queue

while True:
    try:
        '''
        读取数据
        '''
        m,n=map(int,input().split())
        arr=[]
        for i in range(m):
            arr.append(list(map(int,input().split())))
        start=tuple(map(int,input().split()))
        end=tuple(map(int,input().split()))

        dirs=[(0,1),(1,0),(0,-1),(-1,0)]#探索方向
        path=[]#路径列表

        def mark(arr,pos):#标记到过的路径
            arr[pos[0]][pos[1]]='#'

        def passable(arr,pos):#该点能到则返回0
            try:
                return arr[pos[0]][pos[1]]==0
            except:
                return False#越界不执行

        def arr_solver_queue(arr, start, end):
            path.append(start)
            if start == end:
                print("true")
                return
            qu = Queue()#建立探索方向队列
            mark(arr, start)
            qu.put(start)
            while not qu.empty():
                pos = qu.get()
                for i in range(4):
                    nextp = pos[0] + dirs[i][0], pos[1] + dirs[i][1]#下一个探索位置
                    if nextp[0]<0 or nextp[1]<0:#越界不执行
                        continue
                    if nextp[0]<5 and nextp[1]<5:
                        path.append(nextp)#越界不添加
                    if passable(arr, nextp):
                        if nextp == end:
                            print("ture")
                            path.append(end)
                            print('尝试过的点:\n',path)
                            return
                        mark(arr, nextp)
                        qu.put(nextp)
            print('尝试过的点:\n',path)
            print("false")

        arr_solver_queue(arr,start,end)
    except:
        break
======================================================
