# Program that takes in a corpus as dictacted by the user and tokenizes it, counts the tokens
# and counts the word types. Prints out the max word appearance
#
# Author : Joshua Tymburski
import nltk
import sys

def runProg():
    if len(sys.argv) == 1:
        print("Incorrect syntax. Proper syntax is python a1.py textFile1.txt testFile2.txt etc.")

    firstVar = True;

    for arg in sys.argv:
        if firstVar:
            firstVar = False
        else:
            fileContent = open(arg).read()
            wordTokens = nltk.word_tokenize(fileContent)
            wordTypes = set(wordTokens)
            print("There are " + str(len(wordTokens)) + " word tokens in " + sys.argv[1])
            print("There are " + str(len(wordTypes)) + " word types in " + sys.argv[1])

            maxCount = 0
            maxWord = ""

            for word in wordTypes:
                wordCount = fileContent.count(word)
                if wordCount > maxCount:
                    maxCount = wordCount
                    maxWord = word

            print("Word of '" + maxWord + "' has the most appearances at " + str(maxCount))

runProg()