import pandas as pd

df = pd.read_csv('user.csv')
print(df[(df['username'] == 123) & (df['password'] == 123)].empty)
# if df[(df['username'] == 123) & (df['password'] == 123)].index != ([],):
#     print("True")
# else:
#     print("False")

# print(df.isin((123,123)).any())