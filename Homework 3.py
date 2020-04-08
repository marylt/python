'''
Name: Mary Ton
StudentDirectory ID: mton
Date: 2019-10-21
Assignment: Homework 3
'''

# libraries to be imported:
import sys
import re
import json

# main function
def main():
    if len(sys.argv) < 2:
        print("There are not enough arguments. Please have at least two.")
    else:
        dataset = Dataset(sys.argv[1])
        while True:
            search_string = input("Enter a term to search, or enter 'q' to quit: ")
            if search_string == 'q':
                break
            else:
                for items in dataset.contents:
                    search_result = re.search(search_string, items.text)
                    if search_result:
                        print("Text: ", items.text, "Date: ", items.created)


#############

# first class:
# this class will serve for the sys.argv function:
class Dataset():
    def __init__(self, filepath):
        with open('aoc.json', encoding = 'utf-8') as file:
            data = json.load(file)
            self.contents = []
            for items in data:
                self.contents.append(Tweet(items))

#############

# second class:
# This class will serve as the search-through for modelling the data in memory:
class Tweet():
    def __init__(self, tweet):
        self.text = tweet['text']
        self.created = tweet['created']

#############

# calling the main function:
if __name__ == '__main__':
    main()
    
# end of code for Homework 3!
