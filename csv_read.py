#pip install pandas > voor het downloaden van libraries / databases etc. 
print('Start csv uitlezen applicatie')

import pandas

df = pandas.read_csv('pokemon.csv')
print(df["Name"])

for r, rij in df.iterrows():
    print(r)
    print(rij["Name"])
    print(rij["Attack"])
