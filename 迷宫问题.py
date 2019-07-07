'''
迷宫问题
0表示可以到达
1表示不可以到达
'''

from queue import Queue

while True:
    try:
        '''
        读取数据
        '''
        m,n=map(int,input().split())
        arr=[]
        for i in range(m):
            arr.append(list(map(int,input().split())))
        start=tuple(map(int,input().split()))
        end=tuple(map(int,input().split()))

        dirs=[(0,1),(1,0),(0,-1),(-1,0)]#探索方向
        path=[]#路径列表

        def mark(arr,pos):#标记到过的路径
            arr[pos[0]][pos[1]]='#'

        def passable(arr,pos):#该点能到则返回0
            try:
                return arr[pos[0]][pos[1]]==0
            except:
                return False#越界不执行

        def arr_solver_queue(arr, start, end):
            path.append(start)
            if start == end:
                print("true")
                return
            qu = Queue()#建立探索方向队列
            mark(arr, start)
            qu.put(start)
            while not qu.empty():
                pos = qu.get()
                for i in range(4):
                    nextp = pos[0] + dirs[i][0], pos[1] + dirs[i][1]#下一个探索位置
                    if nextp[0]<0 or nextp[1]<0:#越界不执行
                        continue
                    if nextp[0]<5 and nextp[1]<5:
                        path.append(nextp)#越界不添加
                    if passable(arr, nextp):
                        if nextp == end:
                            print("ture")
                            path.append(end)
                            print('尝试过的点:\n',path)
                            return
                        mark(arr, nextp)
                        qu.put(nextp)
            print('尝试过的点:\n',path)
            print("false")

        arr_solver_queue(arr,start,end)
    except:
        break