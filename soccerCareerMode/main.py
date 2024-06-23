import time
import sys
import random

# Delay Printing Function
def delay_print(s, delay=0.05):
    print()
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)

# Footballer Class Definition
class Footballer:
    def __init__(self, firstName, surname, age, ovr, pot, skills, weakFoot, club, league, nationality, price, wage, position):
        self.firstName = firstName
        self.surname = surname
        self.age = age
        self.ovr = ovr
        self.pot = pot
        self.skills = skills
        self.weakFoot = weakFoot
        self.club = club
        self.league = league
        self.nationality = nationality
        self.price = price
        self.wage = wage
        self.position = position

    def player_setup(self):
        self.firstName = input('\nWhat will your character\'s first name be? ')
        self.surname = input('What will your character\'s surname be? ')
        while True:
            try:
                age = int(input('What will your character\'s age be? (16-36) '))
                if 16 <= age <= 36:
                    self.age = age
                    break
                else:
                    print("Age must be between 16 and 36.")
            except ValueError:
                print("Please enter a valid age.")
        self.nationality = input('What will your character\'s nationality be? ')
        
        # Function to get valid input from the user
        def get_valid_input(prompt, options):
            while True:
                user_input = input(prompt).capitalize()
                if user_input in options:
                    return user_input
                else:
                    print(f"Invalid input. Please enter one of the following: {', '.join(options)}")

        # Define valid positions
        valid_positions = ['Defender', 'Midfielder', 'Attacker']
        # Get position from the user
        self.position = get_valid_input('What will your character\'s position be? (Defender, Midfielder, or Attacker) ', valid_positions)
        
def trainingDay():
    delay_print("Training Day")
    ovrIncrease = random.uniform(0.0, 1.0)
    player.ovr += ovrIncrease
    delay_print("Your new overall level is now " + str(player.ovr) + str(ovrIncrease))
    

if __name__ == "__main__":
    # Settings
    print("SETTINGS:")
    setting = input('\nTEXT SPEED\nBACK\n').lower()
    if setting == 'text speed':
        printSpeed = input('Slow, medium or fast text speed?\n').lower()
        if printSpeed == 'slow':
            text_delay = 0.075
        elif printSpeed == 'medium':
            text_delay = 0.03
        elif printSpeed == 'fast':
            text_delay = 0.008
        else:
            text_delay = 0.05  # Default medium speed
    else:
        text_delay = 0.04  # Default back option

    # Introduction Messages
    delay_print("Welcome to Soccer Career 2024.", text_delay)
    delay_print("In this text-based game, you will play as a football player in the Irish first league. "
                "This is a developing game so apologies for any bugs. Please report these bugs on my github MrMao10 "
                "so I can fix them. I would also appreciate any recommendations to improve the game. Thanks!", text_delay)

    # Player Setup
    player = Footballer(firstName='', surname='', age=0, ovr=40, pot=95, skills=0, weakFoot=0, club='', league='', nationality='', price=50000, wage=350, position='')
    player.player_setup()
    print("\nPlayer setup complete. Here is your player information:")
    print(f"Name: {player.firstName} {player.surname}")
    print(f"Age: {player.age}")
    print(f"Nationality: {player.nationality}")
    print(f"Position: {player.position}")
