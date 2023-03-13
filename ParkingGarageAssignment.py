class Garage():

    def __init__(self): 
        self.capacity = 100
        self.tickets = [i for i in range(1,100)]
        self.parkingSpaces = [i for i in range(1, 100)]
        self.currentTicket = {} 
        self.occupiedSpaces = []
    
    def takeTicket(self): 
        print (f"There are {len(self.parkingSpaces)} parking spots available.")
        print("Please take a ticket.")
        self.parkingSpaces = self.parkingSpaces[:-1]
        self.tickets = self.tickets[:-1]

    def payForParking(self):
        hours = int(input("How many hours did you park? "))
        ticket_price = int(hours) * 10 
        print(f'Your total is {ticket_price}')
        payment = input("Would you like to pay?")
        if payment == "yes":
            ticket_id = input("Enter your ticket_id.")
            ticket_price = int(hours) * 10
            print(f'This is your ticket number:{ticket_id} and your payment is {ticket_price}.')
            self.currentTicket[ticket_id] = {'paid': True}
            print("Thank you! Your ticket has been paid. You have 15 minutes to leave. ")
        elif payment == "no":
            self.currentTicket = {"paid": False}
            print("Sorry, you need to pay to leave.")
        else: 
            print("Please try again.")
        

    def leaveGarage(self):
        ticket_id = input("Enter your ticket number: ")
        if ticket_id in self.currentTicket:
            del self.currentTicket[ticket_id]
            self.parkingSpaces.append(int(ticket_id) - 1)
            self.tickets.append(int(ticket_id))
            print("Thank you! Have a nice day!")
        else:
            print("Invalid ticket number.")
    
    def exit_program(self):
        quit()


the_moon_garage = Garage()

print("Welcome to the Moon Garage!")
print("Hourly rates are $10.")
print("Type 1 to take a ticket.")
print("Type 2 to pay for parking.")
print("Type 3 to leave the garage.")
print("Type 4 to exit.")


def run():
    while True:
        an_input = input("What would you like to do? ")

        if an_input == "1":
            the_moon_garage.takeTicket() 
        elif an_input == "2":
            the_moon_garage.payForParking()
        elif an_input == "3":
            the_moon_garage.leaveGarage() 
        elif an_input == "4":
            the_moon_garage.exit_program()
        else: 
            print("Please enter a valid option.")

run()