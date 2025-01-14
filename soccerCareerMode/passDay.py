import datetime
from lib.itest import Derry_City

startDate = datetime.datetime(2024, 2, 1)

def advance(player):
    global startDate
    print(startDate.strftime("%d %m %y"))
    startDate += datetime.timedelta(days=1)
    print("\n   OPTIONS     \n")
    advanceMenu = input('ADVANCE    QUIT \nSTATS    STANDINGS\n').lower()
    if advanceMenu == 'advance':
        pass
    elif advanceMenu == 'quit':
        quit
    elif advanceMenu == 'standings':
        pass #display league table
    elif advanceMenu == 'stats':
        stats = input(f'\n{player.name} STATS\n TEAM STATS').lower()
        if stats == 'player stats':
            #print player goals, assists, cleansheets, appearances
            pass
        elif stats == 'team stats':
            print(f"\nTotal Team Goals: {Derry_City.goals}\nTeam Cleansheets: {Derry_City.cleansheets}")
        else:
            pass