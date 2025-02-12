import pandas as pd
import glob

files = glob.glob("*.csv")
count = 0

for file in files:
    df = pd.read_csv(file, encoding='utf-8', on_bad_lines='skip')
    count += df.apply(lambda row: row.astype(str).str.contains("GitHub", case=False, na=False).any(), axis=1).sum()

print(f"Total lines containing 'GitHub': {count}")
