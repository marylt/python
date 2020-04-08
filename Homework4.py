'''
Name: Mary Ton
StudentDirectory ID: mton
Date: 2019-10-28
Assignment: Homework 4 Relational Databases
'''

# libraries to be imported
import sqlite3
import csv

# opening csv file and creating reader with encoding + delimiter
data = open('books.csv', 'r', encoding = 'utf-8')
reader = csv.reader(data, delimiter=',')

# defining connection memory and cursor
conn = sqlite3.connect(':memory:')
curs = conn.cursor()

# creating the books table and commiting 
curs.execute('''CREATE TABLE books ('id' INTEGER, 'title' TEXT, 'author' TEXT, 'year' DATE);''')

conn.commit()

# going through the csv file to add data into the books table
for r in reader:
    curs.execute(''' INSERT INTO books VALUES (?,?,?,?)''', r)

# closing the csv file and commiting the data into the books table
data.close()
conn.commit()

# selecting all from the table books
sq = ''' SELECT author, title, year FROM books '''
book = curs.execute(sq).fetchall()

# ignoring the encoding errors in order to print everything from the books table
for x in book:
    try:
        print(x)
    except UnicodeEncodeError:
        pass

# End of code for Homework 4 Relational Databases