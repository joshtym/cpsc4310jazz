import nltk
import sys
import random
import string

def mainFunc():
   if len(sys.argv) < 4:
      print("Insufficient arguments. Correct syntax is python thisProg.py yourText.txt lengthOfSentences numOfSentences")
      return

   fileContent = open(sys.argv[1]).read()
   tokens = nltk.word_tokenize(fileContent)
   lowerCaseTokens = []

   for token in tokens:
      if token not in string.punctuation:
         lowerCaseTokens.append(token.lower())

   count = 0
   for count in range(0,int(sys.argv[3])):
      sentence = []
      count += 1

      while(True):
         if len(sentence) == int(sys.argv[2]):
            break
         sentence.append(random.choice(lowerCaseTokens))

      count2 = 0
      strSentence = ""
      for count2 in range(0,int(sys.argv[2])):
         strSentence = strSentence + sentence[count2]
         if count2 != int(sys.argv[2]) - 1:
            strSentence = strSentence + " "
         count2 += 1

      print("Sentence " + str(count) + " is : " + strSentence)

mainFunc()