import sys
import os
import random

def myFunction():
   print ("Starting Gen:")
   weekDates = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
   otherDateColloquials = ["tomorrow", "two days from now"]
   months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
   daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
   locations = ["my office", "room 892", "room D634", "CEO's office", "Dan's office", "room B567", "the Dean's office", "Calgary", "head office"]
   event = ["ice cream", "scheduling", "financing", "computer learning", "programming", "curriculum", "python tutorial", "Linux tutorial", "How To Program Productively"]
   minuteTimes = ["00","15","30","45"]

   firstPart = "Subject: Meeting\nHello,\nWe have scheduled the "
   secondPart = " meeting. It will be in "

   for i in range(100):
      f = open("scheduleEmails/email" + str(i) + ".txt", 'w')
      dateSelector = random.randint(1,3)
      fullString = firstPart + random.choice(event) + secondPart + random.choice(locations)

      if dateSelector == 1:
         fullString = fullString + " on " + random.choice(weekDates)
      if dateSelector == 2:
         fullString = fullString + random.choice(otherDateColloquials)
      if dateSelector == 3:
         month = random.choice(months)
         monthIndex = int(months.index(month) + 1)
         fullString = fullString + " on " + random.choice(months) + " " + str(random.randint(1,monthIndex))

      fullString = fullString + " from " + str(random.randint(1,12)) + ":" + random.choice(minuteTimes) + " to " + str(random.randint(1,12)) + ":" + random.choice(minuteTimes)
      f.write(fullString)

myFunction()