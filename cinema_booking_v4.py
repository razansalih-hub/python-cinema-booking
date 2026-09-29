#This is an advanced v4 of cinema booking project
# -- CINEMA BOOKING -- 

import json

try:
    with open("bookings.json", "r") as f:
        data = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    data = {}
    
# 1- Welcome screen
print("=" *30)
print(" WELCOME TO RAZAN CINEMA ")
print("=" *30)
print(" ")
print("*" *50)

# 2- Movies Detalis
movies_by_day = {
    "Sunday" : ["The Godfather.", "Avatar.", "Oppenheimer."] ,
    "Monday" : ["Pulp Fiction.", "Gravity.", "Interstellar."] ,
    "Tuesday" : ["The Shawshank Redemption." , "Life of Pi.", "Dune: Part Two."] , 
    "Wednesday" : ["Parasite.", "Hugo.", "The Dark Knight."] ,
    "Thursday" : ["No Country for Old Men.", "Avatar: The Way of Water.", "Dunkirk."] , 
    "Friday" : ["Whiplash.", "Tron: Legacy.", "Tenet."] ,
    "Saturday" : ["Knives Out.", "The Walk.", "Nope."]}
        
movies_details = { "The Godfather." : {"Type" : "Normal - Crime, Drama", "Price" : 8} ,
    "Avatar." : {"Type" : "3D - Sci-Fi, Adventure" , "Price" : 12} , 
    "Oppenheimer." : {"Type" : "IMAX - Historical, Biography, Drama" , "Price" : 15} , 
    "Pulp Fiction." : {"Type" : "Normal - Crime, Drama" , "Price" : 8} , 
    "Gravity." : {"Type" : "3D - Sci-Fi, Thriller" , "Price" : 12} , 
    "Interstellar." : {"Type" : "IMAX - Sci-Fi, Drama, Adventure" , "Price" : 15} , 
    "The Shawshank Redemption." : {"Type" : "Normal - Drama" , "Price" : 8} , 
    "Life of Pi." : {"Type" : "3D - Adventure, Drama, Fantasy" , "Price" : 12} , 
    "Dune: Part Two." : {"Type" : "IMAX - Sci-Fi, Adventure" , "Price" : 15} , 
    "Parasite." : {"Type" : "Normal - Thriller, Drama" , "Price" : 8} , 
    "Hugo." : {"Type" : "3D - Adventure, Family, Fantasy" , "Price" : 12} , 
    "The Dark Knight." : {"Type" : "IMAX - Action, Crime, Drama" , "Price" : 15} , 
    "No Country for Old Men." : {"Type" : "Normal - Crime,Thriller,Neo-Western" , "Price" : 8} , 
    "Avatar: The Way of Water." : {"Type" : "3D - Sci-Fi, Action, Adventure" , "Price" : 12} , 
    "Dunkirk." : {"Type" : "IMAX - Historical, War, Action" , "Price" : 15} , 
    "Whiplash." : {"Type" : "Normal - Drama, Music, Psychological Thriller" , "Price" : 8} , 
    "Tron: Legacy." : {"Type" : "3D - Sci-Fi, Action, Adventure" , "Price" : 12} , 
    "Tenet." : {"Type" : "IMAX - Sci-Fi, Action, Thriller" , "Price" : 15} , 
    "Knives Out." : {"Type" : "Normal - Comedy, Mystery, Crime" , "Price" : 8} , 
    "The Walk." : {"Type" : "3D - Biography, Drama, Adventure" , "Price" : 12} , 
    "Nope." : {"Type" : "IMAX - Sci-Fi, Horror, Mystery" , "Price" : 15} , 
    }
    
showtimes = {
    "The Godfather."           : "2:00 PM",
    "Avatar."                  : "5:00 PM",
    "Oppenheimer."             : "9:00 PM",
    "Pulp Fiction."            : "2:00 PM",
    "Gravity."                 : "5:00 PM",
    "Interstellar."            : "9:00 PM",
    "The Shawshank Redemption.": "2:00 PM",
    "Life of Pi."              : "5:00 PM",
    "Dune: Part Two."          : "9:00 PM",
    "Parasite."                : "2:00 PM",
    "Hugo."                    : "5:00 PM",
    "The Dark Knight."         : "9:00 PM",
    "No Country for Old Men."  : "2:00 PM",
    "Avatar: The Way of Water.": "5:00 PM",
    "Dunkirk."                 : "9:00 PM",
    "Whiplash."                : "2:00 PM",
    "Tron: Legacy."            : "5:00 PM",
    "Tenet."                   : "9:00 PM",
    "Knives Out."              : "2:00 PM",
    "The Walk."                : "5:00 PM",
    "Nope."                    : "9:00 PM",
}

