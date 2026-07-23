# ✈️ ShubhYatra - Travel Booking Backend API (Django + DRF + MySQL)

A **RESTful Travel Booking Backend API** built using **Django**, **Django REST Framework (DRF)**, and **MySQL**. The project enables users to browse travel routes, transport modes, seat availability, and book tickets through secure REST APIs. It supports JWT Authentication, CRUD operations, search, filtering, pagination, and automatic fare calculation. All APIs were developed and tested using **Postman**.

---

# 📁 Project Structure

```text
Backend/
├── travelapp/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── routers.py
│   ├── serializers.py
│   ├── tests.py
│   └── viewsets.py
│
├── shubhYatra/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
└── README.md
```

---

# 🚀 Features

- 🔐 JWT Authentication using Django REST Framework Simple JWT
- 👤 User Registration & Login
- 🚆 Travel Mode Management
- 🚍 Mode Type Management
- 🛣️ Route Management
- 💺 Seat Availability & Booking
- 🎫 Ticket Booking System
- 💰 Automatic Fare Calculation
- 🗄️ MySQL Database Integration
- 🔗 RESTful APIs using Django REST Framework
- ⚡ ModelSerializers for JSON Serialization
- 🔄 RESTful CRUD APIs using DRF ModelViewSets & Routers
- 🔍 Search using DRF SearchFilter
- 🎯 Filtering using DjangoFilterBackend
- 📄 Pagination for Efficient API Responses
- 🧪 API Development & Testing using Postman
- 🛠️ Django Admin Panel

---

# 📌 API Capabilities

- 🔐 JWT Authentication
- 👤 User Registration & Login
- 🚍 Travel Booking CRUD Operations
- 🔄 JSON Serialization
- 🔍 Search
- 🎯 Filtering
- 📄 Pagination
- 🔗 Foreign Key Relationships
- 💰 Automatic Fare Calculation
- 💺 Seat Availability Management

---

# 🛠️ Tech Stack

- Python
- Django
- Django REST Framework (DRF)
- MySQL
- Simple JWT
- Postman

---

# 📂 Database Models

## Mode

Stores available transport modes.

**Fields**

- Mode Name

---

## ModeType

Stores transport services with pricing.

**Fields**

- Service
- Mode
- Price Per Kilometer

---

## Route

Stores travel routes.

**Fields**

- Source
- Via
- Destination
- Distance

---

## Seat

Stores seat availability.

**Fields**

- Mode Type
- Route
- Seat Number
- Booking Status

---

## Book

Stores ticket booking information.

**Fields**

- Mode Type
- Route
- Seat
- Number of Passengers
- Total Price

**Computed Properties**

- Automatic Fare Calculation
- Booking Confirmation

---

# 🔗 Database Relationships

```text
Mode
   │
   └──────< ModeType
                 │
                 ├──────< Seat
                 │
                 └──────< Book

Route
   │
   ├──────< Seat
   │
   └──────< Book
```

---

# 🌐 API Endpoints

| Endpoint | Description |
|----------|-------------|
| `/mode/` | Manage Transport Modes |
| `/modetype/` | Manage Mode Types |
| `/route/` | Route CRUD Operations |
| `/seat/` | Seat Availability Management |
| `/book/` | Ticket Booking Management |
| `/token/` | Generate JWT Access & Refresh Tokens |
| `/token/refresh/` | Refresh JWT Access Token |

---

# ▶️ Application Workflow

```text
User Registration / Login
          │
          ▼
JWT Authentication
          │
          ▼
Browse Travel Modes
          │
          ▼
Select Mode Type
          │
          ▼
Search & Filter Routes
          │
          ▼
View Available Seats
          │
          ▼
Select Seat
          │
          ▼
Calculate Fare
          │
          ▼
Book Ticket
          │
          ▼
Store Booking in MySQL Database
          │
          ▼
View Booking Details
```

---

# 🚀 Future Improvements

- 💳 Online Payment Gateway Integration (Stripe/Razorpay)
- 📧 Email Ticket Confirmation
- 📱 SMS Notifications
- 📍 Live Vehicle Tracking
- ⭐ User Ratings & Reviews
- ❤️ Favorite Routes
- 📄 PDF Ticket Generation
- 🌍 Multi-language Support
- 🎟️ Coupon & Discount System
- 👨‍💼 Role-Based Access Control (Admin, Operator & Passenger)
- 🐳 Docker Containerization
- ☁️ Cloud Deployment (AWS, Render, Railway)
- 📖 API Documentation using Swagger/OpenAPI
- 🧪 Unit & Integration Testing
- ⚡ Redis Caching for Improved Performance
