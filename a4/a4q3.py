# Program that gets the jaccard score, tf-idf weight, and cosine similarity between two documents.
# To run this program, please use python a4q3.py
#
# Author: Joshua Tymburski
import nltk
import math

# metrics to tokenize and lemmatize all the lowercase words and return it as a list
def tokenizeAndClean(text):
   lemmatizer = nltk.WordNetLemmatizer()
   newText = []
   for word in nltk.word_tokenize(unicode(text, errors='ignore')):
      newText.append(lemmatizer.lemmatize(word.lower()))
   return newText

# Function that returns the Jaccard Coefficient
def jaccard_score(label1, label2):
    return (float(len(label1.intersection(label2))))/float(len(label1.union(label2)))

# Returns a vector of terms and how many times each term appears
def getCountVector(terms, tokenizedList):
   countValues = []
   for term in terms:
      count = 0
      for token in tokenizedList:
         if token == term:
            count += 1
      countValues.append(count)
   return countValues

# Calculate the tdf-idf weighting
def getLogWeightFreq(vec):
   for i in range(0,len(vec)):
      if vec[i] != 0:
         vec[i] = ((math.log(vec[i]))/(math.log(2))) + 1
   return vec

# Normalize vector (used by cosine)
def normalizeVec(vec):
   num = 0.0
   for i in vec:
      num += i*i
   num = math.sqrt(num)

   for i in range(0,len(vec)):
      vec[i] = vec[i] / num

   return vec

# Do the log weighting to get the TF score for each document
def getTFScore(listOne, listTwo, firstSet, secondSet):
   countOne = getCountVector(firstSet.difference(secondSet), listOne)
   countTwo = getCountVector(secondSet.difference(firstSet), listTwo)

   countOne = getLogWeightFreq(countOne)
   countTwo = getLogWeightFreq(countTwo)

   scores = [0,0]

   for i in range(0,len(countOne)):
      scores[0] += countOne[i]
      scores[1] += countTwo[i]

   return scores

# Do the cosine similarity calculations (normalize and add)
def getCosineSim(listOne, listTwo, allTerms):
   countOne = getCountVector(allTerms, listOne)
   countTwo = getCountVector(allTerms, listTwo)

   countOne = getLogWeightFreq(countOne)
   countTwo = getLogWeightFreq(countTwo)

   countOne = normalizeVec(countOne)
   countTwo = normalizeVec(countTwo)

   cosineVal = 0.0
   for i in range(0,len(countOne)):
      cosineVal += (countOne[i] * countTwo[i])
   return cosineVal

def mainFunc():
   # Open the files and tokenize each
   fileOne = open('test.txt')
   fileTwo = open('test2.txt')
   tokenizedListOne = tokenizeAndClean(fileOne.read())
   tokenizedListTwo = tokenizeAndClean(fileTwo.read())
   firstSet = set(tokenizedListOne)
   secondSet = set(tokenizedListTwo)

   # Get Jaccard Score
   print("Jaccard Similarity is: " + str(jaccard_score(firstSet, secondSet)))

   scores = getTFScore(tokenizedListOne, tokenizedListTwo, firstSet, secondSet)
   # Get TF-IDF scores
   print("The TF-IDF scores for the two documents are: " + str(scores[0]) + " and " + str(scores[1]))
   
   # Get Cosine Similarity[]
   print("Cosine Similarity is: " + str(getCosineSim(tokenizedListOne, tokenizedListTwo, firstSet.union(secondSet))))

mainFunc()
