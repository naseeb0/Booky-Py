import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def dictionary(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        user_decision = input((f"Did u mean {get_close_matches(word, data.keys())[0]} ?  "))
        if user_decision == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif user_decision == "N":
            return "No Words Found"
        else:
            return "We didnt understaand Your iNput"
        # 

word = input("Please Enter a Word \n")

output = dictionary(word)
if type(output) == list:
    for item in output:
        print(item + "\n")
else:
    print(output)