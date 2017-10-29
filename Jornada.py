"""
Created by Ricardo Morato
28/10/2017
"""

import numpy as np
from Structure import structure


class Jornada(object):
    def __init__(self, teams):
        cols = 5
        self.__classification = np.empty((len(teams), cols))
        '''self.__classification[0, 0] = 'Team'
        self.__classification[0, 1] = 'Points'
        self.__classification[0, 2] = 'Wins'
        self.__classification[0, 3] = 'Draws'
        self.__classification[0, 4] = 'Loose'''

        # Work with index because np array dont work with Strings
        i = 0
        while i < len(teams):
            self.__classification[i, 0] = i # Col Team
            i += 1

    def get_classification(self):
        #arr[arr[:, 1].argsort()]
        return self.__classification[self.__classification[:, 1].argsort()].astype(int)

    def add_win(self, team):
        self.__classification[team, 2] += 1 # Add 1 in Wins column
        self.__classification[team, 1] += 3 # Add 3 in Points column

    def add_draw(self, team):
        self.__classification[team, 3] += 1
        self.__classification[team, 1] += 1  # Add 1 in Points column

    def add_loose(self, team):
        self.__classification[team, 4] += 1