# 🎬 Razan Cinema Booking (Python Project)

## Description
A beginner-friendly Python project that simulates a cinema booking system. 
The user selects a day, chooses a movie from that day's schedule, and views full details 
(type, price, showtime) before confirming the booking. All movie data is stored in nested 
dictionaries and lists.

This is my fifth Python project, part of my learning journey toward robotics and AI.

## Features
- Displays available movies for each day of the week
- Uses nested dictionaries to store movies, details, and showtimes
- Validates the user's chosen day with `in`
- Lets the user pick a movie by number (1–3)
- Shows full movie details: type, price, and showtime
- Asks for booking confirmation (yes/no)
- Cleans user input with `.strip().title()` and `.strip().lower()`

## Example Run
```

==============================
🎬 WELCOME TO RAZAN CINEMA 🎬
==============================

Please choose a day: sunday

Here is Sunday movies

1. The Godfather.
2. Avatar.
3. Oppenheimer.

==================================================
Which movie you want to watch (1-3)? 2

This is your movie details:

---

Movie type is: 3D - Sci-Fi, Adventure

Ticket price is: $12

Movie show time is: 5:00 PM

==================================================

Do you want to confirm your booking (yes/no)? yes
Your booking is confirmed!!

```

## Concepts Practiced
- Dictionaries (simple + nested)
- Dictionary of Lists
- Accessing nested data with multiple keys
- `in` operator for validation
- `if / elif / else` for decision making
- String methods: `.strip()`, `.title()`, `.lower()`
- Type conversion with `int()`
- f-strings for formatted output
- User input handling
- Booking confirmation logic

## How to Run
```bash
python cinema_booking.py
```

Author

Razan — Learning Python step by step, aiming for robotics and AI 🦿
GitHub: @razansalih-hub

```
