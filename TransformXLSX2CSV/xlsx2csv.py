import pandas as pd

read_file = pd.read_excel (r'data.xlsx')
read_file.to_csv (r'data.csv', index = None, header=True)