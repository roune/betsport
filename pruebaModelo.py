import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder

if __name__ == '__main__':

    lenc = LabelEncoder()
    data1=pd.read_csv('./Datasets/SP1-2012_normAverage.csv')
    data2 = pd.read_csv('./Datasets/SP1-2013_normAverage.csv')
    data3 = pd.read_csv('./Datasets/SP1-2014_normAverage.csv')
    data4 = pd.read_csv('./Datasets/SP1-2015_normAverage.csv')
    data5 = pd.read_csv('./Datasets/SP1-2016_normAverage.csv')

    data =  pd.concat([data1,data2, data3, data4, data5])

    y_df = data['FTR']
    x_df = data.loc[:,data.columns != 'FTR']
    y = lenc.fit_transform(np.array(y_df))
    X = np.array(x_df.loc[:,[True if c not in  ['Div','Date','HomeTeam','AwayTeam','HTTeam','ATTeam'] else False for c in x_df.columns]])

    final_x = []
    final_y = []
    for i in range(X.shape[0]):
        if np.any(X[i]):
            final_x.append(X[i])
            final_y.append(y[i])

    X = np.array(final_x)
    y = np.array(final_y)


    # Cross Validation a usar y numero maximo de iteraciones


    clf = RandomForestClassifier(bootstrap=True, class_weight= None, criterion= 'entropy', max_depth= 6, min_samples_leaf= 2, min_samples_split= 10, n_estimators= 1000)
    scores = cross_val_score(clf, X, y)

    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

