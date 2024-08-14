import pandas as pd
pd.set_option('display.max_colwidth', None)

#preprocessing the data csv file
df = pd.read_csv("movies.csv")
df = df[ ["genres", "keywords", "title", "overview", "vote_average", "cast", "director"]]
df = df.dropna(subset=df.columns)   #droped na values column    
print(df.columns)

