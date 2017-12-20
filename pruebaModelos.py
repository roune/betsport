from time import time

import numpy as np
import pandas as pd
from scipy.stats import randint as sp_randint
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import RandomizedSearchCV, cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC


def report(results, n_top=3):
    '''
    :param results: Resultados del clasidicador
    :param n_top: Numero de puestos a mostrar
    '''
    for i in range(1, n_top + 1):
        candidates = np.flatnonzero(results['rank_test_score'] == i)
        for candidate in candidates:
            print("Modelo posicion: {0}".format(i))
            print("Acierto: {0:.3f} (std: {1:.3f})".format(
                results['mean_test_score'][candidate],
                results['std_test_score'][candidate]))
            print("Parametros Modelo: {0}".format(results['params'][candidate]))
            print("")

if __name__ == '__main__':

    lenc = LabelEncoder()
    data=pd.read_csv('./Datasets/SP1_data.csv')

    y_df = data['HTR']
    x_df = data.loc[:,data.columns != 'HTR']
    y = lenc.fit_transform(np.array(y_df))
    X = np.array(x_df.loc[:,[True if c not in  ['Div','Date','HomeTeam','AwayTeam','HTTeam','ATTeam'] else False for c in x_df.columns]])
    # Cross Validation a usar y numero maximo de iteraciones
    cv = StratifiedKFold(n_splits=10, shuffle=True).split(X, y)
    n_iter_search = 20


    clfRF = RandomForestClassifier()
    param_RF = {"max_depth": [6, None],
                 "n_estimators":sp_randint(500, 1000),
                 "min_samples_split": sp_randint(2, 11),
                 "min_samples_leaf": sp_randint(1, 11),
                 "bootstrap": [True, False],
                 "criterion": ["gini", "entropy"],
                 "class_weight": ['balanced', None]}
    #
    #
    #rsRF = RandomizedSearchCV(clfRF, param_distributions=param_RF,
    #                                    n_iter=n_iter_search,n_jobs=-1,cv=cv)

    #start = time()
    #rsRF.fit(X, y)
    #print("RandomForestClassifier:")
    #print("RandomizedSearchCV tarda %.2f segundos"
    #      " opciones de los parametros." % ((time() - start)))
    #report(rsRF.cv_results_)

    # clfSVC = SVC()
    # param_SVC = {"C": sp_randint(1, 1000),
    #              "gamma": [0.0001,0.001,"auto"],
    #              "degree": sp_randint(3,20),
    #              "kernel": ["linear","rbf","sigmoid"],
    #              "class_weight":['balanced',None]}
    #
    #
    # rsSVC = RandomizedSearchCV(clfSVC, param_distributions=param_SVC,
    #                           n_iter=n_iter_search, n_jobs=-1,cv=cv)
    #
    # start = time()
    # rsSVC.fit(X, y)
    # print("SVC:")
    # print("RandomizedSearchCV tarda %.2f segundos"
    #       " opciones de los parametros." % ((time() - start)))
    # report(rsSVC.cv_results_)

    #clfSVCBest = SVC(C=947, class_weight=None, degree=10, gamma=0.001, kernel='sigmoid',probability=True)
    #clfAda=AdaBoostClassifier(base_estimator=clfSVCBest)

    param_ADA = {
        "n_estimators":sp_randint(200, 1000),
        "learning_rate": [0.001,0.01,0.1,1]
    }

    # rsADA = RandomizedSearchCV(clfAda, param_distributions=param_ADA,
    #                           n_iter=n_iter_search, n_jobs=-1,cv=cv)

    #start = time()
    #rsADA.fit(X, y)
    #print("AdaBoost(SVC):")
    #print("RandomizedSearchCV tarda %.2f segundos"
    #      " opciones de los parametros." % ((time() - start)))
    #report(rsADA.cv_results_)

    # clfET = ExtraTreesClassifier()
    # rsET = RandomizedSearchCV(clfET, param_distributions=param_RF,
    #                           n_iter=n_iter_search, n_jobs=-1, cv=cv)
    #
    # start = time()
    # rsET.fit(X, y)
    # print("ExtraTreesClassifier:")
    # print("RandomizedSearchCV tarda %.2f segundos"
    #       " opciones de los parametros." % ((time() - start)))
    # report(rsET.cv_results_)


    ######### KNN #######
    clfKNN = KNeighborsClassifier()
    param_KNN = {
        "n_neighbors": [1, 3, 5, 7, 9, 11, 13],
        "algorithm": ["auto", "ball_tree", "kd_tree", "brute"],
        "weights": ["uniform", "distance"]
    }

    #rsKNN = RandomizedSearchCV(clfKNN, param_distributions=param_KNN,
    #                           n_iter=n_iter_search, n_jobs=-1, cv=cv)


    #start = time()
    #rsKNN.fit(X, y)
    #print("NearestNeighborClassifier:")
    #print("RandomizedSearchCV tarda %.2f segundos"
    #      " opciones de los parametros." % ((time() - start)))
    #report(rsKNN.cv_results_)



    ######### Logistic Regression #######
    clfLR = LogisticRegression()
    param_LR = {
        "tol": [0.01,0.05,0.1, 0.2, 0.5], #tolerance
        "multi_class": ["ovr", "multinomial"],
        "fit_intercept": [True, False],
        "solver": ["newton-cg", "sag", "saga", "lbfgs"]
    }

    rsLR = RandomizedSearchCV(clfLR, param_distributions=param_LR,
                              n_iter=n_iter_search, n_jobs=-1, cv=cv)

    start = time()
    rsLR.fit(X, y)
    print("LogisticRegressionClassifier:")
    print("RandomizedSearchCV tarda %.2f segundos"
         " opciones de los parametros." % ((time() - start)))
    report(rsLR.cv_results_)



    ######### NAIVE BAYES #######
    clfNB = GaussianNB()

    start = time()
    score = cross_val_score(clfNB, X, y, cv=cv)
    print("NaiveBayesClassifier:")
    print("NaiveBayesClassifier tarda %.2f segundos"
          " opciones de los parametros." % ((time() - start)))
    print("Acierto: ", np.mean(score))

