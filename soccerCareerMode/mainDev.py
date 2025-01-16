import time
import sys
import random
import datetime
from lib.passDay import advance, startDate
from lib.leagueTable import club

# Delay Printing Function
def delay_print(s, delay=0.05):
    print()
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)

# Footballer Class Definition
class Footballer:
    def __init__(self, firstName, surname, age, ovr, pot, skills, weakFoot, club, league, nationality, price, wage, position, goalCount, assistCount, cleansheetCount, appearances, pace, finishing, attPosition, shotPower, longShots, penalties, volleys, vision, crossing, fkAcc, longPass, shortPass, curve, agility, balance, reactions, composure, ballControl, dribbling, interceptions, headingAcc, defAwareness, standTackle, slideTackle, jumping, stamina, strength, aggression):
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
        self.goalCount = goalCount
        self.assistCount = assistCount
        self.cleansheetCount = cleansheetCount
        self.appearances = appearances
        self.pace = pace
        self.finishing = finishing
        self.attPosition = attPosition
        self.shotPower = shotPower
        self.longShots = longShots
        self.penalties = penalties
        self.volleys = volleys
        self.vision = vision
        self.crossing = crossing
        self.fkAcc = fkAcc
        self.longPass = longPass
        self.shortPass = shortPass
        self.curve = curve
        self.agility = agility
        self.balance = balance
        self.reactions = reactions
        self.composure = composure
        self.ballControl = ballControl
        self.dribbling = dribbling
        self.interceptions = interceptions
        self.headingAcc = headingAcc
        self.defAwareness = defAwareness
        self.standTackle = standTackle
        self.slideTackle = slideTackle
        self.jumping = jumping
        self.stamina = stamina
        self.strength = strength
        self.aggression = aggression

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
        if self.position == 'Defender':
            self.pace = 40
            self.finishing = 20
            self.attPosition = 20
            self.shotPower = 27
            self.longShots = 20
            self.penalties = 25
            self.volleys = 20
            self.vision = 30
            self.crossing = 30
            self.fkAcc = 25
            self.longPass =  30
            self.shortPass = 35
            self.curve = 30
            self.agility = 30
            self.balance = 30
            self.reactions = 40
            self.composure = 28
            self.ballControl = 30
            self.dribbling = 27
            self.interceptions = 43
            self.headingAcc = 47
            self.defAwareness = 47
            self.standTackle = 47
            self.slideTackle = 47
            self.jumping = 40
            self.stamina = 40
            self.strength = 45
            self.aggression = 45
        elif self.position == 'Midfielder':
            self.defending = 30
            self.vision = 38
            self.finishing = 30
        elif self.position == 'Attacker':
            self.defending = 20
            self.vision = 33
            self.finishing = 45
        
    
teams = ['Bohemians', 'Dundalk', 'Drogheda United', 'UCD', 'Sligo Rovers', 'Shamrock Rovers', 'St Patricks Athletic', 'Cork City', 'Shelbourne' ]
Bohemians = club('Bohemians', 60, 59, 59, 60, 1890, '', '', '', '', '', 42870, 'Ireland', 'Irish Premier Division', '', '', '', '')
Dundalk = club('Dundalk', 58, 58, 60, 58, 1903, '', '', '', '', '', 42870, 'Ireland', 'Irish Premier Division', '', '', '', '')
Drogheda_United = club('Drogheda United', 57, 57, 58, 56, 1919, '', '', '', '', '', 8570, 'Ireland', 'Irish Premier Division', '', '', '', '')
UCDfc = club('UCD', 55, 55, 54, 54, 1895, '', '', '', '', '', 4290, 'Ireland', 'Irish Premier Division', '', '', '', '')
Sligo_Rovers = club('Sligo Rovers', 59, 59, 57, 58, 1928, '', '', '', '', '', 42870, 'Ireland', 'Irish Premier Division', '', '', '', '')
Shamrock_Rovers = club('Shamrock Rovers', 63, 63, 64, 62, 1899, '', '', '', '', '', 60020, 'Ireland', 'Irish Premier Division', '', '', '', '')
St_Patricks_Athletic = club('St Patricks Athletic', 62, 61, 62, 63, 1929, '', '', '', '', '', 42870, 'Ireland', 'Irish Premier Division', '', '', '', '')
Cork_City = club('Galway United', 56, 56, 58, 56, 1984, '', '', '', '', '', 0, 'Ireland', 'Irish Premier Division', '', '', '', '')
Shelbourne = club('Shelbourne', 60, 61, 61, 59, 1895, '', '', '', '', '', 21440, 'Ireland', 'Irish Premier Division', '', '', '', '')
Derry_City = club('Derry City', 61, 60, 64, 62, 1928, '', '', '', '', '', 100000, 'Ireland', 'Irish Premier Divsion', 0, 0, 0, 0)
    
def trainingDay():
    delay_print("Training Day")
    if player.ovr >= player.pot:
        pass
    elif player.age < 26:
        ovrIncrease = random.uniform(0.2, 0.8)
    elif 31 > player.age > 26:
        ovrIncrease = random.uniform(0.0, 0.075)
    elif player.age > 34:
        ovrIncrease = random.uniform(-0.2, 0)
    else:
        ovrIncrease = random.uniform(0.0, 0.05)
    player.ovr += ovrIncrease
    delay_print(f"Your overall level is now {player.ovr:.0f}\n")
    
    
