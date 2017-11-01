"""
Created by Ricardo Morato
29/10/2017
"""

import numpy as np
import copy
from heapq import merge

from Data import Data
from Jornada import Jornada


class League(object):
    def __init__(self, f):
        self.__file = f
        self.__data = None
        self.__jornadas = []
        self.__data_full = []
        self.__teams = []
        self.__matches = None
        self.__d = Data(f, True)
        self.__dataset = self.__d.get_data().tolist()
        self.set_data()

        i = 0

        while i < len(self.__jornadas):
            self.set_jornada_full(i)
            i += 1

    def get_attr_names(self):
        data = []
        data.append(self.__jornadas[0].get_attr_names())
        data.append(self.__d.get_attr_names())
        return data

    def get_jornada(self, n):
        return self.__jornadas[n]

    def get_jornada_full(self, n):
        return self.__data_full[(n)*len(self.__teams):(n+1)*len(self.__teams)]

    def set_jornada_full(self, n):
        jornada = self.__jornadas[n].get_classification().tolist()

        for team in jornada:
            line = self.__matches[team[0]]
            additional = self.__dataset[line[n][0]-1]

            aux = []
            aux.append(team)
            aux.append(additional)

            #Hace merge de dos lista pero mezcla los ordenes
            # y ya no se donde esta cada cosa xd
            #aux.append(list(merge(team, additional)))

            self.__data_full.append(aux)

    def get_index_team(self, team):
        return self.__teams.index(team)

    def set_data(self):
        with open(self.__file, 'r') as f:
            lines = f.read().splitlines()

            num_lines = len(lines)
            num_lines -= 1  # Quit attr name row

            # self.__data = np.array(map(lambda x: list(x.split(',')), lines[0:]))
            self.__data = np.array([list(x.split(',')) for x in lines[0:]])
            
            aux = self.__data[1:, 2]
            self.__teams = sorted(set(aux))
            teams = self.__teams

            n_jornadas = len(np.argwhere(self.__data == teams[0]))

            all_matches = []

            for team in teams:
                matches = np.argwhere(self.__data == team).tolist()
                all_matches.append(matches)

            self.__matches = all_matches

            i = 0
            while i < n_jornadas:
                if i == 0:
                    jornada = Jornada(teams)
                else:
                    jornada = copy.deepcopy(self.__jornadas[i-1])

                for team in teams:
                    t = self.get_index_team(team)  # Index of the team
                    index = all_matches[t][i]
                    data = self.__data[index[0]] # Line in file for the team and jornada = i

                    result = data[6]
                    if index[1] == 2: # Home
                        if result == 'H': # Home wins
                            jornada.add_home_win(t)
                        elif result == 'A': # Away wins
                            jornada.add_home_loose(t)
                        else: # Draw
                            jornada.add_home_draw(t)

                        jornada.add_home_goals(t, int(data[4]))
                        jornada.add_home_goals_against(t, int(data[5]))
                    else: # Away
                        if result == 'H':  # Home wins
                            jornada.add_away_loose(t)
                        elif result == 'A':  # Away wins
                            jornada.add_away_win(t)
                        else:  # Draw
                            jornada.add_away_draw(t)

                        jornada.add_away_goals(t, int(data[5]))
                        jornada.add_away_goals_against(t, int(data[4]))
                
                jornada.add_classification()
                self.__jornadas.append(jornada)
                i += 1