import nltk

# metrics to tokenize and lemmatize all the lowercase words and return it as a list
def tokenizeAndClean(text):
   lemmatizer = nltk.WordNetLemmatizer()
   newText = []
   for word in nltk.word_tokenize(unicode(text, errors='ignore')):
      newText.append(lemmatizer.lemmatize(word.lower()))
   return newText

def jaccard_score(label1, label2):
    return (float(len(label1.intersection(label2))))/float(len(label1.union(label2)))

def mainFunc():
   fileOne = open('test.txt')
   fileTwo = open('test2.txt')
   tokenizedFiles = []
   firstSet = set(tokenizeAndClean(fileOne.read()))
   secondSet = set(tokenizeAndClean(fileTwo.read()))
   tokenizedFiles.append(firstSet)
   tokenizedFiles.append(secondSet)

   # Get Jaccard Score
   print("Jaccard Similarity is: " + str(jaccard_score(tokenizedFiles[0], tokenizedFiles[1])))

mainFunc()
