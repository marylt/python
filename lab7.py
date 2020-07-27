
# libraries to be imported
import re

# loading holmes text file
with open('holmes.txt') as book:
    text = book.read()

#####################

# question 1, answer is 461 for specifically 'Holmes'

pattern1 = r'Holmes'
count = len(re.findall(r'\b' + 'Holmes' + r'\b', text))
print(count)

# question 2, possible answer is 'Briony' from 'Briony Lodge'

lodgesearch = re.search('(\S+?) Lodge', text)
print(lodgesearch)

# question 3, answers are 'moustached--evidently' and 'disproportionately'
    # 'disproportionately' seems to be more of a 'real word' so that is the answer

words = [w for w in text.split() if "ly" in w]
for w in words:
    if len(w) > 15 and '--' not in w:
        print(w)

# question 4, answer is 37,462

l = (re.findall("[\d]+", text))
final = []
print(sum(map(int, l)))

#####################
# End of script for Module 7 Lab
