# assignment: PA4: Calculator
# author: Aidan Au-Yeung
# date: 11/18/22
# file: Main module for PA4. Contains uses the tree.py class to make Binary Trees to perform simple calculations.
# input: infix equation
# output: solved equation
from stack import Stack
from tree import ExpTree
import re
#shitty regex implementation. Problem: string manipulation. How tf would we place the parantheses shit in order. idk i left this in becaue i put effort into it and it didn't work :/
# def infix_to_postfix(infix):
#     out = []
#     #print(infix)
#     stuff_in_paren = re.findall(r'\((.*?)\)',infix)
#     if len(stuff_in_paren) > 0:
#         for stuff in stuff_in_paren:
#             #print(stuff)
#             out.append(infix_to_postfix(stuff))
#             infix = infix.replace(stuff, "")
#             #print(infix)
#     num_lst = re.findall('[\d]+', infix) 
#     op_lst = re.findall('[+-/*]',infix)
#     for num in num_lst:
#         out.append(num)
#     if len(op_lst) == 1:
#         out.append(op_lst[0])
#     else:
#         for i in range(len(op_lst)):
#             out.append(op_lst[-i+1])
#     return out

#method takes in an equation and returns a list where each operands are combined into list value. exp combine_nums('420/69') would return the list ['420','/','69'] idk its hard to describe what this method does in words but its really basic -_- 
def combine_nums(objects):
    #print(objects)
    out = []
    ops = '+-/*()^'
    combo = ''
    for index, obj in enumerate(objects):
        if obj in ops:
            out.append(obj)
        elif index < len(objects)-1:
            if objects[index+1] in ops:
                if combo == '':
                    out.append(obj)
                else:
                    combo += obj
                    out.append(combo)
                    combo = ''
            else:
                combo += obj
        else:
            combo += obj
            out.append(combo)
    return out
        
#takes in an infix equation as a string and returns a string which is the postfix version of the input
def infix_to_postfix(infix):
    s = Stack()
    ops = {'+':0,'-':0,'*':1,'/':1,'^':2}
    out = []
    infix = combine_nums(infix)
    for char in infix:
        if char == '(':
            s.push(char)
            #print(char)
            #print('postfix:' + str(out))
            #print('stack' + str(s.items))
        elif s.items.count('(') > 0:
            if char.replace('.','',1).isnumeric():
                out.append(char)
                #print(char)
                #print('postfix:' + str(out))
                #print('stack' + str(s.items))
            elif char in ops:
                if not s.isEmpty():
                    if s.peek() != '(':
                        if ops[s.peek()] >= ops[char]:
                            out.append(s.pop())
                s.push(char)
                #print(char)
                #print('postfix:' + str(out))
                #print('stack' + str(s.items))               
            elif char == ')':
                while not s.peek() == '(':
                        out.append(s.pop())
                s.pop()
                #print(char)
                #print('postfix:' + str(out))
                #print('stack' + str(s.items))
                # if not s.isEmpty() and s.peek() != '(':
                #     out.append(s.pop())

        elif char.replace('.','',1).isnumeric():
            out.append(char)
            #print(char)
            #print('postfix:' + str(out))
            #print('stack' + str(s.items))            
        elif char in ops:
            if not s.isEmpty():
                if ops[s.peek()] >= ops[char]:
                    out.append(s.pop())
                    if not s.isEmpty():
                        if ops[s.peek()] == ops[char]:
                            out.append(s.pop())                   
            s.push(char)
            #print(char)
            #print('postfix:' + str(out))
            #print('stack' + str(s.items))
        else:
            #print(char)
            print('error!')
    while not s.isEmpty():
        out.append(s.pop())
    
    return ' '.join(out)

#converts infix equation into postfix to create an expression tree that evaluates the equation. returns a float which is the output of the equation   
def calculate(infix):
    postfix = infix_to_postfix(infix)
    #print(postfix)
    postfix = postfix.split()
    #print(postfix)
    tree = ExpTree.make_tree(postfix)
    #print(tree)
    return ExpTree.evaluate(tree)

#Main Interface!
if __name__ == '__main__':
    print('Welcome to Calculator Program!')
    quit = False
    while quit == False:
        infix = input("Please enter your expression here. To quit enter 'quit' or 'q':")
        if infix == 'quit' or infix == 'q':
            quit = True
        else:
            try:
                print('\n')
                print(calculate(infix))
            except:
                print("ERROR! Enter your equation in infix notation! Exp: (a+b)*c/d^(e-f)")
    print('\nGoodbye!')
#a driver to test calculate module
# if __name__ == '__main__':
#     # test infix_to_postfix function
#     assert infix_to_postfix('(5+2)*3') == '5 2 + 3 *'
#     assert infix_to_postfix('5+2*3') == '5 2 3 * +'

#     # test calculate function
#     assert calculate('(5+2)*3') == 21.0
#     assert calculate('5+2*3') == 11.0
    
    
