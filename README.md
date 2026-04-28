# Travel-Booking-website


A backend travel booking system built with Django and Django REST Framework that manages transport modes, routes, seats, and ticket bookings with automatic fare calculation.

 Features
Manage travel modes (Bus, Train, Flight, Cab, etc.)
Add service types for each mode
Create travel routes with distance and via points
Manage seats for each route
Prevent duplicate seat booking
Automatic ticket price calculation
REST API with CRUD operations
Booking confirmation messages
🛠️ Tech Stack
Python
Django
Django REST Framework
SQLite / MySQL
📂 Project Structure
travel_booking/
│── models.py
│── serializers.py
│── viewsets.py
│── urls.py


🧩 Database Models
1. Mode
Stores travel categories.

Examples:
Bus
Train
Flight

2. ModeType
Stores service type under each mode.

Examples:
AC Sleeper Bus
Express Train
Economy Flight

Fields:
modes
service
price_per_km


3. Route
Stores travel routes.

Fields:
source
destination
via
distance


4. Seat
Stores seat details.

Fields:
mode
route
seat_no
is_booked


5. Book
Stores booking information.

Fields:
mode
route
passengers
seat
total_price
💰 Price Calculation
total_price = price_per_km × distance × passengers


🔌 API Endpoints
Endpoint	Description
/modes/	Manage transport modes
/modetype/	Manage services
/routes/	Manage routes
/Seats/	Manage seats
/bookings/	Book tickets
📥 Sample Booking Request
POST /bookings/

{
  "mode": 1,
  "route": 1,
  "passengers": 2,
  "seat": 3
}
Response
{
  "mode": 1,
  "route": 1,
  "passengers": 2,
  "seat": 3,
  "total_price": 960,
  "message": "Your ticket for route is successfully booked"
}
🔒 Validation
Prevent Duplicate Seats

Same seat number cannot be added twice for same route and mode.

unique_together = ['route', 'seat_no', 'mode']




🌟 Future Improvements
User Authentication
Payment Gateway
Cancel Booking
Search API
Admin Dashboard
Booking History
Email Confirmation
QR Code Ticket\

Still this is in development stage once I finished frontend,I will integerate with it.



👨‍💻 Author
Kishan BM

Screenshots
<img width="1118" height="782" alt="image" src="https://github.com/user-attachments/assets/d1e19619-cbf7-47e2-a5d3-f25f539bf332" />
<img width="959" height="692" alt="Screenshot 2026-04-28 192536" src="https://github.com/user-attachments/assets/5aecdc40-cf9b-416c-b789-29e0502de947" />



📜 License
this project is open source and free to use.


