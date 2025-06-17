
from pathlib import Path

def load_csv_to_dict(path, filename):
    file_path = Path(path) / filename

    if not file_path.exists():
        print(f"File not found: {file_path}")
        return {}, []

    with open(file_path, "r") as f:
        lines = f.readlines()

    headers = lines[0].strip().split(",")
    rows = lines[1:]

    data = {header: [] for header in headers}

    for line in rows:
        cells = line.strip().split(",")
        if len(cells) < len(headers):
            cells += [""] * (len(headers) - len(cells))
        elif len(cells) > len(headers):
            cells = cells[:len(headers)]

        for idx, header in enumerate(headers):
            data[header].append(cells[idx])

    return data, headers

def print_csv_summary(data, headers):
    print(f"CSV Loaded with {len(headers)} columns and {len(data[headers[0]])} rows\n")
    for header in headers:
        print(f"{header}: {data[header][:5]}{'...' if len(data[header]) > 5 else ''}")

    print(data)

def main():
    path = input("Enter the path to your CSV folder: ").strip()
    filename = input("Enter file name (e.g., data.csv): ").strip()

    data, headers = load_csv_to_dict(path, filename)

    if data:
        print_csv_summary(data, headers)

if __name__ == "__main__":
    main()
