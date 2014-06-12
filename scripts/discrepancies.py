#!/usr/bin/env python3

import sys
import csv

_, f2 = sys.argv

valid_ids = set()
with open("identifiers/country-us.csv", 'r') as fd1:
    fs1 = csv.DictReader(fd1)
    for row in fs1:
        id_ = row['id']
        valid_ids.add(id_)

with open(f2, 'r') as fd2:
    fs2 = csv.DictReader(fd2)
    for row in fs2:
        if row['id'] not in valid_ids:
            print("Error: %s is invalid" % (row['id']))
