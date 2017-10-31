"""
Created by Ricardo Morato
29/10/2017
"""

import numpy as np
import copy
from Jornada import Jornada


class League(object):
    def __init__(self, f):
        self.__file = f
        self.__data = None
        self.__jornadas = []
        self.set_data()

    def get_jornada(self, n):
        return self.__jornadas[n]

    def set_data(self):
        with open(self.__file, 'r') as f:
            lines = f.read().splitlines()

            num_lines = sum(1 for line in open(self.__file))
            num_lines -= 1  # Quit attr name row
            
            # self.__data = np.array(map(lambda x: list(x.split(',')), lines[0:]))
            self.__data = np.array([list(x.split(',')) for x in lines[0:]])
            
            aux = self.__data[1:, 2]
            teams = sorted(set(aux))

            n_jornadas = len(np.argwhere(self.__data == teams[0]))

            i = 0
            while i < n_jornadas:
                if i == 0:
                    jornada = Jornada(teams)
                else:
                    jornada = copy.deepcopy(self.__jornadas[i-1])

                for team in teams:
                    index = np.argwhere(self.__data == team)[i]
                    data = self.__data[index[0]] # Line in file for the team and jornada = i
                    t = teams.index(team) # Index of the team
                    
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