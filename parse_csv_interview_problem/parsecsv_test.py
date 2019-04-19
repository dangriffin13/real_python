import unittest
import pandas as pd
import json
import requests
from analyze_football_csv import read_data, pandas_csv, calc_goal_difference, calc_absolute_val_goal_diff, row_with_min_goal_diff, team_name_min_goal_diff


class ParseCSVTest(unittest.TestCase):

    def setUp(self):
        self.data = 'football_data.csv'

    def test_csv_headers(self):
        self.assertEqual(
            read_data(self.data)[0],
            ['Team','Games','Wins','Losses','Draws','Goals','Goals Allowed','Points'])

    def test_pandas_headers(self):
        self.assertEqual(pandas_csv(self.data).columns.tolist(), ['Team','Games','Wins','Losses','Draws','Goals','Goals Allowed','Points'])

    def test_calc_goal_difference(self):
        test_data = [
            ['Team', 'Goals', 'Goals Allowed'],
            ['Arsenal', 76, 36],
            ['Fulham', 36, 44],
            ['Everton', 45, 57]
        ]
        headers = test_data.pop(0)
        df = pd.DataFrame(test_data, columns=headers)
        df = calc_goal_difference(df)
        self.assertEqual(df['Diff'][1], -8)

    def test_absolute_val_goal_diff(self):
        test_data = [
            ['Team', 'Diff'],
            ['Arsenal', 43],
            ['Fulham', -8],
            ['Everton',-12]
        ]
        headers = test_data.pop(0)
        df = pd.DataFrame(test_data, columns=headers)
        self.assertEqual(calc_absolute_val_goal_diff(df)['Absolute Diff'].tolist(), [43, 8, 12])

    def test_row_with_min_goal_diff(self):
        test_data = [
            ['Team', 'Absolute Diff'],
            ['Arsenal', 43],
            ['Aston_Villa', 1],
            ['Everton', 12]
        ]
        headers = test_data.pop(0)
        df = pd.DataFrame(test_data, columns=headers)
        self.assertEqual(row_with_min_goal_diff(df).tolist(),['Aston_Villa', 1]) 

    def test_team_name(self):
        row = pd.Series(['Aston_Villa', -1, 1], index=['Team','Diff', 'Absolute Diff'])
        self.assertEqual(team_name_min_goal_diff(row), 'Aston_Villa')


if __name__ == '__main__':
    unittest.main()
    