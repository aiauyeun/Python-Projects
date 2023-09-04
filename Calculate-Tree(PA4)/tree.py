# assignment: PA4: Calculator
# author: Aidan Au-Yeung
# date: 11/18/22
# file: tree.py uses the stack class from stack.py to create a binary tree class which is used to make expression trees in the expression tree class!
# input: no inputs. its a class file

from stack import Stack

#class creates a Binary Tree 
class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
    
    def __str__(self):
        s = f"{self.key}"
        s += '('
        if self.leftChild != None:
            s += str(self.leftChild)
        s += ')('
        if self.rightChild != None:
            s += str(self.rightChild)
        s += ')'
        return s


    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
    
    def getLeftChild(self):
        return self.leftChild
    
    def getRightChild(self):
        return self.rightChild
    
    def getRootVal(self):
        return self.key
    
    def setRootVal(self,obj):
        self.key = obj

#Contains multiple methods that use the parent binary tree class
class ExpTree(BinaryTree):

    #returns an Expession Tree that is the binary tree of the inputed postfix expression
    def make_tree(postfix):
        # s=Stack()
        # for i in postfix:
        #     if i in "+-*/^":
        #         t=ExpTree(i)
        #         print(s.items)
        #         if t.rightChild == None:
        #             t.rightChild = ExpTree(s.pop())
        #         else:
        #             k = ExpTree(s.pop())
        #             k.rightChild = t.rightChild
        #             t.rightChild = k
        #         if t.leftChild == None:
        #             t.leftChild = BinaryTree(s.pop())

        #         else:
        #             k = ExpTree(s.pop())
        #             k.leftChild = t.leftChild
        #             t.leftChild = k               
        #         s.push(t)
        #     if i.isnumeric():
        #         s.push(i)
        # return s.pop()
        ops = '+-/*^'
        node_stack = Stack()
        root = ExpTree(postfix[-1])
        node_stack.push(root)
        del postfix[-1]
        for i in reversed(postfix):
            cur_node = node_stack.peek()
            while not cur_node.getLeftChild() == None and not cur_node.getRightChild() == None:
                node_stack.pop()
                cur_node = node_stack.peek()
 
            if i.replace('.','',1).isnumeric():
                if cur_node.getRightChild() == None:
                    cur_node.rightChild = ExpTree(i)
                else: 
                    cur_node.leftChild = ExpTree(i)
            elif i in ops:
                if cur_node.getRightChild() == None:
                    t = ExpTree(i)
                    cur_node.rightChild = t
                else:
                    t = ExpTree(i)  
                    cur_node.leftChild = t
                node_stack.push(t)
        
        return root
    
    #traverses tree to return the equation in prefix notation
    def preorder(tree):
        s = ''
        s += tree.getRootVal()
        if tree.getLeftChild() != None:
            s += tree.getLeftChild().preorder()
        if tree.getRightChild() != None:
            s += tree.getRightChild().preorder()
        return s
        #I spent way too much time trying to do this without recursion so I might as well leave my struggle in here. Originally made it so that for makeTree, if it there was an operator, I would attach on a new node to the tree and if it was a number, I would attach on a string :/ idfk my work was rendered useless compared to wikipedia's pseudocode...
        # #Traverses tree in order of root, left and then right!
        # out = ''
        # s = Stack()
        # s.push(tree)
        # traversed = []
        # while len(s.items) > 0:
        #     cur_node = s.peek()
        #     if traversed.count(cur_node) >= 2 and ((type(cur_node.getLeftChild() == str) and cur_node.getRightChild() in traversed)):
        #         out += cur_node.key
        #         s.pop()
        #         continue            
        #     if cur_node.getLeftChild() not in traversed:
        #         out += cur_node.key
        #         if type(cur_node.getLeftChild()) == BinaryTree:
        #             traversed.append(cur_node)
        #             s.push(cur_node.getLeftChild())
        #             continue
        #         else:
        #             out += cur_node.getLeftChild()
        #     if cur_node.getRightChild() not in traversed:
        #         if type(cur_node.getRightChild()) == str:
        #             out += cur_node.getRightChild()
        #         else:
        #             traversed.append(cur_node)
        #             s.push(cur_node.getRightChild())
        #             continue
        #     if type(cur_node.getRightChild()) == str and type(cur_node.getLeftChild()) == str:
        #         traversed.append(cur_node)
        #     if ((cur_node.getRightChild() in traversed) or (type(cur_node.getRightChild()) == str)) and ((type(cur_node.getLeftChild()) == str) or (cur_node.getLeftChild() in traversed)):
        #         s.pop()
        # return out

        
    #traverses exptree to return the equation in infix notation
    def inorder(tree):
        ops = '+-/*^'
        s = ''
        if tree.getRootVal() in ops:
            s += '('
        if tree.getLeftChild() != None:
            s += tree.getLeftChild().inorder()
        s += tree.getRootVal()
        if tree.getRightChild() != None:
            s += tree.getRightChild().inorder()
        if tree.getRootVal() in ops:
            s += ')'
        return s

            
        # #get to botom left node
        # out = ''
        # lowest = tree.getLeftChild()
        # s = Stack()
        # traversed = []
        # s.push(tree)
        # while type(lowest) != str:
        #     s.push(lowest)
        #     traversed.append(lowest)
        #     lowest = lowest.getLeftChild()

        # #traverse tree from left, root, then right!
        # while len(s.items) > 0:
        #     three = ''
        #     cur_node = s.peek()
        #     if type(cur_node.getLeftChild()) == str:
        #         if out.count('(') <= out.count(')'):
        #             three += '('
        #         three += cur_node.getLeftChild()
        #         #print(three)
        #         traversed.append(cur_node)
        #     elif cur_node.getLeftChild() not in traversed:
        #         s.push(cur_node.getLeftChild())
        #         continue
        #     three += cur_node.key
        #     #print(three)
        #     if type(cur_node.getRightChild()) == str:
        #         three += cur_node.getRightChild()
        #         if out.count('(') > out.count(')'):
        #             three += ')'
        #         #print(three)
        #         s.pop()            
        #     else:
        #         s.pop()
        #         s.push(cur_node.getRightChild())
        #     if type(cur_node.getRightChild()) == str and type(cur_node.getLeftChild()) == str:
        #         out += '(' + three + ')'
        #     else:
        #         out += three
        # out = '(' + out + ')'
        # print(out.count('('))
        # print(out.count(')'))
        # return out

    #traverses tree to return the expression in postfix notation  
    def postorder(tree):
        s = ''

        if tree.getLeftChild() != None:
            s += tree.getLeftChild().postorder()
        if tree.getRightChild() != None:
            s += tree.getRightChild().postorder()    
        s += tree.getRootVal()
        return s
        #Wasted too much time trying to do this so im leaving it in   
                #should be like inorder but now in the order left right root!
        #get to botom left node
        # out = ''
        # lowest = tree.getLeftChild()
        # s = Stack()
        # traversed = []
        # s.push(tree)
        # while type(lowest) != str:
        #     s.push(lowest)
        #     traversed.append(lowest)
        #     lowest = lowest.getLeftChild()

        # #inorder:traverse tree from left, root, then right!
        # #goal is to change this code to make it traverse tree to left, right, then root!
        # while len(s.items) > 0:
        #     cur_node = s.peek()
        #     traversed.append(cur_node)
        #     if traversed.count(cur_node) >= 2 and ((type(cur_node.getLeftChild() == str) and cur_node.getRightChild() in traversed)):
        #         out += cur_node.key
        #         s.pop()
        #         continue
        #     if cur_node.getLeftChild() not in traversed:
        #         if type(cur_node.getLeftChild()) == str:
        #             traversed.append(cur_node.getLeftChild())
        #             out += cur_node.getLeftChild()
                    
        #         else:
        #             s.push(cur_node.getLeftChild())
        #             continue
        #         #print(out)
        #     if cur_node.getRightChild() not in traversed:
        #         if type(cur_node.getRightChild()) == str:
        #             traversed.append(cur_node.getRightChild())
        #             out += cur_node.getRightChild()
        #             #print(out)
        #         else:
        #             s.push(cur_node.getRightChild())
        #             continue
        #     out += cur_node.key
        #     if ((cur_node.getRightChild() in traversed) or (type(cur_node.getRightChild()) == str)) and ((type(cur_node.getLeftChild()) == str) or (cur_node.getLeftChild() in traversed)):
        #         s.pop()
        # print(traversed)
        # return out

    #traverses through the tree to evaluate the expression
    def evaluate(tree):
        out = 0.0
        ops = '+-/*^'
        first = 0.0
        second = 0.0
        op = None
        if tree.getRootVal() == None:
            return 0.0
        
        if tree.getLeftChild() == None and tree.getRightChild() == None:
            return tree.getRootVal()

        first = ExpTree.evaluate(tree.getLeftChild())
        second = ExpTree.evaluate(tree.getRightChild())

        if tree.getRootVal() == '+':
            return float(first) + float(second)
        if tree.getRootVal() == '-':
            return float(first) - float(second)  
        if tree.getRootVal() == '*':
            return float(first) * float(second)        
        if tree.getRootVal() == '/':
            return float(first) / float(second)  
        if tree.getRootVal() == '^':
            return float(first) ** float(second)  
            
    
    def __str__(self):
        return ExpTree.inorder(self)
    # def __str__(self):
    #     s = f"{self.key}"
    #     s += '('
    #     if self.leftChild != None:
    #         s += str(self.leftChild)
    #     s += ')('
    #     if self.rightChild != None:
    #         s += str(self.rightChild)
    #     s += ')'
    #     return s

        

   
