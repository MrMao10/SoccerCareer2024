import time
import sys
import random
import datetime
from lib.passDay import advance, startDate
from lib.leagueTable import clubs

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
        
    def __repr__(self):
        return self.firstName

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
        nationalities = ['Afghan', 'Albanian', 'Algerian', 'American', 'Andorran', 'Angolan', 'Antiguans', 'Argentinean', 'Armenian', 'Australian', 'Austrian', 'Azerbaijani', 'Bahamian', 'Bahraini', 'Bangladeshi', 'Barbadian', 'Barbudans', 'Batswana', 'Belarusian', 'Belgian', 'Belizean', 'Beninese', 'Bhutanese', 'Bolivian', 'Bosnian', 'Brazilian', 'British', 'Bruneian', 'Bulgarian', 'Burkinabe', 'Burmese', 'Burundian', 'Cambodian', 'Cameroonian', 'Canadian', 'Cape Verdean', 'Central African', 'Chadian', 'Chilean', 'Chinese', 'Colombian', 'Comoran',  'Congolese', 'Costa Rican', 'Croatian', 'Cuban', 'Cypriot', 'Czech', 'Danish', 'Djibouti', 'Dominican', 'Dutch', 'Dutchman', 'Dutchwoman', 'East Timorese', 'Ecuadorean', 'Egyptian', 'Emirian', 'Equatorial Guinean', 'Eritrean', 'Estonian', 'Ethiopian', 'Fijian', 'Filipino', 'Finnish', 'French', 'Gabonese', 'Gambian', 'Georgian', 'German', 'Ghanaian', 'Greek', 'Grenadian', 'Guatemalan', 'Guinea-Bissauan', 'Guinean', 'Guyanese', 'Haitian', 'Herzegovinian', 'Honduran', 'Hungarian', 'I-Kiribati', 'Icelander', 'Indian', 'Indonesian', 'Iranian', 'Iraqi', 'Irish', 'Italian', 'Ivorian', 'Jamaican', 'Japanese', 'Jordanian', 'Kazakhstani', 'Kenyan', 'Kittian and Nevisian', 'Kuwaiti', 'Kyrgyz', 'Laotian', 'Latvian', 'Lebanese', 'Liberian', 'Libyan', 'Liechtensteiner', 'Lithuanian', 'Luxembourger', 'Macedonian', 'Malagasy', 'Malawian', 'Malaysian', 'Maldivan', 'Malian', 'Maltese', 'Marshallese', 'Mauritanian', 'Mauritian', 'Mexican', 'Micronesian', 'Moldovan', 'Monacan', 'Mongolian', 'Moroccan', 'Mosotho', 'Motswana', 'Mozambican', 'Namibian', 'Nauruan', 'Nepalese', 'Netherlander', 'New Zealander', 'Ni-Vanuatu', 'Nicaraguan', 'Nigerian', 'Nigerien', 'North Korean', 'Norwegian', 'Omani', 'Pakistani', 'Palauan', 'Palestinian', 'Panamanian', 'Papua New Guinean', 'Paraguayan', 'Peruvian', 'Polish', 'Portuguese', 'Qatari', 'Romanian', 'Russian', 'Rwandan', 'Saint Lucian', 'Salvadoran', 'Samoan', 'San Marinese', 'Sao Tomean', 'Saudi', 'Scottish', 'Senegalese', 'Serbian', 'Seychellois', 'Sierra Leonean', 'Singaporean', 'Slovakian', 'Slovenian', 'Solomon Islander', 'Somali', 'South African', 'South Korean', 'Spanish', 'Sri Lankan', 'Sudanese', 'Surinamer', 'Swazi', 'Swedish', 'Swiss', 'Syrian', 'Taiwanese', 'Tajik', 'Tanzanian', 'Thai', 'Togolese', 'Tongan', 'Trinidadian or Tobagonian', 'Tunisian', 'Turkish', 'Tuvaluan', 'Ugandan', 'Ukrainian', 'Uruguayan', 'Uzbekistani', 'Venezuelan', 'Vietnamese', 'Welsh', 'Yemenite', 'Zambian', 'Zimbabwean']
        while True:    
            nationality = str(input('What will your character\'s nationality be? ').capitalize())
            if nationality in nationalities:
                self.nationality = nationality
                break
            else:
                print("Not in the database of nationalities. Please try again.")

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
            self.pace = 40
            self.finishing = 25
            self.attPosition = 33
            self.shotPower = 28
            self.longShots = 35
            self.penalties = 30
            self.volleys = 28
            self.vision = 48
            self.crossing = 28
            self.fkAcc = 35
            self.longPass =  45
            self.shortPass = 50
            self.curve = 38
            self.agility = 33
            self.balance = 33
            self.reactions = 43
            self.composure = 33
            self.ballControl = 47
            self.dribbling = 43
            self.interceptions = 35
            self.headingAcc = 25
            self.defAwareness = 35
            self.standTackle = 37
            self.slideTackle = 30
            self.jumping = 28
            self.stamina = 40
            self.strength = 28
            self.aggression = 38
        elif self.position == 'Attacker':
            self.pace = 35
            self.finishing = 50
            self.attPosition = 48
            self.shotPower = 47
            self.longShots = 38
            self.penalties = 40
            self.volleys = 35
            self.vision = 34
            self.crossing = 30
            self.fkAcc = 33
            self.longPass =  32
            self.shortPass = 34
            self.curve = 33
            self.agility = 33
            self.balance = 33
            self.reactions = 43
            self.composure = 33
            self.ballControl = 45
            self.dribbling = 42
            self.interceptions = 25
            self.headingAcc = 47
            self.defAwareness = 18
            self.standTackle = 21
            self.slideTackle = 20
            self.jumping = 42
            self.stamina = 37
            self.strength = 42
            self.aggression = 35
        
    
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
    oldOvr = player.ovr - ovrIncrease
    delay_print(f"Old rating: {oldOvr:.0f}\nNew rating: {player.ovr:.0f}\n")

    
