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