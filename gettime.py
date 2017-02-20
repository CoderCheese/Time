from datetime import datetime
now = datetime.now()
print "Here is the time:"
print '%s ' % (now.minute) + "minutes have passed since " + '%s ' % (now.hour) + "o'Clock"
print "The date is " + '%s/%s/%s' % (now.month, now.day, now.year)
