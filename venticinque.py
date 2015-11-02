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


class Board(object):

    def __init__(self):
        self.board = np.zeros((5, 5))
        self.curpos = [0, 0]
        self.counter = 1
        self.board[0][0] = 1

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

    L = []

    print '--- LEVEL 0 --'
    b0 = Board()  # new empty board
    L.append([b0])

    print '--- LEVEL 1 --'
    av_moves = moves(L[0][0].curpos)  # init av. moves
    llist = []
    for mov in av_moves:
        tmp = deepcopy(L[0][0])
        if tmp.do_move(mov):
            llist.append(tmp)
    L.append(llist)

    print '--- LEVEL 2 --'
    found = False
    level = 2
    while not found:
        for c_board in L[level - 1]:
            av_moves = moves(c_board.curpos)

