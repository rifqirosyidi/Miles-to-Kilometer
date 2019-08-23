# ======= Simple Converting Miles to Km ========

# Ask user to enter number of miles
miles = input("Enter a Miles (number) : ")

# check if in user input is not a digit number
while not miles.isdigit():

    # ask to enter a number again
    miles = input("Please enter a number of mile : ")

    # check if user has input the correct value
    if miles.isdigit():
        break

miles = int(miles)
# convert miles to km
kilometers = miles * 1.60934
kilometers_2 = round(kilometers, 2)

print(f'{miles} miles is equal to {kilometers_2} kilometer')