# a driver for testing BinaryTree and ExpTree
if __name__ == '__main__':
    
    postfix = '5 2 + 3 *'.split()
    # #postfix and prefix don't work for dupes
    # #2 2 3 * 4 5 6 / * + *
    # #1 2 + 3 4 + 5 * - 6 +
    # #1 2 + 3 4 + 5 * - 6 + 7 8 9 / 10 11 12 / * + * -
    tree = ExpTree.make_tree(postfix)
    print(tree)
    # print(ExpTree.postorder(tree))
    # print(ExpTree.postorder(tree))
    print(ExpTree.evaluate(tree))
    # print(ExpTree.evaluate(tree))
    # # test an ExpTree
    
    # postfix = '5 2 3 * +'.split()
    # tree = ExpTree.make_tree(postfix)
    # assert str(tree) == '(5+(2*3))'
    # assert ExpTree.inorder(tree) == '(5+(2*3))'
    # assert ExpTree.postorder(tree) == '523*+'
    # assert ExpTree.preorder(tree) == '+5*23'
    # assert ExpTree.evaluate(tree) == 11.0

    # postfix = '5 2 + 3 *'.split()
    # tree = ExpTree.make_tree(postfix)
    # assert str(tree) == '((5+2)*3)'
    # assert ExpTree.inorder(tree) == '((5+2)*3)'
    # assert ExpTree.postorder(tree) == '52+3*'
    # assert ExpTree.preorder(tree) == '*+523'
    # assert ExpTree.evaluate(tree) == 21.0