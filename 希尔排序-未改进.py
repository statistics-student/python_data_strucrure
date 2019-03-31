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