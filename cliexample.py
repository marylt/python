import sys
import json

$ 

print(sys.argv)

with open(sys.argv[1], encoding = 'utf-8') as handle:
    contents = handle.read()

print(contents)

search_string = sys.argv[2]

result = re.findal(search_string, contents)

print(result)

''' for tweet in tweets:
    print(tweet) '''