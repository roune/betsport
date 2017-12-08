from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB

from Data import Data
from League import League

if __name__ == '__main__':

    f = open('./output.csv', 'w')

    i = 2007
    while i <= 2017:
        print ('./datasets/SP1' + str(i) + '.csv')
        l = League('./datasets/SP1' + str(i) + '.csv')

        if i == 2007:
            names = ','.join(l.get_attr_names()[0]) + ',' + ','.join(l.get_attr_names()[1])
            f.write(names + '\n')

        j = 0
        if j != 2017:
            n = 38
        else:
            n = 9

        while j < n:
            for team in l.get_jornada_full(j):
                team_as_string = (str(team[0]).strip('[]') + ', ' + str(team[1]).strip('[]')).replace(' ', '')
                f.write(team_as_string + '\n')

            j += 1

        i += 1

    f.close()

    dataset = Data('./output.csv', True).get_data()

    features = dataset[:, :24]
    target = dataset[:, 24]
    features_train, features_test, target_train, target_test = train_test_split(features,
                                                                            target, test_size=0.33, random_state=10)
    clf = GaussianNB()
    clf.fit(features_train, target_train)
    target_pred = clf.predict(features_test)

    print target_pred

    print accuracy_score(target_test, target_pred, normalize=True)