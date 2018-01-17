from sklearn.preprocessing import LabelEncoder
import numpy as np
import pandas as pd
from sklearn.model_selection import RandomizedSearchCV, cross_val_score, StratifiedKFold


if __name__ == '__main__':

    lenc = LabelEncoder()
    data=pd.read_csv('./Datasets/SP1-2016_data.csv')

    y_df = data['HTR']
    x_df = data.loc[:,data.columns != 'HTR']
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
    cv = StratifiedKFold(n_splits=10, shuffle=True).split(X, y)
