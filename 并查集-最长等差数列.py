# coding=utf-8

"""
并查集
找到连续最长等差数列
"""

class Solution:
    def __init__(self):
        self.longest_arr = []
    def longestlist(self,arr):
        ans = 0
        s = set(arr)
        for item in arr:
            temp = []
            if item in s:
                s.discard(item)
                temp.append(item)
                cnt = 1
                right = item + 1
                left = item - 1
                while right in s:
                    s.discard(right)
                    temp.append(right)
                    right += 1
                    cnt += 1
                while left in s:
                    s.discard(left)
                    temp = [left] + temp
                    left = left - 1
                    cnt += 1
                if ans < cnt:
                    ans = cnt
                    self.longest_arr = temp
        return ans

arr = [100,4,98,2,99,3,1,55,7,8,9,10,11,12]
result = Solution()
print(result.longestlist(arr))

print(result.longest_arr)
