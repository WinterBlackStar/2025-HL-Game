import math

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

# checks for an integer more than 0 (allows <enter>)
def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more"

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)
    
            # checks that the number is more than / equal to 13
            if response < 1:
                print(error)
            else:
                return response
            
        except ValueError:
            print(error)


# calculate the maximum number of guesses
def calc_guesses(low, high):
    num_range = high - low + 1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    return max_guesses


# Main Routine Starts here

# Initialise game variables
mode = "regular"
rounds_played = 0

print()
print("🔼🔼🔼 Welcome to the Higher Lower Game🔽🔽🔽")

want_instructions = yes_no("Do you want to read the instructions?")

# checks user enter yes (yes) or no (no)
if want_instructions == "yes":
    instructions()

# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for inifinte mode: ")

# Ask user for number of rounds / infinite mode
num_rounds = int_check(question= "Rounds <enter for infinite>: ",
                       low=1, exit_code="")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Get Game parameters
low_num = int_check("Low Number?")
high_num = int_check(question= "High Number?", low=low_num+1)
guesses_allowed = calc_guesses(low_num, high_num)

# Game loop starts here
while rounds_played < num_rounds:

    # Round headings
    if mode == "infinite":
        rounds_heading = f"\n000 rounds {rounds_played + 1} of {num_rounds} (Infinite Mode) 000"
    else:
        rounds_heading = f"\n 💿💿💿 round {rounds_played + 1} of {num_rounds} 💿💿💿"

    print(rounds_heading)
    print()

    user_choice = input("Choose: ")

    if user_choice == "xxx":
        break

    rounds_played += 1

    # if users are in infinite mode, increase number of rounds!
    if mode == "inifinte":
        num_rounds += 1


# Game loop ends here

# Game History / Statistics area
