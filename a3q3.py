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

def trainAndClassify(featuresOfMails, propToTrain):
   sizeOfTraining = int(len(featuresOfMails) * propToTrain)
   trainingData = featuresOfMails[:sizeOfTraining]
   testData = featuresOfMails[sizeOfTraining:]
   classifier = nltk.NaiveBayesClassifier.train(featuresOfMails)

   index = sizeOfTraining
   scheduleIndicies = []
   for email in testData:
      if classifier.classify(email[0]) == 'schedule':
         scheduleIndicies.append(index)
      index += 1

   return scheduleIndicies
         

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


featuresOfMails = []
for (email, designation) in setOfAllMails:
   featuresOfMails.append((features(email), designation))

tempFeaturesOfMails = []
for fom in featuresOfMails:
   tempFeaturesOfMails.append(fom)
random.shuffle(tempFeaturesOfMails)

scheduleIndicies = trainAndClassify(tempFeaturesOfMails, 0.9)
indexInUnShuffled = []

emailsExamining = []
for i in scheduleIndicies:
   emailsExamining.append(schedule[featuresOfMails.index(tempFeaturesOfMails[i])])

timeTokenizer = nltk.RegexpTokenizer('\d*\d:\d\d')
dateTokenizer = nltk.RegexpTokenizer('Monday|Tuesday|Wednesday|Thursday|Friday|tomorrow|two days from now|January \d*\d|February \d*\d|March \d*\d|April \d*\d|May \d*\d|June \d*\d|July \d*\d|August \d*\d|September \d*\d|October \d*\d|November \d*\d|December \d*\d')
locationTokenizer = nltk.RegexpTokenizer('be in.*on|be in.*tomorrow|be in.*two')
finalLocationTokenizer = nltk.RegexpTokenizer('[A-z0-9]+')

for i in emailsExamining:
   print(i)
   print('\n')
   date = str(dateTokenizer.tokenize(i)[0])
   location = locationTokenizer.tokenize(i)[0]
   startTime = str(timeTokenizer.tokenize(i)[0])
   endTime = str(timeTokenizer.tokenize(i)[1])
   trimmedLocationList = finalLocationTokenizer.tokenize(location)
   length = len(trimmedLocationList)
   trimmedLocation = ""

   for i in range(length):
      if i != 0 and i != length - 1:
         trimmedLocation += str(trimmedLocationList[i])
         if trimmedLocationList[i+1] == 's':
            trimmedLocation += '\''
         else:
            trimmedLocation += ' '

   print('Date: ' + date)
   print('Location: ' + trimmedLocation)
   print('Time: ' + startTime + ' to ' + endTime)
   print('\n')