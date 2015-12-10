import json
import urllib
from bs4 import BeautifulSoup
import random, twitter, string
DRUNK_PHRASES = [
    "I'm drunk",
    "I'm wasted",
    "I'm smashed",
    "I'm inebriated",
    "I'm intoxicated"
]
CANDIDATE_LIST = ["Hillary Clinton", "Bernie Sanders", "Donald Trump", "Ben Carson", "Ted Cruz", "Carly Fiorina", "Lindsey Graham", "Rand Paul", "Marco Rubio", "Mike Huckabee"]
DEMOCRATS = ["Hillary Clinton", "Bernie Sanders"]
CANDIDATE_PHRASES = {
    "Hillary Clinton" : ("best", "worst"),
    "Bernie Sanders" : ("Upper-Class", "worst"),
    "Donald Trump" : ("Best", "Worst"),
    "Ben Carson" : ("Washington", "politician"),
    "Ted Cruz" : ("Obamacare", "Constitution"),
    "Carly Fiorina" : ("Hillary", "Congress"),
    "Lindsey Graham" : ("Values", "Liberty"),
    "Rand Paul" : ("Liberty", "Tax"),
    "Marco Rubio" : ("Future", "Iran"),
    "Mike Huckabee" : ("Clinton", "Faith")
}
def getRandomDrunkPhrase():
    r = random.randint(0, len(DRUNK_PHRASES) - 1)
    return DRUNK_PHRASES[r]

def getCandidateParty(candidate):
    return "democrat" if candidate in DEMOCRATS else "republican"

def getCandidatePhrases(candidate):
    return CANDIDATE_PHRASES[candidate]

def getRandomCandidate():
    r = random.randint(0, len(CANDIDATE_LIST) - 1)
    return CANDIDATE_LIST[r]

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
    random_candidate = getRandomCandidate()
    r = CANDIDATE_LIST.index(random_candidate)
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
        candidate_info[candidate]["party"] = getCandidateParty(candidate)
    return candidate_info

def twitterInfo(query):
    api = twitter.Api(consumer_key='2DIC2A8HVULFML31XvpTY0Egr',
                  consumer_secret='GHu0ZOwyDQq6G6YJ4OgzB0k4B8iUyRzdMnlmeCOJmRsVNWyq4Z',
                  access_token_key='2674508256-gwiIyCrx10t1V4ztSelCfFosgetyrDC5jXoSbfJ',
                  access_token_secret='Y6F9Nq8iJkc5BPZkqakoGsZeKmc1Ho2krmRdhKL4ziP4Y')

    statuses = api.GetSearch(term=query, result_type='popular', count=10000)
    status_text = [s.text for s in statuses]
    word_counts = {}

    ignored_words = ['a', 'to', 'the', 'has', 'should', 'on', 'is']
    for status in status_text:
        split_status = status.split()
        split_status = [s.encode('ascii', errors='ignore') for s in split_status]
        split_status = [s.translate(None, string.punctuation) for s in split_status]
        for word in split_status:
            if word in ignored_words:
                break
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
    cloud = []
    for key, value in word_counts.iteritems():
        cloud.append([key, value])
    return cloud

def generateClouds():
    clouds = {}
    for candidate in CANDIDATE_LIST:
        candidate_str = candidate.replace(" ", "")
        clouds[candidate_str] = twitterInfo(candidate)
    return clouds
