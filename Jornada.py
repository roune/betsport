"""
Created by Ricardo Morato
28/10/2017
"""

import numpy as np


class Jornada(object):
    def __init__(self, teams):
        cols = 18
        self.__classification = np.zeros((len(teams), cols))
        self.__attr_names = ['Team', 'Points',
                             'Wins', 'Draws', 'Loose',
                             'Home wins', 'Home draws', 'Home loose',
                             'Away wins', 'Away draws', 'Away loose',
                             'Goals', 'Goals against',
                             'Home goals', 'Away goals',
                             'Home goals against', 'Away goals against',
                             'Position']

        translate_team_from_index = []
        # Work with index because np array dont work with Strings
        i = 0
        while i < len(teams):
            self.__classification[i, 0] = i # Teams column
            translate_team_from_index.insert(i, teams[i])
            #for j in range(1,cols):
            #    self.__classification[i, j] = 0
            i += 1

    def get_attr_names(self):
        return self.__attr_names

    def get_classification(self):
        #arr[arr[:, 1].argsort()]
        return self.__classification[(-self.__classification[:, 1]).argsort()].astype(int)
    
    def add_classification(self):
        clas = self.get_classification()
        for position in range(len(clas)):
            self.__classification[clas[position, 0], 17] = position + 1
    
    def get_team(self, index):
        return translate_team_from_index[index]

    def add_home_win(self, team):
        self.__classification[team, 5] += 1  # Add 1 in Home wins column
        self.add_win(team)

    def add_home_draw(self, team):
        self.__classification[team, 6] += 1  # Add 1 in Home draws column
        self.add_draw(team)

    def add_home_loose(self, team):
        self.__classification[team, 7] += 1  # Add 1 in Home loose column
        self.add_loose(team)

    def add_away_win(self, team):
        self.__classification[team, 8] += 1  # Add 1 in Away wins column
        self.add_win(team)

    def add_away_draw(self, team):
        self.__classification[team, 9] += 1  # Add 1 in Away draws column
        self.add_draw(team)

    def add_away_loose(self, team):
        self.__classification[team, 10] += 1  # Add 1 in Away loose column
        self.add_loose(team)

    def add_win(self, team):
        self.__classification[team, 2] += 1 # Add 1 in Wins column
        self.__classification[team, 1] += 3 # Add 3 in Points column

    def add_draw(self, team):
        self.__classification[team, 3] += 1
        self.__classification[team, 1] += 1  # Add 1 in Points column

    def add_loose(self, team):
        self.__classification[team, 4] += 1

    def add_goals(self, team, goals):
        self.__classification[team, 11] += goals

    def add_goals_against(self, team, goals):
        self.__classification[team, 12] += goals

    def add_home_goals(self, team, goals):
        self.__classification[team, 13] += goals
        self.add_goals(team, goals)

    def add_home_goals_against(self, team, goals):
        self.__classification[team, 15] += goals
        self.add_goals_against(team, goals)

    def add_away_goals(self, team, goals):
        self.__classification[team, 14] += goals
        self.add_goals(team, goals)

    def add_away_goals_against(self, team, goals):
        self.__classification[team, 16] += goals
        self.add_goals_against(team, goals)
        