# -*- coding: utf-8 -*-
"""

Created on Mon Jan 24 08:49:03 2022

@author: Sudarshan S


### Ticket booking application (backend logic) - Dynamic

- ticket repo
- dynamic money transfer (wallet)
- buy / cancellation / returns
- User repo

## Untitled Cinemas
- No. of screens in the theatre?
- No. of seats in every screen?
- Seats category - Economy - RS.64, Elite - Rs.120, Premium Rs.170, Super Premium Rs.195
- No. of movies run in a day?
- Movie show timings (8:00 AM, 11:00 AM, 1:40 PM, 4:25 PM, 7:10 PM, 10:30 PM)
- Booking ID

User Inputs
- Date
  - print available movies on that date
  - show time
  - seat category
  - payment status
"""
import random

# Enter number of screens
#no_of_screens = int(input('Enter the Number of Screens in the Theatre : '))
no_of_screens = 2

screens = ['AUDI' + str(screen+1) for screen in range(no_of_screens)]

print(f'Available Screens are : {screens}')

movies = ['Spiderman', 'Dark Knight', 'Iron Man', 'Captain America', 'Minal Murali']

show_timings = {'early morning' : '8:00 AM', 'morning' : '11:00 AM', 'matniee' : '1:40 PM', 'afternoon' : '4:25 PM', 'evening': '7:10 PM', 'night': '10:30 PM'}

no_of_seats = {screens[id] : random.randrange(50, 220) for id in range(no_of_screens)}

row_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

seat_categories_price = {'Economy' : 64, 'Elite' : 120, 'Premium' : 170, 'Super Premium' : 195}

seat_categories = [key for key,val in seat_categories_price.items()]


def arrangeSeats(screen):
    
    while True:
        col = random.randrange(5,25)
        row = no_of_seats[screen] // col
        remaining = no_of_seats[screen] % col
    
        if row > 8 and row < len(row_letters)-7 and remaining < col:
            break
        
    rows = { row_letters[idx] : [ {num+1 : True} for num in range(col) ] for idx in range(row) }
    if remaining:
        rows[row_letters[len(rows)]] = [{n+1 : True} for n in range(remaining)]
    
    return rows

def categorisingSeats(screen):

    seats_of_audi = arrangeSeats(screen)
    
    seat_categories_arranged = {}
    
    count = 0
    premium = {}
    elite = {}
    economy = {}
    for key, val in seats_of_audi.items():
        
        if count == 0:
            seat_categories_arranged['Super Premium'] = {key : val}
        elif count > 0 and count < 3:
            premium[key] = val
        elif count > len(seats_of_audi)-3 and count <= len(seats_of_audi):
            elite[key] = val
        else:
            economy[key] = val
            
        seat_categories_arranged['Premium'] = premium
        seat_categories_arranged['Economy'] = economy
        seat_categories_arranged['Elite'] = elite
        count+=1
    
    return seat_categories_arranged



all_screens_data = { screen : categorisingSeats(screen) for screen in screens }


def getScreen(screen, out = False):
    
    if out:
        print(f'\n{screen} - {no_of_seats[screen]} Seats')
        print('--------------------------')
        for cat, rows in all_screens_data[screen].items():
            print(f'\n{cat} : INR {seat_categories_price[cat]}\n')
            for key, val in rows.items():
                test = []
                for i in val:
                    for x,y in i.items():
                        if y == True:
                            test.append('| ' + str(x) + ' |')
                        else:
                            test.append('| X |')
                print(key + ' => ', ' '.join(test))
        print('--------------------------\n')
        
    else:
        return all_screens_data[screen]


   
def getAllScreens(out = False):
    if out:
        for screen in screens:
            getScreen(screen, True)
    else:
        return all_screens_data
        



def availability(screen):
    
    screen = getScreen(screen)
    seat_details = {}
    for category, value in screen.items():
        seat_details[category] = {}
        seat_details[category]['available'] = 0
        seat_details[category]['booked'] = 0
        for key, val in value.items():
            for i in val:
                for x,y in i.items():
                    if y == True:
                        seat_details[category]['available'] += 1
                    else:
                        seat_details[category]['booked'] += 1
    return seat_details

    


def bookTicket(screen, category, qty):
    
    count = 0
    available = availability(screen)[category]['available']
    if available > qty:
        for key, val in all_screens_data[screen][category].items():
            for i in val:
                for x,y in i.items():
                    if y == True:
                        if count <= qty:
                            all_screens_data[screen][category][key][x-1][x] = False
                            count += 1
    else:
        print(f'We cannot accommodate {qty} people in {category} category seats, please check with other category of seats...')

    getScreen(screen, True)





bookTicket('AUDI1', 'Elite', 11)


print(availability('AUDI1'))

