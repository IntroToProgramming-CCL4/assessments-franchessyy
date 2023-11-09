#this will print your date and time now
import datetime
now = datetime.datetime.now()
print ("Current date and time :")
print (now.strftime("%Y-%m-%d %H: %M:%S"))