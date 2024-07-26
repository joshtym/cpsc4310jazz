import nltk
import nltk.metrics.distance

def tokenizeAndClean(text):
   lemmatizer = nltk.WordNetLemmatizer()
   newText = []
   for word in nltk.word_tokenize(unicode(text, errors='ignore')):
      newText.append(lemmatizer.lemmatize(word.lower()))
   return newText

def mainFunc():
   fileOne = open('test.txt')
   fileTwo = open('test2.txt')
   tokenizedFiles[2] = [tokenizeAndClean(fileOne), tokenizeAndClean(fileTwo)]

mainFunc()
