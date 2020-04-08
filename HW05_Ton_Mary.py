'''
Name: Mary Ton
StudentDirectory ID: mton
Date: 2019-10-11
Assignment: Homework 2
'''
import csv
with open('energy.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
