import os
import nltk
import nltk.corpus
import random

stoplist = nltk.corpus.stopwords.words('english')

def getAllFiles(folder):
   fileContentList = []
   listOfFiles = os.listdir(folder)

   for singleFile in listOfFiles:
      f = open(folder + singleFile,'r')
      fileContentList.append(f.read())
   f.close()
   return fileContentList

def tokenizeAndClean(text):
   lemmatizer = nltk.WordNetLemmatizer()
   newText = []
   for word in nltk.word_tokenize(unicode(text, errors='ignore')):
      newText.append(lemmatizer.lemmatize(word.lower()))
   return newText

def features(text):
   return {word: True for word in text if not word in stoplist}

def trainAndEvaluate(featuresOfMails, propToTrain):
   sizeOfTraining = int(len(featuresOfMails) * propToTrain)
   trainingData = featuresOfMails[:sizeOfTraining]
   testData = featuresOfMails[sizeOfTraining:]
   classifier = nltk.NaiveBayesClassifier.train(trainingData)
   print('The accuracy of the training data was ' + str(nltk.classify.accuracy(classifier, trainingData)))
   print('The accuracy of the test data was ' + str(nltk.classify.accuracy(classifier, testData)))
   classifier.show_most_informative_features(5)


spam = getAllFiles('testData/spam/')
nonspam = getAllFiles('testData/nonspam/')

tokenizedSpam = []
tokenizedNonSpam = []

for sp in spam:
   tokenizedSpam.append(tokenizeAndClean(sp))
for ns in nonspam:
   tokenizedNonSpam.append(tokenizeAndClean(ns))

setOfAllMails = []
for ts in tokenizedSpam:
   setOfAllMails.append((ts, 'spam'))
for tns in tokenizedNonSpam:
   setOfAllMails.append((tns, 'nonspam'))

random.shuffle(setOfAllMails)

featuresOfMails = []
for (email, designation) in setOfAllMails:
   featuresOfMails.append((features(email), designation))

trainAndEvaluate(featuresOfMails, 0.9)