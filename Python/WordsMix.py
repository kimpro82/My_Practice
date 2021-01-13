# 0. Check If Words.csv Exists

import os

path = "C:\\Users\\……\\Python\\Words.csv"
# \\ : escape character of \
os.path.isfile(path)


# 1. Read Words.csv simply 

import csv

with open(path,'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)

    for c in reader:
        for k, v in c.items():
            print(v, end= ' ')
        print("\n")


# 1-1. Read Words.csv as dictionary type

with open(path,'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(row)


# 1-2. Get rid of '\ufeff' from the head of data

with open(path,'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(row)
