import pandas as pd
import os
import glob


source="/Users/alexander/Code/Python/01_filemanip/XLSX/XLSX2CSV"
dest='/Users/alexander/Code/Python/01_filemanip/XLSX/XLSX2CSV/conv/'
os.chdir(source)


for file in glob.glob("*.xlsx"):
       df = pd.read_excel(file)
       df.to_csv(dest+file+'.csv', index=False)

for file in glob.glob("*.xls"):
       df = pd.read_excel(file)
       df.to_csv(dest+file+'.csv', index=False)