def f(arr,k):
    start_time=time.time()
    arr=sorted(set(arr))
    if len(arr)==1 and arr[0]==0:
        print(0)
    else:
        if arr[0]==0:
            arr=arr[1:]
        len_=len(arr)
        start=0
        for i in range(k):
            print(arr[i]-start)
            start=arr[i]
            if i+1==len_:
                break
        print(time.time()-start_time)