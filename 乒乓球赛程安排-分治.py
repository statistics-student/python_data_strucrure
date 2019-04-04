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