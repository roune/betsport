from time import time

import numpy as np
from scipy.stats import randint as sp_randint
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import StratifiedKFold
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

    # Cross Validation a usar y numero maximo de iteraciones
    cv = StratifiedKFold(n_splits=10, shuffle=True).split(X, y)
    n_iter_search = 40


    clfRF = RandomForestClassifier()
    param_RF = {"max_depth": [6, None],
                "n_estimators":sp_randint(200, 1000),
                "min_samples_split": sp_randint(2, 11),
                "min_samples_leaf": sp_randint(1, 11),
                "bootstrap": [True, False],
                "criterion": ["gini", "entropy"],
                "class_weight": ['balanced', None]}


    rsRF = RandomizedSearchCV(clfRF, param_distributions=param_RF,
                                       n_iter=n_iter_search,n_jobs=-1,cv=cv)

    start = time()
    rsRF.fit(X, y)
    print("RandomForestClassifier:")
    print("RandomizedSearchCV tarda %.2f seconds"
          " opciones de los parametros." % ((time() - start)))
    report(rsRF.cv_results_)

    clfSVC = SVC()
    param_SVC = {"C": sp_randint(1, 1000),
                 "gamma": [0.0001,0.001,"auto"],
                 "degree": sp_randint(3,20),
                 "kernel": ["linear", "polynomial","rbf","sigmoid"],
                 "class_weight":['balanced',None]}


    rsSVC = RandomizedSearchCV(clfSVC, param_distributions=param_SVC,
                              n_iter=n_iter_search, n_jobs=-1,cv=cv)

    start = time()
    rsSVC.fit(X, y)
    print("RandomizedSearchCV tarda %.2f seconds"
          " opciones de los parametros." % ((time() - start)))
    report(rsSVC.cv_results_)


    clfET = ExtraTreesClassifier()
    rsET = RandomizedSearchCV(clfET, param_distributions=param_RF,
                              n_iter=n_iter_search, n_jobs=-1, cv=cv)

    start = time()
    rsET.fit(X, y)
    print("RandomizedSearchCV tarda %.2f seconds"
          " opciones de los parametros." % ((time() - start)))
    report(rsET.cv_results_)

