# In this task it was necessary to Save the following part from the train.csv file to the train_part.csv file: lines
# where matches are greater than the average of the columns pos, reads_all, mismatches, deletions, insertions
import pandas as pd
from statistics import mean


df = pd.read_csv('C:\Python_programs\Homework_pandas\data_train.csv', sep = ',')
df = pd.DataFrame(df, dtype='float')
m = mean(df['matches'])
res = df[df['matches'] > m]
res = res[['pos', 'matches', 'reads_all', 'mismatches', 'deletions', 'insertions']]
res = pd.DataFrame(res)
res.to_csv('train_part.csv')

