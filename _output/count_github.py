import os
import pandas as pd

DATA_DIR = "/home/ubuntu/ad-688-classroom-sp25-lab-01-Assignment-01"
csv_files = ["questions.csv", "question_tags.csv"]

count = 0
chunk_size = 50000


def contains_github(chunk):
    text_columns = chunk.select_dtypes(include=["object"])
    return text_columns.apply(lambda col: col.str.contains("GitHub", case=False, na=False)).any(axis=1).sum()

for file in csv_files:
    file_path = os.path.join(DATA_DIR, file)
    try:
        for chunk in pd.read_csv(file_path, encoding='utf-8', on_bad_lines='skip', chunksize=chunk_size, low_memory=True):
            count += contains_github(chunk)
    except Exception as e:
        print(f"Error reading {file}: {e}")

print(f"Total lines containing 'GitHub': {count}")
