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