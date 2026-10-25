import datetime
import time 

def birthday_time():
    birthdays={
        "Humayun": "2026-10-20"    
        }
    today=datetime.date.today().strftime("%y-%m-%d")
    
    for bday in birthdays:
        if bday==today:
            print("Happy birthday TO Humayun")
        else:
            print("Not Humayun's birthday today")
while True:
    birthday_time()
    time.sleep(24*60*60)
    