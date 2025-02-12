import pandas as pd
import glob

files = glob.glob("*.csv")

github_count = 0

for file in files:
    try:
        print(f"Processing {file}...")
        df = pd.read_csv(file, encoding='utf-8', on_bad_lines='skip')

        count = df.apply(lambda row: row.astype(str).str.contains("GitHub", case=False, na=False).any(), axis=1).sum()
        github_count += count
    except Exception as e:
        print(f"Error processing {file}: {e}")

print(f"Total lines containing 'GitHub': {github_count}")

