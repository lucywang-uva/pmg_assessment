import sys
import csv
import os
import pandas as pd

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option('max_colwidth', None)


dfs = []

for i in range(1,len(sys. argv)):
    data = pd.read_csv("/Users/lucywang/Documents/fixtures/" + sys.argv[i]);
    data['filename'] = sys.argv[i]
    dfs.append(data);

print(pd.concat((dfs), ignore_index=True))
