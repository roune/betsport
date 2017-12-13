
from sklearn.feature_selection import RFECV, SelectFromModel
from sklearn.metrics import accuracy_score
from sklearn.model_selection import StratifiedKFold, cross_val_predict



class selectBestFeatures(object):
    '''
    :Date 2017-12-08
    :Version: 1

    '''


    def __init__(self, clasificador):
        '''

        :param clasificador: Clasificador con el que se van a probar los parametros elegidos
        '''
        self.clasificador = clasificador


    def bestFeatures(self, df,cv=None):
       '''

       :param df:  Dataset con las clases en la columna FTR
       :type df: dataFrame
       :param cv:  Iterador cross validation (optional)
       :return:  Dataset
       '''

       y = df['FTR']
       X = df.loc[:,df.columns.value != 'FTR']
       claFit = self.clasificador.fit(X,y)

       if cv==None:
        cv =  StratifiedKFold(n_splits=10,shuffle=True).split(X,y)

       dfRFECV = RFECV(self.clasificador, step=1,cv=cv,n_jobs=-1).fit_transform(X,y)
       dfSelectModel = SelectFromModel(claFit).fit_transform(X,y)

       aciertoRFE = accuracy_score(dfRFECV[-1],cross_val_predict(claFit,dfRFECV[:,:-1],dfRFECV[-1],n_jobs=-1))
       aciertoModel = accuracy_score(dfSelectModel[-1],cross_val_predict(claFit,dfSelectModel[:,:-1],dfSelectModel[-1],n_jobs=-1))

       return dfRFECV if  aciertoRFE >= aciertoModel else dfSelectModel

