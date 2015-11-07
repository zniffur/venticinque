import numpy as np
from copy import deepcopy
import sys

__author__ = 'simo'

"""
j rows
i cols
      i
  0 1 2 3 4
0
1
2 j
3
4

Legal moves conditions (cond, move, result)

j<2  DOWN  j+3
j>2  UP    j-3
i>2  LEFT  i-3
i<2  RIGHT i+3

j<=2, i<=2  DOWN-RIGHT j+2,i+2
j<=2, i>=2  DOWN-LEFT  j+2,i-2
j>=2, i<=2  UP-RIGHT   j-2,i+2
j>=2, i>=2  UP-LEFT    j-2,i-2
"""

# class Node(object):
#
#     def __init__(self, data):
#         """
#
#         :rtype : a node of a tree
#         """
#         self.data = data
#         self.children = []
#
#     def add_child(self, obj):
#         self.children.append(obj)


class Tree(object):

    def __init__(self):
        self.items = []
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def num_children(self):
        return len(self.children)

    def add_item(self, item):
        self.items.append(item)

    def get_item(self):  # get the first of the item
        return self.items[len(self.items)-1]

class Stack(object):

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


class Board(object):

    def __init__(self, board, curpos, counter):
        self.board = board
        self.curpos = curpos
        self.counter = counter
        self.moves = None

    def list_moves(self):
        """
        fill the stack of moves of legal moves in a given position (0..4,0..4)

        :rtype : int
        :param pos: (0..4,0..4)
        :return: True on success
        """

        pos = self.curpos
        self.moves = Stack()
        j = pos[0]
        i = pos[1]

        if j < 2:
            self.moves.push([j+3, i])
        if j > 2:
            self.moves.push([j-3, i])
        if i > 2:
            self.moves.push([j, i-3])
        if i < 2:
            self.moves.push([j, i+3])
        if j <= 2 and i <= 2:
            self.moves.push([j + 2, i + 2])
        if j <= 2 and i >= 2:
            self.moves.push([j + 2, i - 2])
        if j >= 2 and i <= 2:
            self.moves.push([j - 2, i + 2])
        if j >= 2 and i >= 2:
            self.moves.push([j - 2, i - 2])

        return True

    def do_move(self, move):

        if self.board[move[0]][move[1]] == 0:
            self.counter += 1
            self.board[move[0]][move[1]] = self.counter
            self.curpos = move
            return True
        else:
            return False

num_sol = 0


def explore(node):

    if node.get_item().counter == 25:
        global num_sol
        num_sol += 1
        print 'SOL #: ' + str(num_sol)
        print node.get_item().board
        #sys.exit(0)
        return True
    else:
        # add all valid children to the node (i.e. valid moves from current pos)

        tmp = node.get_item()  # read board of this node
        tmp.list_moves()  # generate possible moves
        while not tmp.moves.is_empty():  # loop on the moves
            new_board = deepcopy(tmp)
            mov = tmp.moves.pop()  # pop 1 move
            if new_board.do_move(mov):  # if the move is valid
                new_child = Tree()
                new_child.add_item(new_board)
                node.add_child(new_child)  # add new child

        # recursion: explore all valid children
        for child in node.children:
            # print child.get_item().board
            explore(child)

if __name__ == '__main__':

    # INIT
    board = np.zeros((5, 5))
    board[0][0] = 1
    curpos = [0, 0]
    counter = 1
    b0 = Board(board, curpos, counter)

    t = Tree()  # tree for boards
    t.add_item(b0)  # root node

    explore(t)
    # test
