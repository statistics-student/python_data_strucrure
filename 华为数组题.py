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