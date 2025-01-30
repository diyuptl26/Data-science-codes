#Creating Variables 
Name= input("Enter your name: ")
Age= int(input("Enter your age: "))
Height_in_meters= float(input("Enter your height: "))
#Determine if the user is  a student 
is_student= input("Are you a stduent? (yes/no):").strip().lower()== "yes"
if is_student:
  print("You are currently considered as a student")
else:
 print("You are currently not a student")

#function to calulate if it is a leap year 
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#Get Birthdate 
BirthDay= int(input("Enter the Birth Day: "))
BirthMonth= int(input("Enter the Birth Month: "))
BirthYear= int(input("Enter the Birth Year: "))

# Get today's date 
CurrentMonth= int(input("Enter Current Month: "))
CurrentDate= int(input("Enter today's date: "))
CurrentYear= int(input("Enter Current year: "))

#Now lets calculate days lived 
DaysLived = 0
#Add days for full years lived 
for year in range (BirthYear, CurrentYear):
  if is_leap_year(year):
   DaysLived += 366 
  else:
   DaysLived += 365

#Subtract days from the current year before the birthdate 
if is_leap_year(CurrentYear):
  days_in_months[1]=29 #Adjust February for leap year 
DaysLived += sum(days_in_months[:CurrentMonth-1]) + CurrentDate
DaysLived -= sum(days_in_months[:BirthMonth-1]) + BirthDay
print(f"You have lived for {DaysLived} days")

# Lists
#Create a list of five of your favorite sports
FavSports= ['Volleyball', 'Basketball', "Soccer", "Cricket", "Badminton"]
#Add a new sport to the list
FavSports.append("Athletics")
#Remove the third item from the list
del FavSports[2]
#Sort the list alphabetically
FavSports.sort()
#Reverse the order of the list
FavSports.reverse()
#Print the first and last items in the list

print("First item:",FavSports[0])
print("Last item:", FavSports[-1])

#Dictionaries
#Create a dictionary that stores information about a book (title, author, year published, genre)
book = {
  "Title": "Ramayan", 
  "Author": "Swamimukundananda", 
  "YearPublished": 2018, 
  "Genre": "Itihasa"
  }
#Add a key-value pair for the number of pages
book["NoOfPages"]= 235
#Update the year published to a different year
book["YearPublished"]= 2024
#Delete the author key-value pair
del book ["Author"]
#Print the title of the book
print("Title of the book: ",book["Title"] )

#Tuples
# Create a tuple with five elements
MyTuple= ("Purple", 2001, 5, True, 5.2)
# Print the entire tuple
print("The entire Tuple: ", MyTuple)
# Access and print the 4th element of the tuple
print("Fourth element of the tuple is:", MyTuple[3])
# Try to change the 3rd element of the tuple
try:
  MyTuple[2]= 6  #attempting to change third element
except TypeError as e:
  print("Error:",e)


#COMBINING DATA STRUCTURES
FriendInfo= { 
  "Madhuri": (22, "Purple"),
  "Dhara":   (20, "Blue"),
  "Nidhi":   (22, "White")
}
