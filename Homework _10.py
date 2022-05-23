# Homework 10

# EXERCISE 10.2 (SERIES)
# Create pd.Series where 'index' contains days of the current month and 'data' contains some numbers (temperatures at noon, currency rates, ...).
from operator import index
import pandas as pd
import matplotlib.pyplot as plt

MayDates = pd.date_range("20220502", periods=22)

EURtoPLNmay2022 = pd.Series(data =[4.6850, 4.6925, 4.6875, 4.6673, 4.7028,'','', 4.6985, 4.6763, 4.6575, 4.6680, 4.6883,'','' , 4.6675,	4.6488,	4.6443,	4.6423,	4.6365, '','', 4.6210 ], index = MayDates)
print(EURtoPLNmay2022)

# EXERCISE 10.3 (DATAFRAME)
# Create pd.DataFrame for the periodic tablet (ten elemens). Column names are 'Name', 'Symbol', 'Weight'. 'index' starts from 1 for hydrogen.

name = pd.Series(['Hydrogen', 'Helium', 'Lithium', 'Berillium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon'])
symbol = pd.Series(['H','He','Li','Be','B','C','N','O','F','Ne'])
weight = pd.Series([1.00797, 4.00260, 6.941, 9.01218, 10.81, 12.011, 14.0067, 15.9994, 18.998403, 20.179])

PeriodicTable = pd.DataFrame({'Name': name, 'Symbol':symbol, 'Weight':weight})
PeriodicTable.index += 1
print(PeriodicTable)