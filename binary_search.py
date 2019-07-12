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