# usage: python tweet_sentiment.py AFINN-111.txt three_minutes_tweets.json

import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def cleaning():
    afinnfile = open("AFINN-111.txt")
    scores = {}
    for line in afinnfile:
            term, score = line.split("\t")
            scores[term] = int(score)
    #print scores.keys()
    #cleaning the json file
    jsonfile = open("three_minutes_tweets.json")
    for line in jsonfile:
        dict = json.loads(jsonfile.next())
        if dict.has_key("text"):
            #process the text
            text = dict["text"].split()
            count = 0
            for words in text:
                words = words.encode('utf-8').lower()
                if scores.has_key(words):
                    count += scores[words]
            print count
        else:
            #output 0
            print (0)

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    lines(sent_file)
    lines(tweet_file)
    cleaning()

if __name__ == '__main__':
    main()
