import pandas as pd
import numpy as np

# IMPORTANT: please do not modify this import statement
# from placeholders import put_your_answer_here


# The data frame `df` includes the following information
#
# |            | AUD/USD | EUR/AUD |
# |------------+---------+---------|
# | 2020-09-08 | 0.7280  | 1.6232  |
# | 2020-09-09 | 0.7209  | 1.6321  |
# | 2020-09-10 | NaN     | 1.6221  |
# | 2020-09-11 | 0.7263  | 1.6282  |
# | 2020-09-14 | 0.7281  | NaN     |
# | 2020-09-15 | 0.7285  | 1.6288  |
data = {
    'AUD/USD': [ 0.7280, 0.7209, np.nan, 0.7263, 0.7281, 0.7285,],
    'EUR/AUD': [ 1.6232, 1.6321, 1.6221, 1.6282, np.nan, 1.6288,],
    }
index = [ '2020-09-08', '2020-09-09', '2020-09-10', '2020-09-11', '2020-09-14', '2020-09-15',]
df = pd.DataFrame(data, index)

# Q1.1
sel_q1 = ['2020-09-08','2020-09-14']
q1 = df.loc[sel_q1]
print(q1)

# Q1.2
(start_q2, stop_q2) = (0, 2)
q2 = df.iloc[start_q2:stop_q2]
print(q2)

# Q1.3
(start_q3, stop_q3) = (0, 2)
q3 = df[start_q3:stop_q3]
print(q3)

# Q1.4
row_sel_q4 = ['2020-09-08','2020-09-09']
col_sel_q4 = ['AUD/USD']
q4 = df.loc[row_sel_q4, col_sel_q4]
print(q4)


# Q2.1
print(df.loc['a':'z'])

# Q2.2
print(df.loc['0':'z'])

# Q2.3 (key error)
# new_df = df.copy()
# new_df.loc['1', :] = 1
# print(new_df.loc['1', 'z'])

# Q2.4
print(df.iloc[100:1000])

# Q2.5
print(df.loc[:, 'AUD/USD'])

# Q2.6 (key error)
# print(df.loc['AUD/USD'])