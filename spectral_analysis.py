import matplotlib.pyplot as plt
import pandas as pd
import pathlib

sc_background = pd.read_csv(pathlib.Path(__file__).parent / 'data' / 'sc_background.csv')