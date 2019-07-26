'''
KMP算法相当于两个寻找Nextjarray列表的过程
'''
#nextjarray数组函数
def find_nextj(T_str):

    length = len(T_str)
    arr_start = [None for _ in range(length)]

    k = -1
    j = 0
    arr_start[j] = -1 #初始位置-1

    while j < length-1:
        #如果碰到相同字母+1
        if k == -1 or T_str[j] == T_str[k]:
            k += 1
            j += 1
            if T_str[j] != T_str[k]:
        #防止aaaa这种情况重复次数,相同字母nextj数组与前面相同
                arr_start[j] = arr_start[k]
            else:
                arr_start[j] = k
        else:
            k = arr_start[k]#遇到不同则回退
    return arr_start

def IndexKMP(obj_str,pattern_str):
    Nextjarray = find_nextj(pattern_str)
    i = 0
    j = 0
    length = len(pattern_str)
    while i < len(obj_str) and j < length:
        #第一个字母就不匹配时目标串后移一个位置,所以有'j == -1'
        if j == -1 or obj_str[i] == pattern_str[j]:
            i += 1
            j += 1
        else:
            j = Nextjarray[j]
    if j == length:
        print("匹配成功!匹配成功的位置是: {}".format(i - length))
    else:
        print("匹配失败!")

#Test
T_str = "aaabaaaab"

IndexKMP(T_str,"aaaa")