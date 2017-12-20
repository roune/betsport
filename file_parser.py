from Data import Data

if __name__ == '__main__':

    averages_fields = ['Wins', 'Draws', 'Looses',
                   'Goals', 'GoalsAgainst',
                   'HomeGoals', 'AwayGoals',
                   'HomeGoalsAgainst', 'AwayGoalsAgainst',
                   'Position',
                   'Shoots', 'ShootsAgainst',
                   'HomeShoots', 'AwayShoots',
                   'HomeShootsAgainst', 'AwayShootsAgainst',
                   'ShootsOnTarget', 'ShootsAgainstOnTarget',
                   'HomeShootsOnTarget', 'AwayShootsOnTarget',
                   'HomeShootsAgainstOnTarget', 'AwayShootsAgainstOnTarget',
                   'ShootsHitWoodwork', 'ShootsAgainstHitWoodwork',
                   'HomeShootsHitWoodwork', 'AwayShootsHitWoodwork',
                   'HomeShootsAgainstHitWoodwork', 'AwayShootsAgainstHitWoodwork',
                   'Corners', 'CornersAgainst',
                   'HomeCorners', 'AwayCorners',
                   'HomeCornersAgainst', 'AwayCornersAgainst',
                   'Fouls', 'FoulsReceived',
                   'HomeFouls', 'AwayFouls',
                   'HomeFoulsReceived', 'AwayFoulsReceived',
                   'Offsides', 'OffsidesAgainst',
                   'HomeOffsides', 'AwayOffsides',
                   'HomeOffsidesAgainst', 'AwayOffsidesAgainst',
                   'YellowCards', 'YellowCardsAgainst',
                   'HomeYellowCards', 'AwayYellowCards',
                   'HomeYellowCardsAgainst', 'AwayYellowCardsAgainst',
                   'RedCards', 'RedCardsAgainst',
                   'HomeRedCards', 'AwayRedCards',
                   'HomeRedCardsAgainst', 'AwayRedCardsAgainst']

    #d = Data('./Datasets/SP1-2017.csv', './Datasets/SP1-2017_data.csv')
    d = Data('./Datasets/SP1-2016.csv', './Datasets/SP1-2016_weightedAverage.csv', attrs=','.join(averages_fields), averages='5,4,3,2,1')
    print "Finalizado el primer dataset"
    d = Data('./Datasets/SP1-2015.csv', './Datasets/SP1-2015_weightedAverage.csv', attrs=','.join(averages_fields), averages='5,4,3,2,1')
    print "Finalizado el segundo dataset"
    d = Data('./Datasets/SP1-2014.csv', './Datasets/SP1-2014_weightedAverage.csv', attrs=','.join(averages_fields), averages='5,4,3,2,1')
    print "Finalizado el tercer dataset"
    d = Data('./Datasets/SP1-2013.csv', './Datasets/SP1-2013_weightedAverage.csv', attrs=','.join(averages_fields), averages='5,4,3,2,1')
    print "Finalizado el penultimo dataset"
    d = Data('./Datasets/SP1-2012.csv', './Datasets/SP1-2012_weightedAverage.csv', attrs=','.join(averages_fields), averages='5,4,3,2,1')