def matchday():
    delay_print("Match day\n")
    opposition = random.choice(teams)
    print(f"Derry City v {opposition}")
    home = min(random.randint(0,4), random.randint(0,4))
    away = min(random.randint(0,4), random.randint(0,4))
    if away == 0:
        cleansheet = True
    else:
        cleansheet = False
    if player.position == 'Defender' and player.ovr < 55:
        delay_print(f"{player.club}: {str(home)}\n")
        delay_print(f"{opposition}: {str(away)}\n")
        goals = min(random.randint(0, home), random.randint(0, home), random.randint(0, home), random.randint(0, home))
        player.goalCount += goals
        assists = min(random.randint(0, home-goals), random.randint(0, home-goals), random.randint(0, home-goals))
        player.assistCount += assists
        if goals > 0:      
            delay_print(f"You scored {str(goals)}\n")
            player.ovr += 0.8
        if assists > 0:
            delay_print(f"You had {str(assists)} assist(s)\n")
            player.ovr += 0.07
        if cleansheet == True:
            delay_print(f"You kept a cleansheet\n")
            player.ovr += 0.05
            player.cleansheetCount += 1
        else:
            pass
        if home > away:
            delay_print("You won\n")
            player.ovr += 0.1
            delay_print(f"Your overall is {player.ovr:.0f}\n")
        elif home < away:
            delay_print("You lost\n")
            player.ovr += 0.01
            delay_print(f"Your overall is {player.ovr:.0f}\n")
        elif home == away:
            delay_print("You drew\n")
            player.ovr += 0.05
            delay_print(f"Your overall is {player.ovr:.0f}\n")
    elif player.position == 'Attacker' and player.ovr < 55:
        delay_print(f"{player.club}: {str(home)}\n")
        delay_print(f"{opposition}: {str(away)}\n")
        goals = min(random.randint(0, home), random.randint(0, home))
        player.goalCount += goals
        assists = min(random.randint(0, home-goals), random.randint(0, home-goals), random.randint(0, home-goals))
        player.assistCount += assists
        if goals > 0:      
            delay_print(f"You scored {str(goals)}\n")
            player.ovr += 0.07
        if assists > 0:
            delay_print(f"You had {str(assists)} assist(s)\n")
            player.ovr += 0.08
        if home > away:
            delay_print("You won\n")
            player.ovr += 0.1
            delay_print(f"Your overall is {player.ovr:.0f}\n")
        elif home < away:
            delay_print("You lost\n")
            player.ovr += 0.01
            delay_print(f"Your overall is {player.ovr:.0f}\n")
        elif home == away:
            delay_print("You drew\n")
            player.ovr += 0.05
            delay_print(f"Your overall is {player.ovr:.0f}\n")
    elif player.position == 'Midfielder' and player.ovr < 55:
        delay_print(f"{player.club}: {str(home)}\n")
        delay_print(f"{opposition}: {str(away)}\n")
        goals = min(random.randint(0, home), random.randint(0, home), random.randint(0, home))
        player.goalCount += goals
        assists = min(random.randint(0, home-goals), random.randint(0, home-goals))
        player.assistCount += assists
        if goals > 0:      
            delay_print(f"You scored {str(goals)}\n")
            player.ovr += 0.1
        if assists > 0:
            delay_print(f"You had {str(assists)} assist(s)\n")
            player.ovr += 0.05
        if home > away:
            delay_print("You won\n")
            player.ovr += 0.1
            delay_print(f"Your overall is {player.ovr:.0f}\n")
        elif home < away:
            delay_print("You lost\n")
            player.ovr += 0.01
            delay_print(f"Your overall is {player.ovr:.0f}\n")
        elif home == away:
            delay_print("You drew\n")
            player.ovr += 0.05
            delay_print(f"Your overall is {player.ovr:.0f}\n")

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
    player = Footballer(firstName='', surname='', age='', ovr=40, pot=95, skills=0, weakFoot=0, club="Derry City", league="Irish Premier Devision", nationality='', price=50000, wage=350, position='', finishing='', vision='', defending='', goalCount=0, assistCount=0, cleansheetCount=0, appearances=0)
    player.player_setup()
    print("\nPlayer setup complete. Here is your player information:")
    print(f"Name: {player.firstName} {player.surname}")
    print(f"Age: {player.age}")
    print(f"Nationality: {player.nationality}")
    print(f"Position: {player.position}")
    print(f"Club: {player.club}")
    print(f"League: {player.league}")
    print(f"Defending Attribute: {player.defending}")
    print(f"Vision Attribute: {player.vision}")
    print(f"Finishing attribute: {player.finishing}\n")
    time.sleep(3)
    
    time.sleep(1)
    advance(player)
    time.sleep(1)
    trainingDay()
    time.sleep(1)
    advance(player)
    time.sleep(1)
    matchday()
    time.sleep(1)
    advance(player)
    time.sleep(1)
    trainingDay()
    time.sleep(1)
    advance(player)
    time.sleep(1)
    matchday()
    time.sleep(1)
    advance(player)
    time.sleep(1)
    trainingDay()
    time.sleep(1)
    advance(player)
    time.sleep(1)
    matchday()
    time.sleep(1)
    advance(player)
    time.sleep(1)
    trainingDay()
    time.sleep(1)
    advance(player)
    time.sleep(1)
    matchday()
    time.sleep(1)
    advance(player)
    time.sleep(1)
    trainingDay()
    time.sleep(1)
    advance(player)
    time.sleep(1)
    matchday()
    time.sleep(1)
    advance(player)
    time.sleep(1)
    trainingDay()
    time.sleep(1)
    advance(player)
    time.sleep(1)
    matchday()
    time.sleep(1)
