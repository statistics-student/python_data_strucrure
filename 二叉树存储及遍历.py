'''
编一个程序，读入用户输入的一串先序遍历字符串，根据此字符串建立一个二叉树（以指针方式存储）。
例如如下的先序遍历字符串： ABC##DE#G##F### 其中“#”表示的是空格，空格字符代表空树。建立起此
二叉树以后，再对二叉树进行中序遍历，输出遍历结果。
example:
abc##de#g##f###
c b e g d f a 
'''

while True:
    try:
        str_list = list(input())[::-1]
        class BiTree(object):
            def __init__(self):
                self.data = "#"
                self.leftNode = None
                self.rightNode = None
        def CreateBiT(str_list):
            Temp = BiTree()
            if len(str_list) == 0:
                return Temp
            else:
                temp = str_list.pop()
                if temp == "#":
                    pass
                else:
                    Temp.data = temp
                    Temp.leftNode = CreateBiT(str_list)
                    Temp.rightNode = CreateBiT(str_list)
                return Temp
        def preorder(T):
            if T.data != "#":
                preorder(T.leftNode)
                print(T.data,end=" ")
                preorder(T.rightNode)
        preorder(CreateBiT(str_list))
    except:
        break