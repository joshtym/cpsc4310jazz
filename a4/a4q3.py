import nltk
import math

# metrics to tokenize and lemmatize all the lowercase words and return it as a list
def tokenizeAndClean(text):
   lemmatizer = nltk.WordNetLemmatizer()
   newText = []
   for word in nltk.word_tokenize(unicode(text, errors='ignore')):
      newText.append(lemmatizer.lemmatize(word.lower()))
   return newText

def jaccard_score(label1, label2):
    return (float(len(label1.intersection(label2))))/float(len(label1.union(label2)))

def getCountVector(terms, tokenizedList):
   countValues = []
   for term in terms:
      count = 0
      for token in tokenizedList:
         if token == term:
            count += 1
      countValues.append(count)
   return countValues

def getDict(terms,countVector):
   count = 0
   dictionary = {}
   for word in terms:
      dictionary[word] = countVector[count]
      count += 1
   return dictionary

def getLogWeightFreq(vec):
   for i in range(0,len(vec)):
      if vec[i] != 0:
         vec[i] = ((math.log(vec[i]))/(math.log(10))) + 1
   return vec

def normalizeVec(vec):
   num = 0.0
   for i in vec:
      num += i*i
   num = math.sqrt(num)

   for i in range(0,len(vec)):
      vec[i] = vec[i] / num

   return vec

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
   fileOne = open('test.txt')
   fileTwo = open('test2.txt')
   tokenizedListOne = tokenizeAndClean(fileOne.read())
   tokenizedListTwo = tokenizeAndClean(fileTwo.read())
   firstSet = set(tokenizedListOne)
   secondSet = set(tokenizedListTwo)

   #dictOne = getDict(allTerms,countOne)
   #dictTwo = getDict(allTerms,countTwo)

   # Get Jaccard Score
   print("Jaccard Similarity is: " + str(jaccard_score(firstSet, secondSet)))

   # Get Cosine Similarity
   print("Cosine Similarity is: " + str(getCosineSim(tokenizedListOne, tokenizedListTwo, firstSet.union(secondSet))))

mainFunc()
