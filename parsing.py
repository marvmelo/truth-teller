'''
This module contains the functions responsible for receiving a string
with a logical expression and processing it into a tree using the TreeNode
class defined in the classes module.
'''

if(__name__=="__main__"):

    '''
    This makes sure that the same file is not imported multiple times.
    '''

    from classes import *

from string import ascii_lowercase as variable_alphabet
#The order in which operators appear in this list determine their priority.
operators = ["B", ">", "|", "&", "!"]


def is_single_variable(expression):


    '''
    This function verifies if a string contains only a single logical variable.
    '''

    if(len(expression)==1)and(expression in variable_alphabet):

        return True
    
    else:

        return False


def is_single_operator(expression):


    '''
    This function verifies if a string contains only a single operator.
    '''

    if(len(expression)==1)and(expression in operators):

        return True

    else:

        return False


def split_parentheses(expression):


    '''
    This function is responsible for dealing with parentheses.

    It splits an expression into several subexpressions and their operators
    that, due to parentheses, are in the same scope.

    For instance:
    The expression (x&y)Bx would be split into (x&y), B, and x.

    It returns a list of strings which are expressions and operators in order.
    '''

    split_expression = []
    num_parentheses = 0
    index_initial_parentheses = 0

    for index in range(len(expression)):

        if(expression[index]=="("):

            if(num_parentheses==0):

                index_initial_parentheses = index

            num_parentheses += 1

        elif(expression[index]==")"):

            num_parentheses -= 1

            if(num_parentheses==0):

                split_expression.append(expression[index_initial_parentheses+1:index])

        elif(num_parentheses!=0):

            continue

        elif(expression[index] in variable_alphabet):

            split_expression.append(expression[index])

        elif(expression[index] in operators)and(expression[index]!="!"):

            split_expression.append(expression[index])

    if(len(split_expression)==1):

        split_expression = scope_split(split_expression[0])

    return split_expression


def split_subexpressions(expression_list, operation):


    '''
    This function spli
    '''

    index_operator = expression_list.index(operation)
    
    return expression_list[:index_operator], expression_list[index_operator+1:]

def oberve (expression):

    
'''
def prepare_associative_operator(expression_list, operation):


    
    This function takes a list of subexpressions and an operator and split
    it into lists of subexpressions which are operands of the several consecutive first
    appearence of the operator.

    This is important because a node containing an associative operator can have several child
    which can make this implementation more efficient.

    It would return the operator and the list of lists.

    Initially, this function would make into the final code. But I realized this would make my work
    at the tree structure level easier, which is the opposite of what I wanted. Then, it was discarded,
    but I decided to keep it in the code just in case.


    indeces_operator = []
    prepared_expressions = []
    index_intial = expression_list.index(operation)

    for index_expression in range(index_intial, len(expression_list)):

        if(expression_list[index_expression]==operation):

            indeces_operator.append(index_expression)

        elif(is_single_operator(expression_list[index_expression])):

            break
'''