'''
求当前序列的子序列和的最大值，例如：
1，-2，3，10，-4，7，2，-5的
最大子序列为3，10，-4，7，2，最大和为18，
要求时间复杂度为O(n)
'''
while True:
    try:
        if len(arr)==1:
            print(arr[0])
        else:
            Max=arr[0]#记录当前最大值
            Max_=arr[0]#记录连接最大值
            for i in arr[1:]:
                '''根据加减之后的大小判断是否截断之前的连接'''
                if Max_+i>i:
                    Max_=Max_+i
                    Max=max(Max,Max_)
                else:
                    Max_=i
                    Max=max(Max,i)
            print(Max)
    except:
        break
