# -*- coding:utf-8 -*-
class Solution:

    '''
    说明：此中方法其实在python中严格意义上说是不适用的,在c/c++中存在在原字符串上操作的情况，从右向左插入字符串移动元素
    https://blog.csdn.net/Yeoman92/article/details/77865878?locationNum=8&fps=1
    '''
    def replaceSpace(self, oldString):
        return oldString
    # 创建一个新空间，从左向右遍历，遇到空格，则在新的字符串后追加"%20"
    # 这样无需考虑字符串移动问题，直接在新的空间操作即可
    def repaceSpaceFirst(self, oldString):
        newString = ""
        for c in oldString:
            if c == " ":
                newString += "%20"
            else:
                newString += c
        return newString
    # 使用python的字符串方法
    def replaceSpaceSecond(self, oldString):
        return oldString.replace(" ", "%20")

    # 把原字符串分割为片段，使用"%20"连接各个字符串
    def replaceSpaceThird(self, oldString):
        return "%20".join(oldString.split(" "))

solution = Solution()
print solution.repaceSpaceFirst("I will be successed!")
print solution.replaceSpaceSecond("Go Go Go !")
print solution.replaceSpaceThird("Must Will Cool!")