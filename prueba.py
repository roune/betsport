import numpy as np
from Data import Data
from League import League

if __name__ == '__main__':
    #dataset = Data('./SP1.csv', True)
    #print dataset.get_data()

    l = League('./SP1.csv')
    #for i in range(20):
    #print (l.get_jornada(8).get_classification().tolist())
    for team in l.get_jornada(1).get_classification().tolist():
        print (team)
    #np.savetxt('output.out', dataset.get_norm_data(), delimiter=',')
