#This is project five with Python
# -- CINEMA BOOKING WEBSITE  -- 

# 1- Welcome screen
print("=" *30)
print("🎬 WELCOME TO RAZAN CINEMA 🎬")
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

#Showing avalible Movies by day
day = input("Please choose a day: ").strip().title()
print("""
""")
if day in movies_by_day: 
    print(f"Here is {day} movies")
    print(" ")
    print(f"1. {movies_by_day[day][0]}")
    print(f"2. {movies_by_day[day][1]}")
    print(f"3. {movies_by_day[day][2]}")
else:
    print("Sorry we don't have shows on that day.")

print("""
""")
print("=" *50)
choice = int(input("Which movie you want to watch (1-3)? "))

if choice == 1:
    chosen_film = movies_by_day[day][0]
elif choice == 2:
    chosen_film = movies_by_day[day][1]
elif choice == 3:
    chosen_film = movies_by_day[day][2]
else:
    print("Invalid choice")
    exit()
    
print("This is your movie details:")
print("*" *3)
print(f"Movie type is: {movies_details[chosen_film]['Type']}")
print(" ")
print(f"Ticket price is: ${movies_details[chosen_film]['Price']}")
print(" ")
print(f"Movie show time is: {showtimes[chosen_film]}")
print(" ")
print("*" *50)
print(" ")
confirm = input("Do you want to confirm your booking (yes/no)? ").strip().lower()
if confirm == "yes" :
    print("Your booking is confirmed!!")
else :
    print("See you next time then!!")