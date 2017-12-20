"""
Created by Ricardo Morato
06/12/2017
"""

import numpy as np
import pandas as pd


class MatchDay(object):
    def __init__(self, teams):
        self.__attr_names = ['Team', 'Points',
                             'Wins', 'Draws', 'Looses',
                             'HomeWins', 'HomeDraws', 'HomeLooses',
                             'AwayWins', 'AwayDraws', 'AwayLooses',
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
        self.__numeric_attr = ['Points',
                               'Wins', 'Draws', 'Looses',
                               'HomeWins', 'HomeDraws', 'HomeLooses',
                               'AwayWins', 'AwayDraws', 'AwayLooses',
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
        self.__classification = pd.DataFrame(np.zeros((len(teams), len(self.__attr_names))), columns=self.__attr_names)
        self.__classification[self.__numeric_attr] = self.__classification[self.__numeric_attr].astype(float)
        self.__classification['Team'] = teams

    def get_attr_names(self):
        return self.__attr_names

    def get_classification(self):
        return self.__classification.sort_values(by=['Points'], ascending=False)

    def get_team(self, team):
        return self.__classification[self.__classification.Team == team]

    def get_value(self, team, column):
        return self.__classification[self.__classification.Team == team][column].values[0]

    def set_positions(self):
        classification = self.__classification.sort_values(by='Points', ascending=False)
        rows = classification.shape[0]

        i = 1
        while i <= rows:
            classification.at[classification.index[i-1], 'Position'] = i
            i += 1

        self.__classification = classification

    def add_home_win(self, team):
        old_value = self.__classification[self.__classification.Team == team].HomeWins
        self.__classification.at[self.__classification.Team == team, 'HomeWins'] = old_value + 1
        self.add_win(team)

    def add_home_draw(self, team):
        old_value = self.__classification[self.__classification.Team == team].HomeDraws
        self.__classification.at[self.__classification.Team == team, 'HomeDraws'] = old_value + 1
        self.add_draw(team)

    def add_home_loose(self, team):
        old_value = self.__classification[self.__classification.Team == team].HomeLooses
        self.__classification.at[self.__classification.Team == team, 'HomeLooses'] = old_value + 1
        self.add_loose(team)

    def add_away_win(self, team):
        old_value = self.__classification[self.__classification.Team == team].AwayWins
        self.__classification.at[self.__classification.Team == team, 'AwayWins'] = old_value + 1
        self.add_win(team)

    def add_away_draw(self, team):
        old_value = self.__classification[self.__classification.Team == team].AwayDraws
        self.__classification.at[self.__classification.Team == team, 'AwayDraws'] = old_value + 1
        self.add_draw(team)

    def add_away_loose(self, team):
        old_value = self.__classification[self.__classification.Team == team].AwayLooses
        self.__classification.at[self.__classification.Team == team, 'AwayLooses'] = old_value + 1
        self.add_loose(team)

    def add_win(self, team):
        old_value = self.__classification[self.__classification.Team == team].Wins
        self.__classification.at[self.__classification.Team == team, 'Wins'] = old_value + 1
        old_value = self.__classification[self.__classification.Team == team].Points
        self.__classification.at[self.__classification.Team == team, 'Points'] = old_value + 3

    def add_draw(self, team):
        old_value = self.__classification[self.__classification.Team == team].Draws
        self.__classification.at[self.__classification.Team == team, 'Draws'] = old_value + 1
        old_value = self.__classification[self.__classification.Team == team].Points
        self.__classification.at[self.__classification.Team == team, 'Points'] = old_value + 1

    def add_loose(self, team):
        old_value = self.__classification[self.__classification.Team == team].Looses
        self.__classification.at[self.__classification.Team == team, 'Looses'] = old_value + 1

    def add_goals(self, team, goals):
        old_value = self.__classification[self.__classification.Team == team].Goals
        self.__classification.at[self.__classification.Team == team, 'Goals'] = goals + old_value

    def add_goals_against(self, team, goals):
        old_value = self.__classification[self.__classification.Team == team].GoalsAgainst
        self.__classification.at[self.__classification.Team == team, 'GoalsAgainst'] = goals + old_value

    def add_home_goals(self, team, goals):
        old_value = self.__classification[self.__classification.Team == team].HomeGoals
        self.__classification.at[self.__classification.Team == team, 'HomeGoals'] = goals + old_value
        self.add_goals(team, goals)

    def add_home_goals_against(self, team, goals):
        old_value = self.__classification[self.__classification.Team == team].HomeGoalsAgainst
        self.__classification.at[self.__classification.Team == team, 'HomeGoalsAgainst'] = goals + old_value
        self.add_goals_against(team, goals)

    def add_away_goals(self, team, goals):
        old_value = self.__classification[self.__classification.Team == team].AwayGoals
        self.__classification.at[self.__classification.Team == team, 'AwayGoals'] = goals + old_value
        self.add_goals(team, goals)

    def add_away_goals_against(self, team, goals):
        old_value = self.__classification[self.__classification.Team == team].AwayGoalsAgainst
        self.__classification.at[self.__classification.Team == team, 'AwayGoalsAgainst'] = goals + old_value
        self.add_goals_against(team, goals)

    def add_shoots(self, team, shoots):
        old_value = self.__classification[self.__classification.Team == team].Shoots
        self.__classification.at[self.__classification.Team == team, 'Shoots'] = shoots + old_value

    def add_shoots_against(self, team, shoots):
        old_value = self.__classification[self.__classification.Team == team].ShootsAgainst
        self.__classification.at[self.__classification.Team == team, 'ShootsAgainst'] = shoots + old_value

    def add_home_shoots(self, team, shoots):
        old_value = self.__classification[self.__classification.Team == team].HomeShoots
        self.__classification.at[self.__classification.Team == team, 'HomeShoots'] = shoots + old_value
        self.add_shoots(team, shoots)

    def add_away_shoots(self, team, shoots):
        old_value = self.__classification[self.__classification.Team == team].AwayShoots
        self.__classification.at[self.__classification.Team == team, 'AwayShoots'] = shoots + old_value
        self.add_shoots(team, shoots)

    def add_home_shoots_against(self, team, shoots):
        old_value = self.__classification[self.__classification.Team == team].HomeShootsAgainst
        self.__classification.at[self.__classification.Team == team, 'HomeShootsAgainst'] = shoots + old_value
        self.add_shoots_against(team, shoots)

    def add_away_shoots_against(self, team, shoots):
        old_value = self.__classification[self.__classification.Team == team].AwayShootsAgainst
        self.__classification.at[self.__classification.Team == team, 'AwayShootsAgainst'] = shoots + old_value
        self.add_shoots_against(team, shoots)

    def add_shoots_on_target(self, team, shoots):
        old_value = self.__classification[self.__classification.Team == team].ShootsOnTarget
        self.__classification.at[self.__classification.Team == team, 'ShootsOnTarget'] = shoots + old_value

    def add_shoots_against_on_target(self, team, shoots):
        old_value = self.__classification[self.__classification.Team == team].ShootsAgainstOnTarget
        self.__classification.at[self.__classification.Team == team, 'ShootsAgainstOnTarget'] = shoots + old_value

    def add_home_shoots_on_target(self, team, shoots):
        old_value = self.__classification[self.__classification.Team == team].HomeShootsOnTarget
        self.__classification.at[self.__classification.Team == team, 'HomeShootsOnTarget'] = shoots + old_value
        self.add_shoots_on_target(team, shoots)

    def add_away_shoots_on_target(self, team, shoots):
        old_value = self.__classification[self.__classification.Team == team].AwayShootsOnTarget
        self.__classification.at[self.__classification.Team == team, 'AwayShootsOnTarget'] = shoots + old_value

    def add_home_shoots_against_on_target(self, team, shoots):
        old_value = self.__classification[self.__classification.Team == team].HomeShootsAgainstOnTarget
        self.__classification.at[self.__classification.Team == team, 'HomeShootsAgainstOnTarget'] = shoots + old_value
        self.add_shoots_against_on_target(team, shoots)

    def add_away_shoots_against_on_target(self, team, shoots):
        old_value = self.__classification[self.__classification.Team == team].AwayShootsAgainstOnTarget
        self.__classification.at[self.__classification.Team == team, 'AwayShootsAgainstOnTarget'] = shoots + old_value
        self.add_shoots_against_on_target(team, shoots)

    def add_shoots_hit_woodwork(self, team, shoots):
        old_value = self.__classification[self.__classification.Team == team].ShootsHitWoodwork
        self.__classification.at[self.__classification.Team == team, 'ShootsHitWoodwork'] = shoots + old_value

    def add_shoots_against_hit_woodwork(self, team, shoots):
        old_value = self.__classification[self.__classification.Team == team].ShootsAgainstHitWoodwork
        self.__classification.at[self.__classification.Team == team, 'ShootsAgainstHitWoodwork'] = shoots + old_value

    def add_home_shoots_hit_woodwork(self, team, shoots):
        old_value = self.__classification[self.__classification.Team == team].HomeShootsHitWoodwork
        self.__classification.at[self.__classification.Team == team, 'HomeShootsHitWoodwork'] = shoots + old_value
        self.add_shoots_hit_woodwork(team, shoots)

    def add_away_shoots_hit_woodwork(self, team, shoots):
        old_value = self.__classification[self.__classification.Team == team].AwayShootsHitWoodwork
        self.__classification.at[self.__classification.Team == team, 'AwayShootsHitWoodwork'] = shoots + old_value
        self.add_shoots_hit_woodwork(team, shoots)

    def add_home_shoots_against_hit_woodwork(self, team, shoots):
        old_value = self.__classification[self.__classification.Team == team].HomeShootsAgainstHitWoodwork
        self.__classification.at[
            self.__classification.Team == team, 'HomeShootsAgainstHitWoodwork'] = shoots + old_value
        self.add_shoots_against_hit_woodwork(team, shoots)

    def add_away_shoots_against_hit_woodwork(self, team, shoots):
        old_value = self.__classification[self.__classification.Team == team].AwayShootsAgainstHitWoodwork
        self.__classification.at[
            self.__classification.Team == team, 'AwayShootsAgainstHitWoodwork'] = shoots + old_value
        self.add_shoots_against_hit_woodwork(team, shoots)

    def add_corners(self, team, corners):
        old_value = self.__classification[self.__classification.Team == team].Corners
        self.__classification.at[self.__classification.Team == team, 'Corners'] = corners + old_value

    def add_against_corners(self, team, corners):
        old_value = self.__classification[self.__classification.Team == team].CornersAgainst
        self.__classification.at[self.__classification.Team == team, 'CornersAgainst'] = corners + old_value

    def add_home_corners(self, team, corners):
        old_value = self.__classification[self.__classification.Team == team].HomeCorners
        self.__classification.at[self.__classification.Team == team, 'HomeCorners'] = corners + old_value
        self.add_corners(team, corners)

    def add_away_corners(self, team, corners):
        old_value = self.__classification[self.__classification.Team == team].AwayCorners
        self.__classification.at[self.__classification.Team == team, 'AwayCorners'] = corners + old_value
        self.add_corners(team, corners)

    def add_home_corners_against(self, team, corners):
        old_value = self.__classification[self.__classification.Team == team].HomeCornersAgainst
        self.__classification.at[self.__classification.Team == team, 'HomeCornersAgainst'] = corners + old_value
        self.add_against_corners(team, corners)

    def add_away_corners_against(self, team, corners):
        old_value = self.__classification[self.__classification.Team == team].AwayCornersAgainst
        self.__classification.at[self.__classification.Team == team, 'AwayCornersAgainst'] = corners + old_value
        self.add_against_corners(team, corners)

    def add_fouls(self, team, fouls):
        old_value = self.__classification[self.__classification.Team == team].Fouls
        self.__classification.at[self.__classification.Team == team, 'Fouls'] = fouls + old_value

    def add_received_fouls(self, team, fouls):
        old_value = self.__classification[self.__classification.Team == team].FoulsReceived
        self.__classification.at[self.__classification.Team == team, 'FoulsReceived'] = fouls + old_value

    def add_home_fouls(self, team, fouls):
        old_value = self.__classification[self.__classification.Team == team].HomeFouls
        self.__classification.at[self.__classification.Team == team, 'HomeFouls'] = fouls + old_value
        self.add_fouls(team, fouls)

    def add_away_fouls(self, team, fouls):
        old_value = self.__classification[self.__classification.Team == team].AwayFouls
        self.__classification.at[self.__classification.Team == team, 'AwayFouls'] = fouls + old_value
        self.add_fouls(team, fouls)

    def add_home_fouls_received(self, team, fouls):
        old_value = self.__classification[self.__classification.Team == team].HomeFoulsReceived
        self.__classification.at[self.__classification.Team == team, 'HomeFoulsReceived'] = fouls + old_value
        self.add_received_fouls(team, fouls)

    def add_away_fouls_received(self, team, fouls):
        old_value = self.__classification[self.__classification.Team == team].AwayFoulsReceived
        self.__classification.at[self.__classification.Team == team, 'AwayFoulsReceived'] = fouls + old_value
        self.add_received_fouls(team, fouls)

    def add_offsides(self, team, offsides):
        old_value = self.__classification[self.__classification.Team == team].Offsides
        self.__classification.at[self.__classification.Team == team, 'Offsides'] = offsides + old_value

    def add_offsides_against(self, team, offsides):
        old_value = self.__classification[self.__classification.Team == team].OffsidesAgainst
        self.__classification.at[self.__classification.Team == team, 'OffsidesAgainst'] = offsides + old_value

    def add_home_offsides(self, team, offsides):
        old_value = self.__classification[self.__classification.Team == team].HomeOffsides
        self.__classification.at[self.__classification.Team == team, 'HomeOffsides'] = offsides + old_value
        self.add_offsides(team, offsides)

    def add_away_offsides(self, team, offsides):
        old_value = self.__classification[self.__classification.Team == team].AwayOffsides
        self.__classification.at[self.__classification.Team == team, 'AwayOffsides'] = offsides + old_value
        self.add_offsides(team, offsides)

    def add_home_offsides_against(self, team, offsides):
        old_value = self.__classification[self.__classification.Team == team].HomeOffsidesAgainst
        self.__classification.at[self.__classification.Team == team, 'HomeOffsidesAgainst'] = offsides + old_value
        self.add_offsides_against(team, offsides)

    def add_away_offsides_against(self, team, offsides):
        old_value = self.__classification[self.__classification.Team == team].AwayOffsidesAgainst
        self.__classification.at[self.__classification.Team == team, 'AwayOffsidesAgainst'] = offsides + old_value
        self.add_offsides_against(team, offsides)

    def add_yellow_cards(self, team, yellow_cards):
        old_value = self.__classification[self.__classification.Team == team].YellowCards
        self.__classification.at[self.__classification.Team == team, 'YellowCards'] = yellow_cards + old_value

    def add_yellow_cards_against(self, team, yellow_cards):
        old_value = self.__classification[self.__classification.Team == team].YellowCardsAgainst
        self.__classification.at[self.__classification.Team == team, 'YellowCardsAgainst'] = yellow_cards + old_value

    def add_home_yellow_cards(self, team, yellow_cards):
        old_value = self.__classification[self.__classification.Team == team].HomeYellowCards
        self.__classification.at[self.__classification.Team == team, 'HomeYellowCards'] = yellow_cards + old_value
        self.add_yellow_cards(team, yellow_cards)

    def add_away_yellow_cards(self, team, yellow_cards):
        old_value = self.__classification[self.__classification.Team == team].AwayYellowCards
        self.__classification.at[self.__classification.Team == team, 'AwayYellowCards'] = yellow_cards + old_value
        self.add_yellow_cards(team, yellow_cards)

    def add_home_yellow_cards_against(self, team, yellow_cards):
        old_value = self.__classification[self.__classification.Team == team].HomeYellowCardsAgainst
        self.__classification.at[
            self.__classification.Team == team, 'HomeYellowCardsAgainst'] = yellow_cards + old_value
        self.add_yellow_cards_against(team, yellow_cards)

    def add_away_yellow_cards_against(self, team, yellow_cards):
        old_value = self.__classification[self.__classification.Team == team].AwayYellowCardsAgainst
        self.__classification.at[
            self.__classification.Team == team, 'AwayYellowCardsAgainst'] = yellow_cards + old_value
        self.add_yellow_cards_against(team, yellow_cards)

    def add_red_cards(self, team, red_cards):
        old_value = self.__classification[self.__classification.Team == team].RedCards
        self.__classification.at[self.__classification.Team == team, 'RedCards'] = red_cards + old_value

    def add_red_cards_against(self, team, red_cards):
        old_value = self.__classification[self.__classification.Team == team].RedCardsAgainst
        self.__classification.at[self.__classification.Team == team, 'RedCardsAgainst'] = red_cards + old_value

    def add_home_red_cards(self, team, red_cards):
        old_value = self.__classification[self.__classification.Team == team].HomeRedCards
        self.__classification.at[self.__classification.Team == team, 'HomeRedCards'] = red_cards + old_value
        self.add_yellow_cards(team, red_cards)

    def add_away_red_cards(self, team, red_cards):
        old_value = self.__classification[self.__classification.Team == team].AwayRedCards
        self.__classification.at[self.__classification.Team == team, 'AwayRedCards'] = red_cards + old_value
        self.add_yellow_cards(team, red_cards)

    def add_home_red_cards_against(self, team, red_cards):
        old_value = self.__classification[self.__classification.Team == team].HomeRedCardsAgainst
        self.__classification.at[self.__classification.Team == team, 'HomeRedCardsAgainst'] = red_cards + old_value
        self.add_yellow_cards_against(team, red_cards)

    def add_away_red_cards_against(self, team, red_cards):
        old_value = self.__classification[self.__classification.Team == team].AwayRedCardsAgainst
        self.__classification.at[self.__classification.Team == team, 'AwayRedCardsAgainst'] = red_cards + old_value
        self.add_yellow_cards_against(team, red_cards)
