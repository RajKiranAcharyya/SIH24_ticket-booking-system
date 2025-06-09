# SIH24 Ticket Booking System for Museums

## Overview

The **SIH24 Ticket Booking System** is an advanced, multilingual chatbot-driven platform designed to streamline the process of booking tickets for museums. This project is developed with a focus on providing an intuitive, user-friendly experience that caters to diverse users by supporting multiple languages and enabling seamless interaction.

By leveraging modern technologies, the system offers dynamic pricing models based on peak and off-peak hours, real-time seat availability updates to prevent double bookings, and secure payment processing through Stripe. In addition to ticket booking, the platform allows users to book personal guides, rent exhibition spaces, and schedule special events, making it a comprehensive solution for museum management and visitor engagement.

## Key Features

- **Multilingual Chatbot Interface:**  
  The system incorporates a chatbot that communicates in multiple languages, guiding users step-by-step through ticket booking, seat selection, and additional services with ease and clarity.

- **Real-Time Seat Availability:**  
  Users can view and select from available seats in real time, ensuring they only book from currently open spots and avoid conflicts or overbooking.

- **Dynamic Pricing Model:**  
  The platform automatically adjusts ticket prices depending on whether the booking falls within peak hours or off-peak times, optimizing revenue and visitor flow management.

- **Secure User Authentication:**  
  Using OAuth 2.0, the system ensures safe and reliable login, protecting user information and providing a trusted authentication mechanism.

- **Stripe Payment Gateway Integration:**  
  For smooth and secure transactions, the system integrates Stripe, a widely used payment processor that supports multiple payment methods.

- **Additional Booking Options:**  
  Beyond standard tickets, visitors can book personal museum guides, rent exhibition halls for events, and schedule participation in special museum programs.

- **User Interaction Tracking and Analytics:**  
  The system records user interactions to gather valuable insights, enabling continuous improvements in user experience and service offerings.

- **Technology Stack:**  
  - Backend: Python  
  - Frontend: HTML, CSS, JavaScript  
  - Authentication: OAuth 2.0  
  - Payments: Stripe API

## Detailed Component Description

### Backend (Python)

- Handles all core business logic including ticket booking, seat management, pricing adjustments, and service bookings.
- Implements APIs for user authentication and payment processing.
- Manages real-time data synchronization to keep seat availability updated.

### Frontend (HTML, CSS, JavaScript)

- Provides an interactive user interface with chatbot integration.
- Enables users to navigate through booking processes seamlessly.
- Responsive design for usability across devices.

### Authentication

- Utilizes OAuth 2.0 to allow users to securely log in using trusted third-party providers.
- Ensures secure session management and user data protection.

### Payment Integration

- Stripe is embedded to facilitate quick, secure payments.
- Supports multiple payment options including credit/debit cards and digital wallets.

## Repository Structure

├── index.html               # Main frontend HTML page
├── style.css                # Styling for the frontend
├── script.js                # JavaScript for frontend interactivity and chatbot
├── ticket_booking_system.py # Backend logic for ticket booking
├── user_authentication.py   # Handles OAuth 2.0 login and user sessions
├── payment_integration.py   # Stripe payment gateway integration
├── requirements.txt         # Python dependencies
├── SIH24_Ticket-booking-system.pdf # Project documentation/portal submission

## Getting Started

Follow these steps to run the project locally:

1. **Clone the repository:**

```bash
git clone https://github.com/RajKiranAcharyya/SIH24_ticket-booking-system.git
cd SIH24_ticket-booking-system


pip install -r requirements.txt

python ticket_booking_system.py

Open index.html in a web browser to start interacting with the booking system.

Usage
Use the chatbot interface to select your preferred language.

Follow the prompts to book tickets, select seats, and choose additional services.

Authenticate using OAuth 2.0 when requested.

Complete your payment securely through Stripe.

Receive confirmation of your booking instantly.

Future Enhancements
Expand chatbot language support and natural language processing.

Add mobile app support.

Implement advanced analytics dashboards for museum administrators.

Integrate with museum event calendars and notifications.

