import json
import urllib
from bs4 import BeautifulSoup
import random
CANDIDATE_LIST = ["Hillary Clinton", "Bernie Sanders", "Donald Trump", "Ben Carson", "Ted Cruz", "Carly Fiorina", "Lindsey Graham", "Rand Paul", "Marco Rubio", "Mike Huckabee", "Rick Santorum"]
DEMOCRATS = ["Hillary Clinton", "Bernie Sanders"]
def getRandomQuotes(quotes, num):
    numquotes = len(quotes)
    chosen = []
    toreturn = []
    for i in range(num):
        r = random.randint(0, numquotes - 3)
        while r in chosen:
            r = random.randint(0, numquotes - 3)
        chosen.append(r)
        toreturn.append(quotes[r].decode('unicode-escape'))
    return toreturn
def gatherChildren(soup):
    returnstring = ""
    for child in soup.children:
        if "<ul>" in repr(child):
            print returnstring
            return returnstring
        else:
            returnstring += repr(child).decode('unicode-escape')
    return returnstring
def isCapitalLetter(letter):
    return ord(letter) <= 90 and ord(letter) >= 65 
def getCandidateQuotes(candidate, num):
    jsonurl = "http://en.wikiquote.org/w/api.php?format=json&action=parse&page=" + candidate + "&prop=text&section=1"
    response = urllib.urlopen(jsonurl)
    content = json.loads(response.read())
    soup = BeautifulSoup(json.dumps(content["parse"]['text']['*']), 'html.parser')
    #list_items = soup.find_all('li')[5]

    quotes = [string for string in soup.stripped_strings if (string[-2:] == "\\n" and string.rstrip("\\n") != "" and len(string) > 10 and isCapitalLetter(string[0]) )]
    random_quotes = getRandomQuotes(quotes, num)
    return random_quotes
    # return [gatherChildren(li) for li in list_items]
    #return gatherChildren(list_items)

def getRandomShit():
    toreturn = {}
    r = random.randint(0, len(CANDIDATE_LIST) - 1)
    random_candidate = CANDIDATE_LIST[r]
    random_quote = getCandidateQuotes(random_candidate, 1)[0]
    toreturn[random_candidate] = random_quote
    without = CANDIDATE_LIST[:r] + CANDIDATE_LIST[r+1:]
    wrong_answer = without[random.randint(0, len(without) - 1)]
    toreturn[wrong_answer] = ""
    return toreturn

def generateCandidateInfo():
    candidate_info = {}
    for candidate in CANDIDATE_LIST:
        query_name = candidate.replace(" ", "_")
        candidate_info[candidate] = {}
        candidate_info[candidate]["quotes"] = getCandidateQuotes(query_name, 3)
        candidate_info[candidate]["party"] = "democrat" if candidate in DEMOCRATS else "republican"
    return candidate_info