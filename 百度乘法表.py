while 1:
    s=input()
    if s!='':
        nums=s.split()
        n=int(nums[0])
        m=int(nums[1])
        k=int(nums[2])
        start_list=set()
        out_list=[]
        for i in range(1,n+1):
            for j in range(1,m+1):
                start_list.add(i*j)
        temp=0
        o_temp=0
        for i in start_list:
            for j in range(1,n+1):
                temp=temp+i//j
            out_list+=[i]*(temp-o_temp)
            o_temp=temp
            temp=0
        print(out_list[k-1])
    else:
        break