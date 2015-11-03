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

import numpy as np
from copy import deepcopy
import sys

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

    def do_move(self, move):
        if self.board[move[0]][move[1]] == 0:
            self.counter += 1
            self.board[move[0]][move[1]] = self.counter
            self.curpos = move
            return True
        else:
            return False


def moves(pos):
    """
    return a list of legal moves in a given position (0..4,0..4)

    :rtype : list
    :param pos: (0..4,0..4)
    :return: a list of moves
    """
    j = pos[0]
    i = pos[1]
    retlist = []
    if j < 2:
        retlist.append([j+3, i])
    if j > 2:
        retlist.append([j-3, i])
    if i > 2:
        retlist.append([j, i-3])
    if i < 2:
        retlist.append([j, i+3])
    if j <= 2 and i <= 2:
        retlist.append([j + 2, i + 2])
    if j <= 2 and i >= 2:
        retlist.append([j + 2, i - 2])
    if j >= 2 and i <= 2:
        retlist.append([j - 2, i + 2])
    if j >= 2 and i >= 2:
        retlist.append([j - 2, i - 2])

    return retlist


if __name__ == '__main__':

    # INIT
    board = np.zeros((5, 5))
    board[0][0] = 1
    curpos = [0, 0]
    counter = 1
    b0 = Board(board, curpos, counter)

    s = Stack()  # stack for boards
    s.push(b0)
    m = Stack()  # stack for moves

    while not s.is_empty():
        if s.peek().counter == 25:
            print 'RISOLTO'
            print s.peek().board
            sys.exit(0)
        else:  # not a solution
            av_moves = moves(s.peek().curpos)  # generate possible moves from that board

            if av_moves:  # some moves available
                tmp = s.peek()
                for mov in av_moves:
                    new_board = deepcopy(tmp)
                    if new_board.do_move(mov):  # if the move is valid
                        s.push(new_board)
                        print new_board.board, new_board.counter, new_board.curpos
            else:  # no moves available with this board
                s.pop()
