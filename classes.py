'''
This module implements some classes necessary to logical propositions
in memory.

Every prosition is stored as a tree whose nodes are logical operators,
except the leaves which are logical variables.
'''

if(__name__=="__main__"):

    '''
    This makes sure that the same file is not imported multiple times.
    '''

    from parsing import *


class LogicalVariable():

    
    def __init__(self, symbol):

        self.symbol = symbol
        self.value = None

    def assign_value(self, value):

        self.value = value

    def read(self):

        value = self.value
        self.value = None
        return value


class TreeNode():


    '''
    This class implements a tree node and basics methods to manipulate it.

    It holds a piece of data, a variable pointing at its parents and a list of children.

    It should be provided with the data is going to hold at initialization. If existing, a parent
    can be provided as well.

    The methods implemented allow to to add and remove children, change the data which it is 
    holding, and set or change its parent.
    
    This class is iterable. Trying to use it this way will cause it to iterate over the list
    of children.
    '''

    def __init__(self, data, parent=None):

        self.data = data
        self.children = []
        self.parent = parent

    def add_child(self, child):

        self.children.append(child)

    def remove_child(self, child):

        self.children.remove(child)

    def change_data(self, data):

        self.data = data

    def set_parent(self, parent):

        self.parent = parent

    def __iter__(self):

        return iter(self.children)

'''
class Proposition():

    def __init__(self, expression):

'''