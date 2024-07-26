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


schedule = getAllFiles('a3Data/schedule/')
nonschedule = getAllFiles('a3Data/nonschedule/')

tokenizedschedule = []
tokenizedNonschedule = []

for sp in schedule:
   tokenizedschedule.append(tokenizeAndClean(sp))
for ns in nonschedule:
   tokenizedNonschedule.append(tokenizeAndClean(ns))

setOfAllMails = []
for ts in tokenizedschedule:
   setOfAllMails.append((ts, 'schedule'))
for tns in tokenizedNonschedule:
   setOfAllMails.append((tns, 'nonschedule'))

random.shuffle(setOfAllMails)

featuresOfMails = []
for (email, designation) in setOfAllMails:
   featuresOfMails.append((features(email), designation))

trainAndEvaluate(featuresOfMails, 0.9)