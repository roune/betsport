import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder

def fit():
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
    clf = RandomForestClassifier(bootstrap=True, class_weight= None, criterion= 'entropy', max_depth= 6, min_samples_leaf= 2, min_samples_split= 10, n_estimators= 1000, n_jobs=6)
    scores = cross_val_score(clf, X, y)

    print("Accuracy: %0.4f (+/- %0.4f)" % (scores.mean(), scores.std() * 2))



def test():
    lenc = LabelEncoder()
    data1=pd.read_csv('./Datasets/SP1-2012_normAverage.csv')
    data2 = pd.read_csv('./Datasets/SP1-2013_normAverage.csv')
    data3 = pd.read_csv('./Datasets/SP1-2014_normAverage.csv')
    data4 = pd.read_csv('./Datasets/SP1-2015_normAverage.csv')
    data5 = pd.read_csv('./Datasets/SP1-2016_normAverage.csv')

    data =  pd.concat([data1,data2, data3, data4])

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
    clf = RandomForestClassifier(max_features='log2', n_estimators= 1000, n_jobs=6)
    clf.fit(X,y)

    y_dft = data5['FTR']
    x_dft = data5.loc[:,data5.columns != 'FTR']
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



