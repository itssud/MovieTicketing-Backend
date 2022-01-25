# MovieTicketing-Backend
Dynamic movie ticketing system backed logic explored here...


Features added so far...
- arrangeSeats(screen) => creates random number of seats for a given screen
- categorisingSeats(screen) => creates categories ( Economy, Elite, Premium, Super Premium ) for the given screen's seating system
- getScreen(screen, out = False) => gets a single screen seating data, if out is True then it prints the seating arrangement in a readable manner.
- getAllScreens(out = False) => returns all screen seating data, if out is True, then it prints all the seating arrangements in a readable manner.
- availability(screen) => returns the available and booked number of seats as dictionary of a given screen
- bookTicket(screen, category, qty) => books the ticket for the given quantity in the given category if available


#### Output:

![movie ticketing output #1](https://user-images.githubusercontent.com/96824650/151038439-c2dcd841-a556-4664-8591-0636b448ec2c.PNG)
