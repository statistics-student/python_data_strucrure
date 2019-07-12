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