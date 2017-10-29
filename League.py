"""
Created by Ricardo Morato
29/10/2017
"""

import numpy as np
import copy
from Structure import structure
from Jornada import Jornada


class League(object):
    def __init__(self, f):
        self.__file = f
        self.__data = None
        self.__jornadas = []
        self.read_file()

    def read_file(self):
        with open(self.__file, 'r') as f:
            lines = f.read().splitlines()

            num_lines = sum(1 for line in open(self.__file))
            num_lines -= 1  # Quit attr name row

            self.__data = np.array(map(lambda x: list(x.split(',')), lines[0:]))

            aux = self.__data[1:, 2]
            teams = sorted(set(aux))

            n_jornadas = len(np.argwhere(self.__data == teams[0]))

            i = 0
            while i < n_jornadas:
                if i == 0:
                    jornada = Jornada(teams)
                else:
                    jornada = copy.copy(self.__jornadas[i-1])

                for team in teams:
                    index = np.argwhere(self.__data == team)[i]
                    data = self.__data[index[0]] # Line in file for the team and jornada = i
                    t = teams.index(team) # Index of the team

                    result = data[6]
                    if index[1] == 2: # Home
                        if result == 'H': # Home wins
                            jornada.add_win(t)
                        elif result == 'A': # Away wins
                            jornada.add_loose(t)
                        else: # Draw
                            jornada.add_draw(t)
                    else: # Away
                        if result == 'H':  # Home wins
                            jornada.add_loose(t)
                        elif result == 'A':  # Away wins
                            jornada.add_win(t)
                        else:  # Draw
                            jornada.add_draw(t)

                self.__jornadas.append(jornada)
                i += 1

            print jornada.get_classification() # Print last jornada