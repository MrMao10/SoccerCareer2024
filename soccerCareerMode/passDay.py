import datetime
from lib.leagueTable import clubs

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
        stats = input(f'\n{player.firstName} {player.surname} STATS     TEAM STATS\n').lower()
        if stats == 'player stats':
            #print player goals, assists, cleansheets, appearances
            print(f"\n Total Goals: {player.goalCount}\nTotal Assists: {player.assistCount}\nTotal Appearances: {player.appearances}\nTotal Cleansheets: {player.cleansheetCount}")
        elif stats == 'team stats':
            print(f"\nTotal Team Goals: {clubs[9].gf}\nTeam Cleansheets: {clubs[9].cleansheets}")
        else:
            pass
