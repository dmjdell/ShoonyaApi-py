
import os
import pandas as pd


df = pd.read_csv("NFO_symbols.txt", sep = ',')
val = df [df.TradingSymbol.str.match('^BANKNIFTY28APR22')]
tokens =[]
for index, row in val.iterrows():
    print('NFO|'+ str(row['Token']))
