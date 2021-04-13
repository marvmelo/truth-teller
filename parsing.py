'''
This module contains the functions responsible for receiving a string
with a logical expression and processing it into a tree using the TreeNode
class defined in the classes module.

It also contains some important global variables.
'''

if(__name__=="__main__"):

    '''
    This makes sure that the same file is not imported multiple times.
    '''

    from classes import *

#This list determine the symbols that represents the logical variables.
#The length of the list determines the maximum number of logical variables the program can handle.
from string import ascii_lowercase as variable_alphabet
#The order in which operators appear in this list determine their priority.
operators = ["=", ">", "|", "&", "!"]
#This dictionary holds all instances of the LogicalVariable class.
#It exists so two leaves in the proposition tree can point to the same data structure.
logical_variables = {}


def fill_logical_variables_dic(expression):


    '''
    This function is 
    '''


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
    The expression (x&y)=x would be split into (x&y), =, and x.

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
    This function takes a list of subexpressions and an operatot.

    It splits the list into two list at the place of the first occourrence of the operator and
    return the two sublists.
    '''

    index_operator = expression_list.index(operation)
    
    return expression_list[:index_operator], expression_list[index_operator+1:]