import csv
import re
#encoding: utf-8

##converts .txt to .csv
import csv

with open('lex.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('lexique.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('lemma number','entry', 'Pos', 'definition'))
        writer.writerows(lines)