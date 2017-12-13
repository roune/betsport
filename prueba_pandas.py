from Data import Data

if __name__ == '__main__':

    '''lfp2017 = League('./Datasets/SP1_new.csv')

    print lfp2017.get_match_day_with_weighted_average(0, 'Goals,GoalsAgainst,Shoots,ShootsAgainst', '2,4,6')
    print lfp2017.get_match_day_with_weighted_average(1, 'Goals,GoalsAgainst,Shoots,ShootsAgainst', '2,4,6')
    print lfp2017.get_match_day_with_weighted_average(2, 'Goals,GoalsAgainst,Shoots,ShootsAgainst', '2,4,6')
    print lfp2017.get_match_day_with_weighted_average(3, 'Goals,GoalsAgainst,Shoots,ShootsAgainst', '2,4,6')
    l = lfp2017.get_match_day(0)
    l.to_csv('./Datasets/pandas.csv', sep=',', encoding='utf-8', mode='w')

    i = 1
    while i < 11:
        l = lfp2017.get_match_day(i)
        l.to_csv('./Datasets/pandas.csv', sep=',', encoding='utf-8', mode='a')
        i += 1'''

    d = Data('./Datasets/SP1_new.csv', './Datasets/SP1_data.csv', 'Goals,GoalsAgainst,Shoots,ShootsAgainst', '1,1,1,1,1')

