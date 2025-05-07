#checks for an integer with optional upper / 
# lower limits and an optional exit code for infinite mode
# / quitting the game
def int_check(question, low=None, high=None, exit_code=None):


# Guessing LookupError

#replace number below with random with random number between high / low values
secret = 7

# parameters that already exist in base game
low_num = 0
high_num = 10
guesses_allowed = 5

# Set guesses used to zero at the start of each round
guesses_used = 0
already_guessed = []

guess = ""
while guess != secret and guesses_used < guesses_allowed:

    # ask the user to guess the number
    guess = int_check(question= "Guess: ", low_num, high_num, exit_code)

    # check that they don't want to quit
    if guess == "xxx":
