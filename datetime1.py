import datetime
from datetime import timedelta
import pytz
from pytz import timezone




Portland = datetime.datetime.now()
#gets time as current hour
#this is considered a string, need to convert to integer 
Portland_time = Portland.strftime("%H")
#converts hourly time to an integer
Portland_open = int(Portland_time)

NYC = Portland.astimezone(timezone('America/New_York'))
NYC_time = NYC.strftime("%H")
NYC_open = int(NYC_time)

London = Portland.astimezone(timezone('Europe/London'))
London_time = London.strftime("%H")
London_open = int(London_time)

#checks times for different zones and returns if branch is open/closed
if Portland_open >= 9 and Portland_open <= 17:
    print("The Portland branch is currently open.")
else:
    print("The Portland branch is currently closed.")

if NYC_open >= 9 and NYC_open <= 17:
    print("The New York branch is currently open.")
else:
    print("The New York branch is currently closed.")

if London_open >= 9 and London_open <= 17:
    print("The London branch is currently open.")
else:
    print("The London branch is currently closed.")

    




