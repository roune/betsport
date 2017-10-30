"""
Created by Ricardo Morato
29/10/2017
"""

import numpy as np
import copy

from Data import Data
from Jornada import Jornada


class League(object):
    def __init__(self, f):
        self.__file = f
        self.__data = None
        self.__jornadas = []
        self.__dataset = Data(f, True)

        self.set_data()

    def get_jornada(self, n):
        return self.__jornadas[n]

    def set_data(self):
        '''
        for line in self.__dataset:
            print (line)'''
        dataset = self.__dataset.get_data()

        aux = dataset[:, 2]
        teams = sorted(set(aux))

        matches = []

        for team in teams:
            aux = []

            for match in np.argwhere(dataset[:, 2] == (team)):
                aux.append(match[0])

            for match in np.argwhere(dataset[:, 3] == (team)):
                aux.append(match[0])

            matches.append(sorted(aux))

        for team in matches:
            print team

        i = 0
        while i < len(matches[0]):
            if i == 0:
                jornada = Jornada(teams)
            else:
                jornada = copy.copy(self.__jornadas[i-1])

            for team in teams:
                match = matches[int(team)][i]
                data = dataset[match]  # Line in file for the team and jornada = i

                result = data[6]
                if data[2] == team:  # Home
                    if result == 2:  # Home wins
                        jornada.add_home_win(int(team))
                    elif result == 1:  # Away wins
                        jornada.add_home_loose(int(team))
                    else:  # Draw
                        jornada.add_home_draw(int(team))

                    jornada.add_home_goals(int(team), int(data[4]))
                    jornada.add_home_goals_against(int(team), int(data[5]))
                else:  # Away
                    if result == 2:  # Home wins
                        jornada.add_away_loose(int(team))
                    elif result == 1:  # Away wins
                        jornada.add_away_win(int(team))
                    else:  # Draw
                        jornada.add_away_draw(int(team))

                    jornada.add_away_goals(int(team), int(data[5]))
                    jornada.add_away_goals_against(int(team), int(data[4]))


                jornada.add_classification()

                # data = self.__data[index[0]]  # Line in file for the team and jornada = i
                # t = teams.index(team)  # Index of the team

                self.__jornadas.append(jornada)

            i += 1