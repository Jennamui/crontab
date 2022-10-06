#import packages
import os
import sys
import time
import pandas as pd

#get current working directory
cwd = os.getcwd()

#print cwd
print(cwd)

# get the current time
now = time.time()

# save current time as a string
nowStr = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(now))


#import dataset
df= pd.read_csv('https://healthdata.gov/resource/di4u-7yu6.csv')

df.to_csv('/Users/jennamui/Documents/GitHub/crontab')
