# 🎬 Razan Cinema Booking (Python Project)

## Description
A beginner-friendly Python cinema booking system with two versions:
- **v1** (`Movie_ticket.py`): Basic version without loops.
- **v2** (`cinema_booking_v2.py`): Advanced version with loops, nested dictionaries, 
  discounts, and multiple bookings per session.

This project is part of my Python learning journey toward robotics and AI.

## 📌 Versions

### 🥉 v1 — `Movie_ticket.py`
The starting point: a basic script without loops.

- Week-long movie schedule (dictionaries of lists)
- Day selection with `in` validation
- Movie selection by number
- Booking confirmation (single ticket only)

### 🥈 v2 — `cinema_booking_v2.py`
Added loops for multiple bookings.

- Everything in v1
- **`while True`** loop for multiple bookings in one session
- **`for` loop** for displaying numbered movie lists
- **`.items()`** to display movie details dynamically
- **Membership discount** (10%)
- **Student discount** (20%)
- **List of Dictionaries** to store all bookings
- Displays all confirmed bookings at the end
- Full ticket formatting with separators

### 🥇 v4 — `cinema_booking_v4.py` **(Latest & Most Advanced)**
Full version with functions, user sessions, and JSON persistence.

- Everything in v2
- **6 custom functions** for clean, modular code:
  - `show_movies()` — display movies for a day
  - `show_movie_details()` — show movie info
  - `apply_discount()` — handle pricing logic
  - `print_ticket()` — formatted ticket output
  - `confirm_booking()` — returns boolean
  - `show_all_bookings()` — display a list of bookings
- **Per-user sessions** — each user has their own booking history
- **JSON file persistence** — bookings are saved to `bookings.json` and loaded on startup
- **Session vs. history** — shows current session bookings by default, with option to view all
- **Input validation** — handles invalid days and invalid movie choices
- **`try/except`** — gracefully handles missing or empty JSON files

---

## ✨ Features

-  Display weekly movie schedule (7 days × 3 movies)
-  Choose day and movie interactively
-  View full movie details (type, price, showtime)
-  Apply membership and student discounts (cumulative)
-  Confirm or cancel bookings
-  Book multiple tickets in one session
-  Per-user booking history (via JSON)
-  Save bookings to file — persists between sessions
-  Session view vs. full history view
-  Fully formatted ticket output

---

## 🧠 Concepts Practiced

| Concept | Where It's Used |
|---|---|
| **Nested Dictionaries** | `movies_details` (movie info) |
| **Dictionary of Lists** | `movies_by_day` (schedule) |
| **Simple Dictionary** | `showtimes`, `data` (users) |
| **Lists of Dictionaries** | `user_bookings`, `session_bookings` |
| **`while` loops** | Multiple bookings, retry logic |
| **`for` loops** | Iterating over movies, bookings |
| **`break` / `continue`** | Exit loops, skip invalid input |
| **Functions + `return`** | All 6 custom functions |
| **Parameters & Arguments** | Passing data between functions |
| **`try/except`** | Handling missing/corrupt JSON |
| **File I/O** | Reading/writing `bookings.json` |
| **`json` module** | Serializing/deserializing data |
| **String methods** | `.strip()`, `.title()`, `.lower()`, `.center()` |
| **f-strings + formatting** | `.2f` for prices, `.center()` for layout |
| **Boolean logic** | `in`, `and`, comparisons |

---


# Run v2
python cinema_booking_v2.py
