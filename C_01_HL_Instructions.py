# functions go here

def yes_no(question):
    """Checks user response to a question is yes / no (y/n), return 'yes' or 'no'"""

    while True:

        response = input(question).lower()

        # check the user says yes / no/ /y / n
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")


def instructions():
    """Prints instructions"""

    print("""
*** Instructions ***

To begin, choose the number of rounds and either customise 
the game parameters or go with the default game (where the 
secret number wil be between 1 and 100).
          
Then choose how many rounds you'd like to play <enter> for 
infinite mode.
          
Your goal is to try to guess the secret number without 
running out of guesses.
          
 Good luck!
    """)


# Main routine
print()
print("🔼🔼🔼 Welcome to the Higher Lower Game🔽🔽🔽")
print()
# ask the user if they want to see instructions (check is they say yes / no)
want_instructions = yes_no("Do you want to see the instructions?")

# Display the instructions if the user want to see them...
if want_instructions == "yes":
    instructions()

print()
print("program continues")
