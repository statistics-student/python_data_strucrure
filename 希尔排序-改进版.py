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