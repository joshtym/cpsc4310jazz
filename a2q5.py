import os
import nltk

def getAllFiles(folder):
   fileContentList = []
   listOfFiles = os.listdir(folder)

   for singleFile in listOfFiles:
      f = open(folder + singleFile,'r')
      fileContentList.append(f.read())
   f.close()
   return fileContentList

def cleanUpList(text):
   lemmatizer = nltk.WordNetLemmatizer()
   newText = []
   for word in nltk.word_tokenize(text):
      newText.append(lemmatizer.lemmatize(word.lower()))

spam = getAllFiles('testData/spam/')
nonspam = getAllFiles('testData/nonspam/')