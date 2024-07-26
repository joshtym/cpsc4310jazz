# Naive Bayes classifier to classify spam and no spam by taking in a mass amount of sample spam and
# non spam data. Starts by getting all of the files, tokenizes and cleans them up by taking only
# relevant words and sets these lists as spam or non spam. It then gets the features of each list by
# assigning a dictionary to each word if it's not part of common words (IE, the stoplist). Then, the
# data is run through the classifier and the outputs are printed for accuracy. The spam and nonspam data
# is provided for testing purposes.
#
# Command to run is literally python a2q5.py, that's it
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

# Function that does the interesting portion. Trains from the features
# and evaluates with classifier. propToTrain is the proportion of the
# provided list we are using as the training. Prints out accuracy and
# most informative features
def trainAndEvaluate(featuresOfMails, propToTrain):
   sizeOfTraining = int(len(featuresOfMails) * propToTrain)
   trainingData = featuresOfMails[:sizeOfTraining]
   testData = featuresOfMails[sizeOfTraining:]
   classifier = nltk.NaiveBayesClassifier.train(trainingData)
   print('The accuracy of the training data was ' + str(nltk.classify.accuracy(classifier, trainingData)))
   print('The accuracy of the test data was ' + str(nltk.classify.accuracy(classifier, testData)))
   classifier.show_most_informative_features(5)

# Our spam and nonspam folders
spam = getAllFiles('testData/spam/')
nonspam = getAllFiles('testData/nonspam/')

# Tokenize the spam and nonspam
tokenizedSpam = []
tokenizedNonSpam = []
for sp in spam:
   tokenizedSpam.append(tokenizeAndClean(sp))
for ns in nonspam:
   tokenizedNonSpam.append(tokenizeAndClean(ns))

# Create a key / index model for spam and
# nonspam
setOfAllMails = []
for ts in tokenizedSpam:
   setOfAllMails.append((ts, 'spam'))
for tns in tokenizedNonSpam:
   setOfAllMails.append((tns, 'nonspam'))

# Shuffle all the mails to get different results
random.shuffle(setOfAllMails)

# Get the features and create a key / index of features
# and its designation (IE, spam or nonspam)
featuresOfMails = []
for (email, designation) in setOfAllMails:
   featuresOfMails.append((features(email), designation))

# train and evaluate our training on test data
trainAndEvaluate(featuresOfMails, 0.9)