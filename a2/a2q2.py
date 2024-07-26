# Program created as part of assignment 2 in CPSC 4310. Correct syntax for python is
# python a2q2.py corpus.txt sentenceLength numberOfSentences. So, for example, you would type
# python a2q2.py mytext.txt 4 2 and this would create 2 sentences of length 4 words from the given
# corpus. 
#
# This program was created using the unigram model. IE, we get the probability of a word appearing by
# determining it's frequency and choose words based on probability of that word. So, program
# takes in the file, tokenizes all words in lower case and generates a sentence from it. In particular
# we can use the random function from python since the tokenized list contains every word and if we
# randomly select a word, there exists a unigram probabalistic chance we get a specific word. So, 
# if our text had 40 words with 10 appearances of 'the', then the random function would have a 1/4 chance
# of selecting the word which is exactly the unigram model.
#
# A sample corpus.txt has been provided
#
# Author: Joshua Tymburski
import nltk
import sys
import random
import string

def mainFunc():
   # Ensure proper arguments
   if len(sys.argv) < 4:
      print("Insufficient arguments. Correct syntax is python a2q2.py yourText.txt lengthOfSentences numOfSentences")
      return

   # Open file and tokenize all words, then convert them to lowercase
   fileContent = open(sys.argv[1]).read()
   tokens = nltk.word_tokenize(fileContent)
   lowerCaseTokens = []
   for token in tokens:
      if token not in string.punctuation:
         lowerCaseTokens.append(token.lower())

   # Create exactly numOfSentences number of sentences
   count = 0
   for count in range(0,int(sys.argv[3])):
      sentence = []
      count += 1

      # Create the sentence using the random function
      while(True):
         if len(sentence) == int(sys.argv[2]):
            break
         sentence.append(random.choice(lowerCaseTokens))

      # Just some semantics to get it to a printable format
      count2 = 0
      strSentence = ""
      for count2 in range(0,int(sys.argv[2])):
         strSentence = strSentence + sentence[count2]
         if count2 != int(sys.argv[2]) - 1:
            strSentence = strSentence + " "
         count2 += 1

      # Print sentence
      print("Sentence " + str(count) + " is : " + strSentence)

mainFunc()