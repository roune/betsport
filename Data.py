"""
Created by Ricardo Morato
06/12/2017
"""

import pandas as pd

from League import League


class Data(object):
    def __init__(self, f, fout=None, attrs=None, averages=None):
        self.__data = pd.read_csv(f)
        self.__league = League(f)
        self.__attrs = None
        self.__averages = None
        self.__av = False

        if attrs is not None and averages is not None:
            self.__attrs = attrs
            self.__averages = averages
            self.__av = True
        self.__write_data_in_csv(fout)

    def __write_data_in_csv(self, fout):
        teams = []
        matches = {}

        for index, row in self.__data.iterrows():
            teams.append(row['HomeTeam'])

        teams = sorted(set(teams))

        for team in teams:
            matches[team] = self.__data[(self.__data.HomeTeam == team)][['Div', 'Date', 'HomeTeam', 'AwayTeam', 'FTR']] #  | (self.__data.AwayTeam == team)

        columns_dt = ['Div', 'Date', 'HomeTeam', 'AwayTeam', 'FTR']

        if not self.__av:
            columns = self.__league.get_match_day(0).columns.values.tolist()
        else:
            columns = self.__league.get_match_day_with_weighted_average(n=0, attrs=self.__attrs, averages=self.__averages).columns.values.tolist()

        home_columns = []
        away_columns = []
        print (columns)
        for column in columns:
            home_columns.append('HT' + column)
            away_columns.append('AT' + column)

        columns_dt = columns_dt + home_columns
        columns_dt = columns_dt + away_columns

        new_df = pd.DataFrame(columns=columns_dt)

        j = 0
        for team in teams:
            i = 0
            while i < len(matches[team]):

                if not self.__av:
                    if i == 0:
                        aux = self.__league.get_match_day(0).loc[:,self.__league.get_match_day(0).columns != 'Team']
                        match_day = self.__league.get_match_day(0)
                        aux *= 0
                        match_day.loc[:,self.__league.get_match_day(0).columns != 'Team'] = aux
                    else:
                        match_day = self.__league.get_match_day(i-1)
                else:
                    if i == 0:
                        aux = self.__league.get_match_day_with_weighted_average(n=0, attrs=self.__attrs, averages=self.__averages).loc[:,self.__league.get_match_day_with_weighted_average(n=0, attrs=self.__attrs, averages=self.__averages).columns != 'Team']
                        match_day = self.__league.get_match_day_with_weighted_average(n=0, attrs=self.__attrs, averages=self.__averages)
                        aux *= 0
                        match_day.loc[:,self.__league.get_match_day_with_weighted_average(n=0, attrs=self.__attrs, averages=self.__averages).columns != 'Team'] = aux
                    else:
                        match_day = self.__league.get_match_day_with_weighted_average(n=i-1, attrs=self.__attrs, averages=self.__averages)

                new_columns = []
                for column in columns:
                    new_columns.append('HT' + column)

                match_day.columns = new_columns
                home_team_data = match_day[match_day.HTTeam == matches[team].HomeTeam.values[i]]
            
                result = pd.merge(matches[team].iloc[[i]], home_team_data, left_on='HomeTeam', right_on='HTTeam')

                new_columns = []
                for column in columns:
                    new_columns.append('AT' + column)

                match_day.columns = new_columns
                away_team_data = match_day[match_day.ATTeam == matches[team].AwayTeam.values[i]]

                result = pd.merge(result, away_team_data, left_on='AwayTeam', right_on='ATTeam')

                new_df.loc[j] = result.loc[0]
                j += 1
                i += 1
        
        new_df.to_csv(fout, index=False)
