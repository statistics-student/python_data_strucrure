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