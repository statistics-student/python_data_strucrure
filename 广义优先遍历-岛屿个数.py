'''
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。
输入:
11110
11010
11000
00000

输出: 1

输入:
11000
11000
00100
00011

输出: 3
'''


from queue import Queue
class Solution:
    def numIslands(self,grid):
        nums=0
        q=Queue()
        while True:
            exist = False
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j]=="1":
                        q.put((i,j))
                        grid[i][j]="0"
                        nums+=1
                        exist=True
                        break
                if exist:
                    break

            if exist==False:
                break
            while not q.empty():
                u=q.get()
                if u[0]+1<=len(grid)-1:
                    if grid[u[0]+1][u[1]]=="1":
                        q.put((u[0]+1,u[1]))
                        grid[u[0] + 1][u[1]]="0"
                if u[0]-1>=0:
                    if grid[u[0]-1][u[1]]=="1":
                        q.put((u[0]-1,u[1]))
                        grid[u[0]-1][u[1]]="0"
                if u[1]+1<=len(grid[0])-1:
                    if grid[u[0]][u[1]+1]=="1":
                        q.put((u[0],u[1]+1))
                        grid[u[0]][u[1]+1]="0"
                if u[1]-1>=0:
                    if grid[u[0]][u[1]-1]=="1":
                        q.put((u[0],u[1]-1))
                        grid[u[0]][u[1]-1]="0"
        print(nums)
sol=Solution()
grid=[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]

sol.numIslands(grid)
