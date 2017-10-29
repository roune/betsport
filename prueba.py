import numpy as np
from Data import Data
from League import League

if __name__ == '__main__':
    #dataset = Data('./SP1.csv', True)
    #print dataset.get_data()
    l = League('./SP1.csv')
    print l.get_jornada(8).get_classification()
    #np.savetxt('output.out', dataset.get_norm_data(), delimiter=',')
