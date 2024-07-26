# Naive Bayes classifier to classify scheduling and no scheduling by taking a bunch of pre-provided
# sample data and test data. Following this, it extracts data about the found scheduling emails
# and outputs them to the console. Starts by getting all of the files, tokenizes and cleans them up by taking only
# relevant words and sets the training lists as schedule or non-schedule. It then gets the features of each list by
# assigning a dictionary to each word if it's not part of common words (IE, the stoplist). Then, the
# data is run through the classifier by first training it, then running the testData on it. We will pull the indicies
# of the testData that are classified as scheduling and run regexpr to extract the data we want
#
# Command to run is literally python a3q3.py, that's it
#
# Author : Joshua Tymburski

import os
import nltk
import nltk.corpus
import random

# All of the stopwords
stoplist = nltk.corpus.stopwords.words('english')

# Function that uses the OS and gets every file in the provided directory
def getAllFiles(folder):
   fileContentList = []
   listOfFiles = os.listdir(folder)

   for singleFile in listOfFiles:
      f = open(folder + singleFile,'r')
      fileContentList.append(f.read())
   f.close()
   return fileContentList

# Function to tokenize and lemmatize all the lowercase words and return it as a list
def tokenizeAndClean(text):
   lemmatizer = nltk.WordNetLemmatizer()
   newText = []
   for word in nltk.word_tokenize(unicode(text, errors='ignore')):
      newText.append(lemmatizer.lemmatize(word.lower()))
   return newText

# Function to get a dictionary of non-stoplist words (IE, the features)
def features(text):
   return {word: True for word in text if not word in stoplist}

# Function to train our classifier, then classify our test data.
# Returns a list of indicies that are the emails that are scheduling emails
def trainAndClassify(featuresOfMails, testFeaturesData):
   classifier = nltk.NaiveBayesClassifier.train(featuresOfMails)
   scheduleIndicies = []

   counter = 0
   for tfd in testFeaturesData:
      if classifier.classify(tfd) == 'schedule':
         scheduleIndicies.append(counter)
      counter += 1

   return scheduleIndicies

# Function to extract data. Finds the end and start times, the date and location. Because I
# generated the emails, I know how they look, hence why the regex looks the way it does.
# Prints the email being examined followed by the data of the event, location, and time
def extractData(emails):
   timeTokenizer = nltk.RegexpTokenizer('\d*\d:\d\d')
   dateTokenizer = nltk.RegexpTokenizer('Monday|Tuesday|Wednesday|Thursday|Friday|tomorrow|two days from now|January \d*\d|February \d*\d|March \d*\d|April \d*\d|May \d*\d|June \d*\d|July \d*\d|August \d*\d|September \d*\d|October \d*\d|November \d*\d|December \d*\d')
   locationTokenizer = nltk.RegexpTokenizer('be in.*on|be in.*tomorrow|be in.*two')
   finalLocationTokenizer = nltk.RegexpTokenizer('[A-z0-9]+')

   for i in emailsExamining:
      print("EMAIL BEING EXAMINED IS: ")
      print(i)
      print('\n')
      date = str(dateTokenizer.tokenize(i)[0])
      location = locationTokenizer.tokenize(i)[0]
      startTime = str(timeTokenizer.tokenize(i)[0])
      endTime = str(timeTokenizer.tokenize(i)[1])

      # Semantics to get rid of the first 'be' word and the last word
      # which is not part of the location
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
         

# Training schedule, non schedule, and testData folders
schedule = getAllFiles('a3Data/schedule/')
nonschedule = getAllFiles('a3Data/nonschedule/')
testData = getAllFiles('a3Data/testData/')

# Tokenize all three sets
tokenizedschedule = []
tokenizedNonschedule = []
tokenizedTestData = []

for sp in schedule:
   tokenizedschedule.append(tokenizeAndClean(sp))
for ns in nonschedule:
   tokenizedNonschedule.append(tokenizeAndClean(ns))
for td in testData:
   tokenizedTestData.append(tokenizeAndClean(td))

# Create a key / index model for scheduling and
# nonscheduling
setOfAllMails = []
for ts in tokenizedschedule:
   setOfAllMails.append((ts, 'schedule'))
for tns in tokenizedNonschedule:
   setOfAllMails.append((tns, 'nonschedule'))

# Get the features of the setOfAllMails (our training data)
# and the testData. Shuffle the training set
featuresOfMails = []
featuresOfTestData = []
for (email, designation) in setOfAllMails:
   featuresOfMails.append((features(email), designation))

for ttd in tokenizedTestData:
   featuresOfTestData.append(features(ttd))

random.shuffle(featuresOfMails)

# Get our indicies of the testData which are scheduling emails
# and create our index of emails to feed into our extraction function
scheduleIndicies = trainAndClassify(featuresOfMails, featuresOfTestData)
emailsExamining = []
for i in scheduleIndicies:
   emailsExamining.append(testData[i])

# Get the data we want, output to console
extractData(emailsExamining)