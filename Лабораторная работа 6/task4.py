import json
import csv
INPUT_FILE = "input(1).csv"
with open(INPUT_FILE) as f:
    lines = [line for line in csv.DictReader(f)]
    for line in lines[:5]:
        print(json.dumps([line], indent=5), end = ",")










