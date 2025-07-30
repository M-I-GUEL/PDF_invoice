import pandas as pd
import glob 

filepaths = glob.glob('invoice/*.xlsx')
for filepath in filepaths:
    df = pd.read_excel(filepath)