def matchday():
    delay_print("Match day\n")
    if player.ovr <= clubs[9].ovrRating:
        playChance = random.randint(0, 1)
    elif player.ovr > clubs[9].ovrRating:
        playChance = max(random.randint(0, 1), random.randint(0, 1))
    if playChance == 1:
        player.appearances += 1
        while True:
            opposition = random.choice(clubs)
            if opposition == clubs[0]:
                print(f"{repr(clubs[9])} v {repr(clubs[0])}")
                break
            elif opposition == clubs[1]:
                print(f"{repr(clubs[9])} v {repr(clubs[1])}")
                break
            elif opposition == clubs[2]:
                print(f"{repr(clubs[9])} v {repr(clubs[2])}")
                break
            elif opposition == clubs[3]:
                print(f"{repr(clubs[9])} v {repr(clubs[3])}")
                break
            elif opposition == clubs[4]:
                print(f"{repr(clubs[9])} v {repr(clubs[4])}")
                break
            elif opposition == clubs[5]:
                print(f"{repr(clubs[9])} v {repr(clubs[5])}")
                break
            elif opposition == clubs[6]:
                print(f"{repr(clubs[9])} v {repr(clubs[6])}")
                break
            elif opposition == clubs[7]:
                print(f"{repr(clubs[9])} v {repr(clubs[7])}")
                break
            elif opposition == clubs[8]:
                print(f"{repr(clubs[9])} v {repr(clubs[8])}")
                break
            else:
                print()
        home = min(random.randint(0,4), random.randint(0,4))
        away = min(random.randint(0,4), random.randint(0,4))
        clubs[9].gf += home
        clubs[9].ga += away
        clubs[9].gd += (home - away)
        opposition.gf += away
        opposition.ga += home
        opposition.gd += (away - home)
        if home > away:
            clubs[9].wins += 1
            clubs[9].points += 3
        elif home == away:
            clubs[9].draws += 1
            clubs[9].points += 1
        elif home < away:
            clubs[9].losses += 1
        if away == 0:
            cleansheet = True
            clubs[9].cleansheets += 1
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
    elif playChance == 0:
        print("You where not picked for this match.")
        while True:
            opposition = random.choice(clubs)
            if opposition == clubs[0]:
                print(f"{repr(player.club)} v {repr(clubs[0])}")
                break
            elif opposition == clubs[1]:
                print(f"{repr(player.club)} v {repr(clubs[1])}")
                break
            elif opposition == clubs[2]:
                print(f"{repr(player.club)} v {repr(clubs[2])}")
                break
            elif opposition == clubs[3]:
                print(f"{repr(player.club)} v {repr(clubs[3])}")
                break
            elif opposition == clubs[4]:
                print(f"{repr(player.club)} v {repr(clubs[4])}")
                break
            elif opposition == clubs[5]:
                print(f"{repr(player.club)} v {repr(clubs[5])}")
                break
            elif opposition == clubs[6]:
                print(f"{repr(player.club)} v {repr(clubs[6])}")
                break
            elif opposition == clubs[7]:
                print(f"{repr(player.club)} v {repr(clubs[7])}")
                break
            elif opposition == clubs[8]:
                print(f"{repr(player.club)} v {repr(clubs[8])}")
                break
            else:
                print()
        home = min(random.randint(0,4), random.randint(0,4))
        away = min(random.randint(0,4), random.randint(0,4))
        clubs[9].gf += home
        clubs[9].ga += away
        clubs[9].gd += (home - away)
        opposition.gf += away
        opposition.ga += home
        opposition.gd += (away - home)
        if home > away:
            clubs[9].wins += 1
            clubs[9].points += 3
        elif home == away:
            clubs[9].draws += 1
            clubs[9].points += 1
        elif home < away:
            clubs[9].losses += 1
        if away == 0:
            cleansheet = True
            clubs[9].cleansheets += 1
        else:
            cleansheet = False
        delay_print(f"{repr(clubs[9])}: {str(home)}\n")
        delay_print(f"{opposition}: {str(away)}\n")
        pass