def show_movies(day) :
    print(f"{day}'s movies are:")
    counter = 1
    for movie in movies_by_day[day] :
        print(f"{counter}- {movie}")
        counter += 1
     
def show_movie_details(chosen_film) :
    print(f"Details for '{chosen_film}': ")
    for key, value in movies_details[chosen_film].items() :
        print(f"{key} : {value}.")
    print(f"Showtime: {showtimes[chosen_film]}")

def apply_discount(price) :
    membership = input("\nAre you a member of the cinema? (yes/ no) ").strip().lower()
    if membership == "yes" :
        price = price * 0.9
        print("You have a Discount of 10%!")
        print(f"Your Current Price is: ${price:.2f}")
    else :
        print("No Discount.")
    isstudent = input("\nAre you a student? (yes/no) ").strip().lower()
    if isstudent == "yes" :
        price = price * 0.8
        print("You have a discount of 20%!")
        print(f"Your current Price is: ${price:.2f}")
    else :
        print("No Discount.")
    return price

def print_ticket(film, day, showtime, price):
    print("=" * 40)
    print("  YOUR TICKET  ".center(40))
    print("=" * 40)
    print(f"Movie    : {film}")
    print(f"Type     : {movies_details[film]['Type']}")
    print(f"Day      : {day}")
    print(f"Showtime : {showtime}")
    print(f"Price    : ${price:.2f}")
    print("=" * 40)

def confirm_booking():
    confirm = input("\nConfirm booking? (yes/no): ").strip().lower()
    if confirm == "yes" :
        return True
    else:
        return False

def show_all_bookings(user_bookings):
        if len(user_bookings) == 0 :
            print("You didn't confirm any bookings yet.")
            return
        number = 1
        print(f"You have {len(user_bookings)} booking.")
        for booking in user_bookings :
            print(f"\n-booking ~{number}: ")
            for key, value in booking.items() :
                print(f" {key}: {value}")
            number += 1

username = input("What's your name? ").strip().lower()

if username in data:
    user_bookings = data[username]
    print(f"Welcome back, {username}!")
    if len(user_bookings) > 0:
        view = input(f"You have {len(user_bookings)} previous booking(s). View them? (yes/no): ").strip().lower()
        if view == "yes":
            show_all_bookings(user_bookings)
else:
    data[username] = []
    user_bookings = []
    print(f"Welcome, {username}!")

session_bookings = []

see = input("Do you want to see this week available movies? (yes/no) ").strip().lower()

if see == "yes" :
    while True :
        day = input("Choose a day : ").strip().title()
        if day in movies_by_day :       
            show_movies(day)
        
            choice = int(input("Choose a movie please (1-3) :"))
            if choice == 1:
                chosen_film = movies_by_day[day][0]
            elif choice == 2:
                chosen_film = movies_by_day[day][1]
            elif choice == 3:
                chosen_film = movies_by_day[day][2]
            else:
                print("Invalid choice, try again")
                continue
            show_movie_details(chosen_film)
            price = movies_details[chosen_film]['Price']
            final_price = apply_discount(price)

            print(f"Your final price is: ${final_price:.2f}")
            answer = confirm_booking()
            if answer == True :
                print("Booking confirmed!")
                print_ticket(chosen_film, day, showtimes[chosen_film], final_price)
    
                booking = { "Movie" : chosen_film ,
                "Day" : day ,
                "Showtime" : showtimes[chosen_film] ,
                "Ticket Price" : final_price ,
                }
                user_bookings.append(booking)
                session_bookings.append(booking)
                data[username] = user_bookings
                with open("bookings.json" , "w") as f:
                    json.dump(data, f, indent=4)
    
            else :
                print("Booking cancelled!")
            ticket2 = input("Do you want to book another ticket? (yes/no) ").strip().lower()
            if ticket2 == "no" :
                print("\nOk,Thank you for choosing Razan Cinema!")
                show_all_bookings(session_bookings)
                
                view_all = input("View all your bookings? (yes/no) ").strip().lower()
                if view_all == "yes" :
                    show_all_bookings(user_bookings)
                break

        else :
            print("Invalid day!")
            continue
            
elif see == "no" :
    print("Ok.")