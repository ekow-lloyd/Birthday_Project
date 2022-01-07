import pprint  # if necessary, this module prints out a more "decent" output
import json  # a module to store the dictionary as a database that can be read or written to
from datetime import datetime, timedelta  # importing the datetime module in order to determine the day/time
import pyinputplus as pyip  # this helps control user input type
import smtplib. # this module allows us to log in and send emails from our mail box

''' database = {'Shrek':'Apr 24', 'Fiona':'Apr 25','Donkey':'Apr 26', 'Ginger':'Apr 27'}  # create an initial dictionary, it could also be empty(this is only necessary once)

with open('bDay_db.json', 'w')as outfile:
    json.dump(database, outfile)
 '''
this_day = (datetime.today().strftime('%b %d'))  # this block changes today's date format to MMM DD like i have in my dictionary
year = (datetime.today().strftime('%Y'))
day = (datetime.today().strftime('%A'))
print()
print("Today's date is : "+ day + ' ' + this_day + ' ' + year)
print()

with open("bDay_db.json", "r") as read_file:  # this section opens the Database in read-mode in order to query it
    dob = json.load(read_file)


def tOdAy():
    """ this function gets today's date"""
    with open('bDay_db.json')as read_file:  # opens databse in read mode
        bdays = json.load(read_file)

    if this_day in bdays.values():  # if today's date matches a day of the bdays...
        print("Birthday match found 😁 : ")
        print([kv for kv in bdays.items() if kv[1] in this_day],end="")  # ..then match it to the index position one of the dictionary item, n print
        partyday = [kv for kv in bdays.items() if kv[1] in this_day] # ..then match it to the index position one of the dictionary item, n print
        #print(partyday)
        # added a feature to email me when a birthday is found for today, this is also done as a cronjob
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login("myemailtosend@gmail.com","mypassword")
        smtpObj.sendmail("myemailtosend@gmail.com", "receivingemail@gmail.com", "Subject:Birthday Today!! \nHi Lloyd,\nBirthday found today: {} .".format(partyday))
        smtpObj.quit()
        
    else:
        print('No birthday today ! 😕 ')  # if today's nobody's birthday

tOdAy()


def toMorRow():                    # this block of  code defines the 'tomorrow' function and searches for birthdays that match tomorrow's date
    """ this function gets tomorrows's date"""
    morrow = datetime.now() + timedelta(days=1)
    toMorRow = (morrow.strftime('%b %d'))

    with open('bDay_db.json')as read_file:
        bdays = json.load(read_file)

    if toMorRow in bdays.values():
        print()
        print("Birthday match found for tomorrow 😉 !!")
        pprint.pprint([kv for kv in bdays.items() if kv[1] in toMorRow])
        print()

    else:
        print()
        print('No birthday tomorrow ! 😕')
        print()
        print()

toMorRow()


def laterThisWeek():
    """ this function gets the next upcoming days starting from two days from now"""
    coming_up = datetime.now()

    with open('bDay_db.json')as read_file:
        bdays = json.load(read_file)

    for x in range(2, 5):
        soon = (coming_up + timedelta(days=x))
        upcoming = (soon.strftime('%b %d'))
        #pprint.pprint(upcoming)
   
        if upcoming in bdays.values():
            print("Birthday match found in next couple of days: ")
            print([kv for kv in bdays.items() if kv[1] in upcoming],end="")
            print()
            break
            

    else:
        if upcoming not in bdays.values():
            #print()
            print('No upcoming birthday later this week ! 😕')
            #pass
         

laterThisWeek()

def yesterday():
    """ this function gets yesterday's date"""
    yestee = datetime.now() - timedelta(days=1)
    yesterday = (yestee.strftime('%b %d'))

    with open('bDay_db.json') as read_file:
        bdays = json.load(read_file)

    if yesterday in bdays.values():
        print('\n\n')
        print("Better late than never!! yesterday was the birthday of : ")
        print([kv for kv in bdays.items() if kv[1] in yesterday])
yesterday()


while True:
    print()  # this block, takes Name input or exits the program if none is given
    birthday = input("Pls enter a name to query the database, or press 'Enter' to exit : ").lower().title()
    if birthday == "":
        print()
        print("Exiting, have a nice day !!\n\n".title())
        break

    if birthday in dob:     # if an existing key/value is given from previous block, this block returns the birthday
        print()  
        pprint.pprint(dob[birthday] + " is the birthday of " + birthday)

    else:  # if no records found, this block takes input to update the Db.
        if birthday not in dob:
            print(birthday + " is not yet stored, do you want to add " + "'" +birthday+"'" + " to the Db ? ")
            print()
            response = pyip.inputMenu(['Yes', 'No'],lettered=False, numbered=True)
            if response == "Yes":
                pass
            else:
                continue

            key1 = input('kindly enter the name of ' + "'" + birthday + "'" + " exactly how you want it saved : ").lower().title()  # the key item (name)
            if key1 == "":  # if nothing is entered, the program exits with the break function
                print("Exiting, have a nice day ! ")
                break
            print()
            value1 = input("kindly enter the date as 'mmm dd' : ").lower().title()  # the value(date of birth- Jan 01) of the Key(name)
            if value1 == "":  # if nothing is entered, the program exits with the break function
                break
            print()
            print("storing the input : ".title())
            dob1 = {}  # an empty dictionary to catch the inputs of previous block
            dob1[key1] = value1  # assigning the entered key and value to the dictionary
            print(dob1)  # just to see what has been entered
            print()

            update_db = dob.update(dob1)  # updating the original dictionary with the recently added dictionary (dob1)
            print()
            print('Database has been updated')
            print()
            with open("bDay_dB.json","w") as write_file:  # this block opens the json database in order to append the new data from-
                json.dump(dob, write_file)  # previous blocks
                print()
                try:                                    # kept getting KeyError and didn't know how to apply the '.get()' function properly
                    print(dob[birthday] + " is the birthday of " + birthday)  # so opted for try and except
                except KeyError:
                    print()
                    print()

