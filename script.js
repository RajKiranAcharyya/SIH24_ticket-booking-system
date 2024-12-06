let availableSeats = 100;

function bookTicket() {
    let numTickets = document.getElementById("num_tickets").value;
    if (numTickets <= availableSeats) {
        availableSeats -= numTickets;
        document.getElementById("response").innerHTML = `Successfully booked ${numTickets} tickets. Available seats: ${availableSeats}`;
    } else {
        document.getElementById("response").innerHTML = `Not enough seats. Only ${availableSeats} seats available.`;
    }
}
