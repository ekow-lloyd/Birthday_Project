
# a simple program that cleans up all the dummy names that i used in creating the database
# can also be used to remove unwanted names out of the database because of typo or whatever reason

import json

# this block opens the database (Db) in read-mode for query 
with open ("bDay_db.json", 'r') as readFile:
    bday = json.load(readFile)

# this is where the name to be removed is entered, if name isn't available, program catches the 'TyperError' 
while True:
    try:
        print('')
        dumName = input("Enter name to be removed from the DB: ").title()
        
        if dumName == '':
            print("Nothing entered, exiting program.")
            break

        if dumName in bday:
            bday.pop(dumName)
            print("All records of " + dumName + " has been wiped .")

            with open ('bDay_db.json', 'w')as writeFile:
                bday = json.dump(bday, writeFile)
                continue
                    
        else:
            if dumName not in bday:
                print('')
                print('No such record available')
                continue

    except TypeError:
        print('')
        print('Record no longer available after deletion !')
    
    except KeyboardInterrupt:
        print('')
        print('Program Interrupted !')
        print('')
        break
        

        

