#import matplotlib.pyplot as plt
import pandas as pd
import pathlib

parent = pathlib.Path(__file__).parent
print(parent)

sc_background = pd.read_csv(pathlib.Path(__file__).parent / 'sc_background.csv')
print(sc_background.head())