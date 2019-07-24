
deriction = [(0,-1),(0,1),(-1,0),(1,0)]#四个方向

stack = []#初始栈

def find_out(matrix,start_position,end_position):
    if start_position == end_position:
        stack.append(end_position)
        print(stack)
        return True
    matrix[start_position[0]][start_position[1]] = 2#访问过的标记为2
    stack.append(start_position)#访问的进栈
    while len(stack) > 0:
        find_eps = False#标志是否四个方向都不可走
        start_position = stack[-1]#每次读取栈顶
        for i in range(4):
            try:
                next_position = start_position[0] + deriction[i][0],start_position[1] + deriction[i][1]#防止下越界
            except:
                continue
            if next_position[0] < 0 or next_position[1] < 0:#防止上越界
                continue
            if next_position == end_position:
                stack.append(end_position)
                print(stack)
                return True
            elif matrix[next_position[0]][next_position[1]] == 0:
                find_eps = True#方向走通就改变状态
                matrix[next_position[0]][next_position[1]] = 2
                stack.append(next_position)
                break
        if find_eps == False:
            stack.pop()#方向走不通就出栈
    return False

'''
测试
'''
matrix = [[1,0,0,1,0,1,0],[0,0,0,1,1,1,1],[0,1,1,0,0,0,0],[0,0,0,1,0,1,1],[1,1,0,0,0,1,1]]

if find_out(matrix,(0,2),(2,6)):
    print('success!')
else:
    print('fail!')
