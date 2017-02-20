from datetime import datetime
now = datetime.now()
#This will show the time in a 24-hour format
print "Here is the time(The time is shown in 24-hour format:"
print '%s ' % (now.minute) + "minutes have passed since " + '%s ' % (now.hour) + "o'Clock"
print "The date is " + '%s/%s/%s' % (now.month, now.day, now.year)
