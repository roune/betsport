"""
Created by Ricardo Morato
06/12/2017
"""

import copy

import numpy as np
import pandas as pd

from MatchDay import MatchDay


class League(object):
    def __init__(self, f, averages=False):
        self.__file = f
        self.__data = pd.read_csv(f)
        self.__date = '20' + self.__data.Date[0][-2:]
        self.__team_names = sorted(set(self.__data.HomeTeam.values))
        self.__match_days = []
        self.__set_match_days()

    # TO-DO
    def get_attr_names(self):
        yield

    def get_data(self):
        return self.__data

    def get_match_day(self, n=None):
        """
        :rtype: MatchDay
        """
        if n is None:
            raise ValueError('The param "n" is required.')

        return self.__match_days[n].get_classification()

    # In progess
    def get_match_day_with_weighted_average(self, n=None, attrs=None, averages=None):
        if n is None:
            raise ValueError('The param "n" is required.')
        if attrs is None:
            raise ValueError('The param "attrs" is required.')
        if averages is None:
            raise ValueError('The param "averages" is required.')

        attrs = attrs.split(',')
        averages = averages.split(',')
        averages = map(float, averages)
        n_averages = len(averages)

        match_day = self.__match_days[n]
        classification = match_day.get_classification()

        for attr in attrs:
            values = []

            for team in classification['Team'].values:
                attr_values = []

                index = (n - n_averages)

                if index < 0:
                    index = 0
                    averages = averages[n_averages - n : n_averages]
                    n_averages = n

                for md in self.__match_days[index : n + 1]:
                    attr_values.append(md.get_value(team, attr))

                average_values = [t - s for s, t in zip(attr_values, attr_values[1:])]

                if n_averages == 0:
                    n_averages = 1

                values.append(sum(np.multiply(average_values, averages)) / n_averages)

            classification[attr] = values

        return classification

    def get_date(self):
        return self.__date

    def get_team_names(self):
        return self.__team_names

    def __set_match_days(self):
        n_match_days = len(self.__data[(self.__data.HomeTeam == self.__team_names[0]) | (
            self.__data.AwayTeam == self.__team_names[0])]['Div'].values)

        i = 0
        while i < n_match_days:
            if i == 0:
                match_day = MatchDay(self.__team_names)
            else:
                match_day = copy.deepcopy(self.__match_days[i - 1])

            matches = {}
            for team in self.__team_names:
                matches[team] = self.__data[(self.__data.HomeTeam == team) | (self.__data.AwayTeam == team)][:]

            for team in self.__team_names:
                row = matches[team].iloc[[i]]
                result = row.FTR.all()

                if row.HomeTeam.all() == team:
                    if result == 'H':
                        match_day.add_home_win(team)
                    elif result == 'A':
                        match_day.add_home_loose(team)
                    else:
                        match_day.add_home_draw(team)

                    match_day.add_home_goals(team, int(row.HG)) if ('HG' in row.columns.values) else None
                    match_day.add_home_goals(team, int(row.FTHG)) if ('FTHG' in row.columns.values) else None
                    match_day.add_home_goals_against(team, int(row.AG)) if ('AG' in row.columns.values) else None
                    match_day.add_home_goals_against(team, int(row.FTAG)) if ('FTAG' in row.columns.values) else None
                    match_day.add_home_shoots(team, int(row.HS)) if ('HS' in row.columns.values) else None
                    match_day.add_home_shoots_against(team, int(row.AS)) if ('AS' in row.columns.values) else None
                    match_day.add_home_shoots_on_target(team, int(row.HST)) if ('HST' in row.columns.values) else None
                    match_day.add_home_shoots_against_on_target(team, int(row.AST)) if (
                        'AST' in row.columns.values) else None
                    match_day.add_home_shoots_hit_woodwork(team, int(row.HHW)) if (
                        'HHW' in row.columns.values) else None
                    match_day.add_home_shoots_against_hit_woodwork(team, int(row.AHW)) if (
                        'AHW' in row.columns.values) else None
                    match_day.add_home_corners(team, int(row.HC)) if ('HC' in row.columns.values) else None
                    match_day.add_home_corners_against(team, int(row.AC)) if ('AC' in row.columns.values) else None
                    match_day.add_home_fouls(team, int(row.HF)) if ('HF' in row.columns.values) else None
                    match_day.add_home_fouls_received(team, int(row.AF)) if ('AF' in row.columns.values) else None
                    match_day.add_home_offsides(team, int(row.HO)) if ('HO' in row.columns.values) else None
                    match_day.add_home_offsides_against(team, int(row.AO)) if ('AO' in row.columns.values) else None
                    match_day.add_home_yellow_cards(team, int(row.HY)) if ('HY' in row.columns.values) else None
                    match_day.add_home_yellow_cards_against(team, int(row.AY)) if ('AY' in row.columns.values) else None
                    match_day.add_home_red_cards(team, int(row.HR)) if ('HR' in row.columns.values) else None
                    match_day.add_home_red_cards_against(team, int(row.AR)) if ('AR' in row.columns.values) else None
                else:
                    if result == 'H':
                        match_day.add_away_loose(team)
                    elif result == 'A':
                        match_day.add_away_win(team)
                    else:
                        match_day.add_away_draw(team)

                    match_day.add_away_goals(team, int(row.AG)) if ('AG' in row.columns.values) else None
                    match_day.add_away_goals(team, int(row.FTAG)) if ('FTAG' in row.columns.values) else None
                    match_day.add_away_goals_against(team, int(row.HG)) if ('HG' in row.columns.values) else None
                    match_day.add_away_goals_against(team, int(row.FTHG)) if ('FTHG' in row.columns.values) else None
                    match_day.add_away_shoots(team, int(row.AS)) if ('AS' in row.columns.values) else None
                    match_day.add_away_shoots_against(team, int(row.HS)) if ('HS' in row.columns.values) else None
                    match_day.add_away_shoots_on_target(team, int(row.AST)) if ('AST' in row.columns.values) else None
                    match_day.add_away_shoots_against_on_target(team, int(row.HST)) if (
                        'HST' in row.columns.values) else None
                    match_day.add_away_shoots_hit_woodwork(team, int(row.AHW)) if (
                        'AHW' in row.columns.values) else None
                    match_day.add_away_shoots_against_hit_woodwork(team, int(row.HHW)) if (
                        'HHW' in row.columns.values) else None
                    match_day.add_away_corners(team, int(row.AC)) if ('AC' in row.columns.values) else None
                    match_day.add_away_corners_against(team, int(row.HC)) if ('HC' in row.columns.values) else None
                    match_day.add_away_fouls(team, int(row.AF)) if ('AF' in row.columns.values) else None
                    match_day.add_away_fouls_received(team, int(row.HF)) if ('HF' in row.columns.values) else None
                    match_day.add_away_offsides(team, int(row.AO)) if ('AO' in row.columns.values) else None
                    match_day.add_away_offsides_against(team, int(row.HO)) if ('HO' in row.columns.values) else None
                    match_day.add_away_yellow_cards(team, int(row.AY)) if ('AY' in row.columns.values) else None
                    match_day.add_away_yellow_cards_against(team, int(row.HY)) if ('HY' in row.columns.values) else None
                    match_day.add_away_red_cards(team, int(row.AR)) if ('AR' in row.columns.values) else None
                    match_day.add_away_red_cards_against(team, int(row.HR)) if ('HR' in row.columns.values) else None

            match_day.set_positions()

            self.__match_days.append(match_day)

            i += 1
