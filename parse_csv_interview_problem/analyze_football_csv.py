
import csv
import numpy as np
import pandas as pd


def file_setup():
    file = 'football_data.csv'
    return pandas_csv(file)

def read_data(data):
    with open(data, 'r') as f:
        data = [row for row in csv.reader(f.read().splitlines())]
    return data

def pandas_csv(csv_file):
    return pd.read_csv(csv_file)
    

def calc_goal_difference(df):
    df['Diff'] = df['Goals'] - df['Goals Allowed']
    return df

def calc_absolute_val_goal_diff(df):
    df['Absolute Diff'] = abs(df['Diff'])
    return df

def row_with_min_goal_diff(df):
    return df.loc[df['Absolute Diff'].idxmin()]

def team_name_min_goal_diff(df_row):
    return df_row['Team']

file = 'football_data.csv'
df = pandas_csv(file)

df['Diff'] = df['Goals'] - df['Goals Allowed']
df['Absolute Diff'] = abs(df['Diff'])

smallest_goal_diff_abs_value = df.loc[df['Absolute Diff'].idxmin()]
smallest_positive_goal_diff = df.loc[df.loc[df['Diff']>0]['Diff'].idxmin()]
most_negative_goal_diff = df.loc[df['Diff'].idxmin()]


if __name__ == '__main__':
    df = file_setup()
    df = calc_goal_difference(df)
    df = calc_absolute_val_goal_diff(df)
    row = row_with_min_goal_diff(df)
    print(team_name_min_goal_diff(row))
    