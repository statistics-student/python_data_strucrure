# coding=utf-8

import numpy as np
######################################################
def insert_sort(arr):
    """插入排序"""
    if len(arr) == 1:
        return arr
    for i in range(1,len(arr)):
        j = i
        key = i - 1
        while key >= 0:
            if arr[j] >= arr[key]:
                arr[key + 1] = arr[j]
                break
            else:
                temp = arr[j]
                arr[j] = arr[key]
                arr[key] = temp
                j -= 1
                key -= 1
    return arr
#######################################################
def merge_sort(arr):
    """归并排序"""
    def merge(left,right):
        """归并函数"""
        i, j = 0, 0
        result = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result
    def mer_sort(small_arr):
        """递归函数"""
        if len(small_arr) == 1:
            return small_arr
        else:
            mid = len(small_arr) // 2
            left = mer_sort(small_arr[:mid])
            right = mer_sort(small_arr[mid:])
            return merge(left,right)
    return mer_sort(arr)
###########################################################
def quick_sort(arr,left,right):
    """快速排序"""
    if left >= right:
        return arr
    low = left
    high = right
    key = arr[left]
    while left < right:
        while left < right and arr[right] >= key:
            right -= 1
        arr[left] = arr[right]
        while left < right and arr[left] <= key:
            left += 1
        arr[right] = arr[left]
    arr[left] = key
    quick_sort(arr,low,left - 1)
    quick_sort(arr,left + 1, high)
    return arr
######################################################
def shell_sort(arr):
    """希尔排序"""
    len_ = len(arr)
    key = len_ // 2
    while key >= 1:
        for i in range(key):
            j = i + key
            while j < len_:
                flag = j - key
                while flag >= 0:
                    if arr[j] >= arr[flag]:
                        arr[flag + key] = arr[j]
                        break
                    else:
                        temp = arr[j]
                        arr[j] = arr[flag]
                        arr[flag] = temp
                        j -= key
                        flag -= key
                j += key
        key //= 2
    return arr
#############################################################
def heap_sort(arr):
    """堆排序"""
    def adjust_heap(arr,i,size):
        lchild = 2 * i + 1
        rchild = 2 * i + 2
        max_index = i
        if i <= size // 2:
            if lchild < size and arr[lchild] > arr[max_index]:
                max_index = lchild
            if rchild < size and arr[rchild] > arr[max_index]:
                max_index = rchild
            if max_index != i:
                arr[i], arr[max_index] = arr[max_index], arr[i]
                adjust_heap(arr,max_index,size)
    def build_heap(arr,size):
        for i in range(size//2,-1,-1):
            adjust_heap(arr,i,size)
    size = len(arr)
    build_heap(arr,size)
    for i in range(size - 1,-1,-1):
        arr[0], arr[i] = arr[i], arr[0]
        adjust_heap(arr,0,i)
    return arr
#############################################################
import math
def radix_sort(arr):
    """基数排序"""
    radix = 10
    k = math.ceil(math.log(max(arr), radix))
    bucket = [[] for _ in range(radix)]
    for i in range(1, k + 1):
        for j in arr:
            bucket[j // (radix**(i - 1)) % radix].append(j)
        del arr[::]
        for m in bucket:
            arr += m
            del m[::]
        bucket = [[] for _ in range(radix)]
    return arr

arr = list(np.random.randint(1,130,10))

"""
start1 = time.time()
print(merge_sort(arr))
end1 = time.time()
print("merge_sort time : ",end1-start1)

start2 = time.time()
print(sorted(arr))
end2 = time.time()
print("sorted time : ",end2-start2)
"""
print(arr)
print(heap_sort(arr))