if __name__ == "__main__":
    print("SOCCER CAREER 2024")
    text_delay = 0.035
    while True:
        startMenu = input('\nPLAY\nLOAD\nSETTINGS\n').lower()
        if startMenu == 'settings':
            print("SETTINGS:")
            while True:
                setting = input('\nTEXT SPEED\nBACK\n').lower()
                if setting == 'text speed':
                    printSpeed = input('Slow, medium or fast text speed?\n').lower()
                    if printSpeed == 'slow':
                        text_delay = 0.075
                        break
                    elif printSpeed == 'medium':
                        text_delay = 0.03
                        break
                    elif printSpeed == 'fast':
                        text_delay = 0.008
                        break
                    elif printSpeed == 'dev':
                        text_delay = 0.001
                        break
                    else:
                        print()
                elif setting == 'back':
                    text_delay = 0.035
        elif startMenu == 'play':
            pass
            break
        elif startMenu == 'load':
            pass
        
    # Introduction Messages
    delay_print("Welcome to Soccer Career 2024.", text_delay)
    delay_print("In this text-based game, you will play as a football player in the Irish first league. "
                "This is a developing game so apologies for any bugs. Please report these bugs on my github MrMao10 "
                "so I can fix them. I would also appreciate any recommendations to improve the game. Thanks!", text_delay)

    # Player Setup
    player = Footballer(firstName='', surname='', age='', ovr=46, pot=95, skills=0, weakFoot=0, club="Derry City", league="Irish Premier Devision", nationality='', price=50000, wage=350, position='', pace='', finishing='', attPosition='', shotPower='', longShots='', penalties='', volleys='', vision='', crossing='', fkAcc='', longPass='', shortPass='', curve='', agility='', balance='', reactions='', composure='', ballControl='', dribbling='', interceptions='', headingAcc='', defAwareness='',standTackle='', slideTackle='', jumping='', stamina='', strength='', aggression='', goalCount=0, assistCount=0, cleansheetCount=0, appearances=0)
    player.player_setup()
    print("\nPlayer setup complete. Here is your player information:")
    print(f"Name: {player.firstName} {player.surname}")
    print(f"Age: {player.age}")
    print(f"Nationality: {player.nationality}")
    print(f"Position: {player.position}")
    print(f"Club: {player.club}")
    print(f"League: {player.league}")
    print(f"[bold]Defending Attributes:[/bold] \n    Defensive Awareness: {player.defAwareness} \n    Stand Tackles: {player.standTackle} \n    Slide Tackle: {player.slideTackle} \n    Heading Accuracy: {player.headingAcc}")
    time.sleep(2)
    print(f"[bold]Passing Attributes:[/bold] \n    Vision: {player.vision} \n    Crossing: {player.crossing} \n    fkAcc: {player.fkAcc} \n    Long Pass: {player.longPass} \n    Short Pass: {player.shortPass} \n    Curve: {player.curve}")
    time.sleep(2)
    print(f"[bold]Attacking attributes:[/bold]\n    Finishing: {player.finishing} \n    Attack Positioning: {player.attPosition} \n    Shot Power: {player.shotPower} \n    Long Shots: {player.longShots} \n    Penalties: {player.penalties} \n    Volleys: {player.volleys}")
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
