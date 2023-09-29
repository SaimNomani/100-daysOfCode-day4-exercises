# You are going to write a program that will select a random name from a list of names. The person selected will have
# to pay for everybody's food bill.
#
# Important: You are not allowed to use the choice() function.
#
# splits the string names_string into individual names and puts them inside a List called names. For this to work,
# you must enter all the names as names followed by comma then space. e.g. name, name, name
#
# Example Input
# Angela, Ben, Jenny, Michael, Chloe
# Note: notice that there is a space between the comma and the next name.
#
# Example Output
# Michael is going to buy the meal today!
import random

names_str = input("Give me everybody's name followed by comma and then  space: ")
names = names_str.split(", ")
random_index = random.randint(0, len(names) - 1)
print(f"{names[random_index]} is going to buy the meal today!")
