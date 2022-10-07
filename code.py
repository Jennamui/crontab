#import packages
import os
import sys
import pandas as pd

#import dataset
df= pd.read_csv('https://healthdata.gov/resource/di4u-7yu6.csv')

df.to_csv('/home/jenna_mui/crontab/data.csv')
