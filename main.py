#### PART 1: INTRO TO PYTHON ####

#### Hello World
# print("Hello World")






#### Data types
## strings -
# print("4" + "3")

# ## integers -
# print(4 + 3)

# ## floats -
# print(4.0 + 3.0)

# ## a mix of types ##
## A float and an integer
# print(4 + 3.0)

## A string and an integer
# print("4" + 3)

#### QUICK NOTES:
## Adding two strings is called ___________



#### Data type conversion
# ## This first example converts the ___________ 3 into ___________ and then concatenates.
# print("4" + 3)

# ## This second example converts the ___________ "4" into ___________ and then adds.
# print("4" + 3)





#### PART 2: USER INPUT ####
## The input function automatically captures input as a string
# name = input("what is your name?")
# print("Hello", name)

## To capture other types of data, be sure to convert it as a type
# user_age = int(input("what is your age?"))
# print("Wow, I'm", user_age, "too!")


##### EXAMPLE 1:
# name = input("what is your name?")
# if name == "Jeff":
#   print("Welcome to the program!")
#   print("The secret message is: Janelle Monae is v. v. cool.")
# print("Program over. Shutting down.")
### Questions before running:
# How many lines will print if I tell the computer my name is "Jeff"?
# How many lines will print if I tell the computer my name is "jeff"?


### EXAMPLE 2
# name = input("what is your name?")
# if name == "Jeff" or name == "jeff":
#   print("Welcome to the program!")
#   print("The secret message is: Janelle Monae is v. v. cool.")
# else:
#   print("Unauthorized User. Only Jeff can use this computer.")
# print("Program over. Shutting down.")
### Questions before running:
# How is this version different from the last one?
# Why is this version of the program better than the last one?


### EXAMPLE 3
# name = input("what is your name?")
# if name == "Jeff":
#   user_age = int(input("What is your age? "))
#   if user_age > 30:
#     print("You look about", user_age-30, "years older than Jeff. Intruder detected!")
#   elif user_age < 30:
#     print("You are too young to be Jeff!")
#   else:
#     print("Welcome to the program!")
#     print("The secret message is: Janelle Monae is v. v. cool.")
# else:
#   print("Unauthorized User. Only Jeff can use this computer.")
# # input("Press return to continue")
# print("Program over. Shutting down.")
### Questions before running:
# What will happen if I tell it my name is Jeff and I'm 40 years old? (right name, wrong age)
# What will happen if I tell it my name is Alyssa and I'm 30 years old? (right age, wrong name)




##### QUICK NOTES
## IF and ELSE lines end with colons and are called conditionals
## Indentation determines what belongs to a conditional and where it ends.
## Use inputs (that aren't saved to variables) to add in pauses for the user. 
