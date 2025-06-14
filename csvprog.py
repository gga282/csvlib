import csv
from pathlib import Path
import re

def load_csv_to_dict(path):

    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader)
       
        data = {h: [] for h in headers}
        for row_num, row in enumerate(reader, start=1):
            
            if len(row) < len(headers):
                row += [''] * (len(headers) - len(row))
            
            elif len(row) > len(headers):
                row = row[:len(headers)]
            
            for h,cell in zip(headers, row):
                data[h].append(cell)
    return headers, data

def type_check(csvFile):
    digits=re.compile(r"\d")
    datereg=re.compile(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}")
    print(type(csvFile))
    for header,col_values in csvFile.items():
        for val in col_values:
            if digits.search(val):
                print(header)
                break



def main():
    base = Path(input("Enter the path to your CSV folder: ").strip())
    fname = input("Enter file name : ").strip()
    csv_path = base / fname

    if not csv_path.exists():
        print(f"File not found: {csv_path}")
        return

    headers, csv_dict = load_csv_to_dict(csv_path)
    n_rows = len(next(iter(csv_dict.values())))

    print(f"\nLoaded {fname!r} with {len(headers)} columns × {n_rows} rows\n")

    type_check(csv_dict)

    print(csv_dict)
if __name__ == "__main__":
    main()