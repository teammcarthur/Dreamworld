'''
Author: Chris McArthur
Date: 31/07/25
Version: 1.0
Description: Program to check if you are eligible for Dreamworld rides.
'''
print('Dreamworld - are you eligible to take the rides')
while(True):
    age = (input('Enter your age:'))
    if age.isnumeric and age < 130 and age > 0:
        print('test')
        break
    else:
        print('This is an invalid age, please try again')
        continue
while(True):
    height = (input('Enter your height (cm):'))
    if height.isnumeric and height < 300 and height > 10:
        print('test')
        break
    else:
        print('This is an invalid height, please try again')
        continue
ageint = int(age)
print('You can go on the following rides: ')
if(height > 150):
    print('Stratosphere', 'Family Karts', 'Scorpion Karts')
if(height > 120):
    print('Fearfall', 'Invader', 'Corkscrew Roller Coaster', 'Bumper Boats')
if(height > 90 and ageint > 5):
    print('Los Banditos')
    if(ageint > 8):
        print('Robot Riot')
if(height > 80):
    print('Log Flume', 'Gold Rush', 'Family Karts', 'Dogems')
if(height < 80 and ageint >= 3 and ageint <= 8):
    print('Fortress of Fun')