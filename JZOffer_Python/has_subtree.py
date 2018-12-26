# -*- coding:utf-8 -*-
'''
题目描述：
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
'''
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:

    '''
    递归的思想
    链接：https://www.nowcoder.com/questionTerminal/6e196c44c7004d15b1610b9afca8bd88
    思路：参考剑指offer
    1、首先设置标志位result = false，因为一旦匹配成功result就设为true，
       剩下的代码不会执行，如果匹配不成功，默认返回false
    2、递归思想，如果根节点相同则递归调用DoesTree1HaveTree2（），
       如果根节点不相同，则判断tree1的左子树和tree2是否相同，
       再判断右子树和tree2是否相同
    3、注意null的条件，HasSubTree中，如果两棵树都不为空才进行判断，
    DoesTree1HasTree2中，如果Tree2为空，则说明第二棵树遍历完了，即匹配成功，
    tree1为空有两种情况（1）如果tree1为空&&tree2不为空说明不匹配，
    （2）如果tree1为空，tree2为空，说明匹配。
    '''
    def HasSubtree(self, pRoot1, pRoot2):
        result = False
        # 当Tree1和Tree2都不为零的时候，才进行比较。否则直接返回false
        if pRoot1 or pRoot2:
            # 以root1的根节点判断是否包含root2
            if pRoot1.val == pRoot2.val:
                result = self.Tree1HasTree2(pRoot1,pRoot2)
            # 如果找不到，继续以root1的左子树为根节点继续找
            if result == False:
                result = self.Tree1HasTree2(pRoot1.left, pRoot2)
            # 仍找不到继续以root1的右子树继续找
            if result == False:
                result = self.Tree1HasTree2(pRoot1.right, pRoot2)
        # return self.Tree1HasTree2(pRoot1,pRoot2) || self.Tree1HasTree2(pRoot1.left, pRoot2) || self.Tree1HasTree2(pRoot1.right, pRoot2)
        return result


    def Tree1HasTree2(self, root1, root2):
        # root2已经遍历完 都可以对上 返回true
        if not root2:
            return True
        # root2还没有遍历完，root1已经遍历完，返回 fasle
        if not root1:
            return False

        # root1节点与root2节点值不相同返回fasle
        if root1.val != root2.val:
            return False
        # 当root1与root2值相同时，进入左叶子节点与右叶子节点的对比
        return self.Tree1HasTree2(root1.left, root2.left) and self.Tree1HasTree2(root1.right, root2.right)
