"""
最长递增子序列
"""

while True:
    try:
        arr=list(map(int,input().split(',')))
        n=len(arr)
        lis_arr=[1]*n#每个位置当前最长递增子序列长度设为1
        if n==1:
            print(arr)
        else:
            for i in range(1,n):
                for j in range(0,i):
                    if arr[j]<=arr[i]:
                        lis_arr[i]=max(lis_arr[i],lis_arr[j]+1)
        """
        比较当前位置的递增子序列的长度和比较位置长度+1的最大长度
        """
            max_i=0
            max_value=lis_arr[0]
            for i in range(n):
                if lis_arr[i]>=max_value:
                    max_value=lis_arr[i]
                    max_i=i
            lis_out_arr=[arr[max_i]]
            for j in range(max_i,-1,-1):
                if lis_arr[j]==max_value-1:
                    max_value=lis_arr[j]
                    lis_out_arr.append(arr[j])
            print(lis_out_arr[::-1])
        """
        构造输出
        """
    except:
        break