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
            
        valid_positions = ['Defender', 'Midfielder', 'Attacker']
        # Get position from the user
        self.position = get_valid_input('What will your character\'s position be? (Defender, Midfielder, or Attacker) ', valid_positions)
    
teams = ['Bohemians', 'Dundalk', 'Drogheda United', 'Waterford', 'Sligo Rovers', 'Shamrock Rovers', 'St Patricks Athletic', 'Galway United', 'Shelbourne' ]

        
def trainingDay():
    delay_print("Training Day")
    if player.age < 26:
        ovrIncrease = random.uniform(0.25, 1.25)
    elif 31>player.age>26:
        ovrIncrease = random.uniform(0.0, 1.0)
    else:
        ovrIncrease = random.uniform(0.0, 0.2)
    player.ovr += ovrIncrease
    delay_print(f"Your new overall level is now {player.ovr:.0f}")
    
def matchday():
    delay_print("Match day\n")
    opposition = random.choice(teams)
    print(f"Derry City v {opposition}")
    home = random.randint(0,4)
    away = random.randint(0,4)
    if away == 0:
        cleansheet = True
    else:
        cleansheet = False
    if player.position == 'Defender' and player.ovr < 55:
        #goals = random.choice([0, 0, 0, 0, 0, 0, 1, 1, 2, 3])
        goals = min(random.randint(0, home), random.randint(0, home), random.randint(0, home), random.randint(0, home))
        assists = min(random.randint(0, home-goals), random.randint(0, home-goals), random.randint(0, home-goals))
        if goals > 0:      
            delay_print(f"You scored {str(goals)}\n")
        if assists > 0:
            delay_print(f"You had {str(assists)} assist(s)\n")
        if cleansheet == True:
            delay_print(f"You kept a cleansheet")
        else:
            pass
        delay_print(f"Your team scored {str(home)}\n")
        delay_print(f"{opposition} scored {str(away)}\n")
        if home > away:
            delay_print("You won\n")
            player.ovr += 0.2
            delay_print(f"Your overall is {player.ovr:.0f}\n")
        elif home < away:
            delay_print("You lost\n")
        elif home == away:
            delay_print("You drew\n")
    elif player.position == 'Attacker' and player.ovr < 55:
        #goals = random.randint(0,home)
        goals = min(random.randint(0, home), random.randint(0, home))
        #assists = random.randint(0,home-goals)
        assists = min(random.randint(0, home-goals), random.randint(0, home-goals), random.randint(0, home-goals))
        if goals > 0:      
            delay_print(f"You scored {str(goals)}\n")
        if assists > 0:
            delay_print(f"You had {str(assists)} assist(s)\n")
        delay_print(f"Your team scored {str(home)}\n")
        delay_print(f"{opposition} scored {str(away)}\n")
        if home > away:
            delay_print("You won\n")
            player.ovr += 0.2
            delay_print(f"Your overall is {player.ovr:.0f}\n")
        elif home < away:
            delay_print("You lost\n")
        elif home == away:
            delay_print("You drew\n")
    elif player.position == 'Midfielder' and player.ovr < 55:
        #goals = random.randint(0,home)
        goals = min(random.randint(0, home), random.randint(0, home), random.randint(0, home))
        #assists = random.randint(0,home-goals)
        assists = min(random.randint(0, home-goals), random.randint(0, home-goals))
        if goals > 0:      
            delay_print(f"You scored {str(goals)}\n")
        if assists > 0:
            delay_print(f"You had {str(assists)} assist(s)\n")
        delay_print(f"Your team scored {str(home)}\n")
        delay_print(f"{opposition} scored {str(away)}\n")
        if home > away:
            delay_print("You won\n")
            player.ovr += 0.2
            delay_print(f"Your overall is {player.ovr:.0f}\n")
        elif home < away:
            delay_print("You lost\n")
        elif home == away:
            delay_print("You drew\n")

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
        elif printSpeed == 'dev':
            text_delay = 0.001
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
    player = Footballer(firstName='', surname='', age='', ovr=40, pot=95, skills=0, weakFoot=0, club="Derry City", league="Irish Premier Devision", nationality='', price=50000, wage=350, position='')
    player.player_setup()
    print("\nPlayer setup complete. Here is your player information:")
    print(f"Name: {player.firstName} {player.surname}")
    print(f"Age: {player.age}")
    print(f"Nationality: {player.nationality}")
    print(f"Position: {player.position}")
    print(f"Club: {player.club}")
    print(f"League: {player.league}")
    time.sleep(3)
    
    trainingDay()
    time.sleep(1)
    matchday()
    time.sleep(1)
    trainingDay()
    time.sleep(1)
    matchday()
    time.sleep(1)
    trainingDay()
    time.sleep(1)
    matchday()
    time.sleep(1)
    trainingDay()
    time.sleep(1)
    matchday()
    time.sleep(1)
    trainingDay()
    time.sleep(1)
    matchday()
    time.sleep(1)
    trainingDay()
    time.sleep(1)
    matchday()
    time.sleep(1)
