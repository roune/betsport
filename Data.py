"""
Created by Ricardo Morato
28/10/2017
"""

import numpy as np

from Structure import structure


class Data(object):
    def __init__(self, f, norm = False):
        self.__file = f
        self.__attr_names = []
        self.__data = None
        self.__data_ready = None
        self.__data_norm_ready = None

        self.read_file()

        if norm:
            self.norm_data()

    def get_attr_names(self):
        return self.__attr_names

    def get_league(self):
        return self.__league

    def get_nom_attr_names(self):
        aux = []

        for attr in self.__attr_names:
            if structure.has_key(attr):
                aux.append(attr)

        return aux

    def get_cont_attr_names(self):
        aux = []

        for attr in self.__attr_names:
            if not structure.has_key(attr):
                aux.append(attr)

        return aux

    def get_data(self):
        return self.__data_ready

    def get_norm_data(self):
        return self.__data_norm_ready

    def get_matches(self, jornada):
        yield

    # !Problem with -999 data. Change -999 to other value?
    def norm_data(self):
        num_cols = self.__data_ready.shape[1]
        num_lines = self.__data_ready.shape[0]

        # Not good solution. Not discrimine de nominal data

        i = 0
        while i < num_cols:
            self.__data_norm_ready = np.empty((num_lines, num_cols))

            col = self.__data_ready[:, i]
            mean = np.mean(col)
            std = np.std(col)

            if std == 0: std = 0.0000001

            j = 0
            while j < num_lines:
                self.__data_norm_ready[j, i] = ((self.__data_ready[j, i] - mean) / std)
                j += 1

            i += 1

    def read_file(self):
        with open(self.__file, 'r') as f:
            lines = f.read().splitlines()

            self.__attr_names = lines[0].split(',')

            num_lines = sum(1 for line in open(self.__file))
            num_lines -= 1  # Quit attr name row
            num_cols = len(self.__attr_names)

            self.__data = np.array(map(lambda x: list(x.split(',')), lines[0:]))
            self.__data_ready = np.empty((num_lines, num_cols))

            i = 0 # Cols
            for attr in self.__data[0]:
                if structure.has_key(attr):
                    aux = self.__data[1:, i]
                    keys = sorted(set(aux))
                    aux_dict = {}

                    # Asign a numeric value to the key
                    j = 0
                    for key in keys:
                        aux_dict[key] = j
                        j += 1

                    # Change the key for the numeric value
                    j = 0
                    while j < len(aux):
                        aux[j] = aux_dict[aux[j]]
                        j += 1

                    j = 0
                    while j < num_lines:
                        self.__data_ready[j, i] = aux[j]
                        j += 1

                else:
                    # If value is empty, error. Change the empty values for -999 in the .csv
                    aux = self.__data[1:,i].astype('float')
                    j = 0
                    while j < num_lines:
                        self.__data_ready[j, i] = aux[j]
                        j += 1
                i += 1

            #np.savetxt('output.out', self.data_ready, delimiter=',')