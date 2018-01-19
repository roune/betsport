import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder

def fit():
    lenc = LabelEncoder()
    data1 = pd.read_csv('./Datasets/SP1-2012_normAverage_withoutDuplicate.csv')
    data2 = pd.read_csv('./Datasets/SP1-2013_normAverage_withoutDuplicate.csv')
    data3 = pd.read_csv('./Datasets/SP1-2014_normAverage_withoutDuplicate.csv')
    data4 = pd.read_csv('./Datasets/SP1-2015_normAverage_withoutDuplicate.csv')
    data5 = pd.read_csv('./Datasets/SP1-2016_normAverage_withoutDuplicate.csv')
    data6 = pd.read_csv('./Datasets/D1-2012_normAverage_withoutDuplicate.csv')
    data7 = pd.read_csv('./Datasets/D1-2013_normAverage_withoutDuplicate.csv')
    data8 = pd.read_csv('./Datasets/D1-2014_normAverage_withoutDuplicate.csv')
    data9 = pd.read_csv('./Datasets/D1-2015_normAverage_withoutDuplicate.csv')
    data10 = pd.read_csv('./Datasets/D1-2016_normAverage_withoutDuplicate.csv')
    data11 = pd.read_csv('./Datasets/E0-2012_normAverage_withoutDuplicate.csv')
    data12 = pd.read_csv('./Datasets/E0-2013_normAverage_withoutDuplicate.csv')
    data13 = pd.read_csv('./Datasets/E0-2015_normAverage_withoutDuplicate.csv')
    data14 = pd.read_csv('./Datasets/E0-2016_normAverage_withoutDuplicate.csv')

    data =  pd.concat([data1,data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13, data14])

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
    clf = RandomForestClassifier( n_estimators= 1000, n_jobs=6)
    scores = cross_val_score(clf, X, y)

    print("Accuracy: %0.4f (+/- %0.4f)" % (scores.mean(), scores.std() * 2))



def test():
    lenc = LabelEncoder()
    data1 = pd.read_csv('./Datasets/SP1-2012_normAverage_withoutDuplicate.csv')
    data2 = pd.read_csv('./Datasets/SP1-2013_normAverage_withoutDuplicate.csv')
    data3 = pd.read_csv('./Datasets/SP1-2014_normAverage_withoutDuplicate.csv')
    data4 = pd.read_csv('./Datasets/SP1-2015_normAverage_withoutDuplicate.csv')
    data6 = pd.read_csv('./Datasets/D1-2012_normAverage_withoutDuplicate.csv')
    data7 = pd.read_csv('./Datasets/D1-2013_normAverage_withoutDuplicate.csv')
    data8 = pd.read_csv('./Datasets/D1-2014_normAverage_withoutDuplicate.csv')
    data9 = pd.read_csv('./Datasets/D1-2015_normAverage_withoutDuplicate.csv')
    data10 = pd.read_csv('./Datasets/D1-2016_normAverage_withoutDuplicate.csv')
    data11 = pd.read_csv('./Datasets/E0-2012_normAverage_withoutDuplicate.csv')
    data12 = pd.read_csv('./Datasets/E0-2013_normAverage_withoutDuplicate.csv')
    data13 = pd.read_csv('./Datasets/E0-2015_normAverage_withoutDuplicate.csv')
    data14 = pd.read_csv('./Datasets/E0-2016_normAverage_withoutDuplicate.csv')
    data15 = pd.read_csv('./Datasets/E0-2017_normAverage_withoutDuplicate.csv')

    data5 = pd.read_csv('./Datasets/SP1-2016_normAverage_withoutDuplicate.csv')

    data =  pd.concat([data1,data2, data3, data4, data6, data7, data8, data9, data10, data11, data12, data13, data5])

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
    clf = RandomForestClassifier( n_estimators= 1000, n_jobs=6)
    clf.fit(X,y)

    y_dft = data14['FTR']
    x_dft = data14.loc[:,data14.columns != 'FTR']
    yt = lenc.fit_transform(np.array(y_dft))
    Xt = np.array(x_dft.loc[:,[True if c not in  ['Div','Date','HomeTeam','AwayTeam','HTTeam','ATTeam'] else False for c in x_dft.columns]])

    final_xt = []
    final_yt = []
    for i in range(Xt.shape[0]):
        if np.any(Xt[i]):
            final_xt.append(Xt[i])
            final_yt.append(yt[i])

    Xt = np.array(final_xt)
    yt = np.array(final_yt)

    score = clf.score(Xt, yt)
    print("Accuracy: %0.4f" % (score))
    resultado = lenc.inverse_transform(clf.predict(X))
    print(resultado)

    cH=0
    cD=0
    cA=0
    for r in resultado:
        if r == 'H':
            cH += 1
        elif r == 'D':
            cD += 1
        elif r == 'A':
            cA += 1
    tam = len(resultado)
    print("Clases predichas procentaje H(%0.4f) D(%0.04f) A(%0.04f)" % (cH/tam, cD/tam, cA/tam))




if __name__ == '__main__':
    fit()
    test()



