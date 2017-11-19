import config
from random import randint
import os

#DEFINITIONS...
# Random list values
def get_value(args):
    value = args[randint(0, len(args) - 1)]
    value = str(value)
    return value

# Gets a random value from each list within a given list
def get_values(args):
    values = []
    for arg in args:
        value = get_value(arg)
        values.append(value)
    return values

# Gets the required password length
def get_length():
    message = "Please choose password length larger or equal to " + str(config.minimum) + ":\n>> "
    while True:
        try:
            password_length = int(input(message))
            while password_length < config.minimum:
                password_length = int(input(message))
            return password_length
        except ValueError:
            print("Invalid value, please use a number")

# Gets a free position based on a given password length and a list of taken positions
def get_position(password_length, positions=False):
    position = randint(0, password_length - 1)
    while positions and position in positions:
        position = randint(0, password_length - 1)
    return position

# Gets a number of random different positions based on a a password length and a number of iterations
def get_positions(length, iterations):
    positions = []
    for iteration in range(iterations):
        position = get_position(length, positions)
        positions.append(position)
    return positions

# Gets a position-value map based on a given password length and list of values
def get_position_map(length, args):
    positions = get_positions(length, len(args))
    position_map = {}
    for i in range(len(positions)):
        position_map[positions[i]] = args[i]
    return position_map

# Returns a random password based on a given length
def randomize(length):
    password = []
    for i in range(length):
        character = get_value(config.characters)
        password.append(character)
    return password

# Sets random values in random positions in a given password
def normalize(password, position_map):
    for position in position_map:
        password[position] = position_map[position]

# Outpus the password
def output(password):
    output = "".join(password)
    #print ("The following password is on your clipboard, use CTRL + V to paste it anywhere you want:")
    print(password)
    print(output)
    #addToClipBoard(output)

# Password to clipboard
def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)

# Generates the password
def generate():
    # Random value per list
    values = get_values(config.groups)
    
    # Password length
    password_length = get_length()

    # Password randomized
    password = randomize(password_length)

    # Positions
    position_map = get_position_map(password_length, values)

    # Password normalized
    normalize(password, position_map)

    # Password output
    output(password)

if __name__ == "__main__": generate()
