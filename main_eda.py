#imports
import pandas as pd
import matplotlib.pyplot as plt

#open the csv and work with it as usual

def func():
    df = pd.read_csv('datasets/management_consulting_final.csv', sep=',')
    return df.head()