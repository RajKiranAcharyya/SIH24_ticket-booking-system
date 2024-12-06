import random
from datetime import datetime


class TicketBookingSystem:
    def __init__(self):
        self.seats = 100  # Total number of available seats
        self.booked_seats = 0
        self.ticket_price = 20  # Base ticket price in USD

    def dynamic_pricing(self):
        """Increase price based on the day (peak and off-peak times)."""
        current_day = datetime.now().weekday()
        if current_day in [5, 6]:  # Saturday and Sunday (Peak days)
            self.ticket_price = 30  # Increased price
        else:
            self.ticket_price = 20  # Normal price
        return self.ticket_price

    def check_availability(self):
        """Check available seats."""
        available_seats = self.seats - self.booked_seats
        return available_seats

    def book_ticket(self, num_tickets):
        """Book tickets if seats are available."""
        available_seats = self.check_availability()
        if num_tickets <= available_seats:
            self.booked_seats += num_tickets
            print(f"Successfully booked {num_tickets} tickets.")
            print(f"Total cost: ${self.dynamic_pricing() * num_tickets}")
        else:
            print(f"Not enough seats. Only {available_seats} seats available.")

    def cancel_ticket(self, num_tickets):
        """Cancel booked tickets."""
        if num_tickets <= self.booked_seats:
            self.booked_seats -= num_tickets
            print(f"Successfully canceled {num_tickets} tickets.")
        else:
            print(f"You don't have {num_tickets} booked tickets to cancel.")


# Example Usage
ticket_system = TicketBookingSystem()

# Check for available seats
print("Available seats:", ticket_system.check_availability())

# Book 5 tickets
ticket_system.book_ticket(5)

# Cancel 2 tickets
ticket_system.cancel_ticket(2)

# Check available seats after booking and canceling
print("Available seats:", ticket_system.check_availability())
