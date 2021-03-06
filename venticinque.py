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

if __name__ == '__main__':

    # INIT
    board = np.zeros((5, 5))
    board[0][0] = 1
    curpos = [0, 0]
    counter = 1
    b0 = Board(board, curpos, counter)

    s = Stack()  # stack for boards
    s.push(b0)

    while not s.is_empty():
        if s.peek().counter == 25:
            print 'RISOLTO'
            print s.peek().board
            #sys.exit(0)
            break
        else:  # not a solution
            tmp = s.peek()  # take the first board on the stack
            tmp.list_moves()
            # generate possible moves from that board position
            # (which could also be invalid) and fill moves stack

            while not tmp.moves.is_empty():  # try next move from that pos.
                new_board = deepcopy(tmp)
                mov = tmp.moves.pop()
                if new_board.do_move(mov):  # if the move is valid
                    s.push(new_board)
                    print new_board.board, new_board.counter, new_board.curpos
            if s.peek() == tmp:  # no valid moves from here
                s.pop()
