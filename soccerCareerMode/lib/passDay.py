import datetime
import json
from lib.leagueTable import clubs
import sys

startDate = datetime.datetime(2024, 2, 1)

def advance(player):
    global startDate
    print("\nDate:", startDate.strftime("%d %m %y"))
    startDate += datetime.timedelta(days=1)
    print("\n   OPTIONS     \n")
    advanceMenu = input('ADVANCE    QUIT \nSTATS    STANDINGS\n').lower()
    if advanceMenu == 'advance':
        pass
    elif advanceMenu == 'quit':
        while True:
            askSave = input('Do you want to quit without saving, or save? ').capitalize()
            if askSave == 'Quit without saving':
                sys.exit()
            elif askSave == 'Save':
                f = open("save.txt", "wt")
                myDict = {
                    "startDate": str(startDate),
                    "playerFirstName": player.firstName,
                    "playerSurname": player.surname,
                    "playerAge": player.age,
                    "playerOvr": player.ovr,
                    "playerSkills": player.skills,
                    "playerWeakFoot": player.weakFoot,
                    "playerNationality": player.nationality,
                    "playerPrice": player.price,
                    "playerWage": player.wage,
                    "playerPosition": player.position,
                    "playerGoals": player.goalCount,
                    "playerAssists": player.assistCount,
                    "playerCleansheets": player.cleansheetCount,
                    "playerAppearances": player.appearances,
                    "playerPace": player.pace,
                    "playerFinishing": player.finishing,
                    "playerAttPosition": player.attPosition,
                    "playerShotPower": player.shotPower,
                    "playerLongShots": player.longShots,
                    "playerPenalties": player.penalties,
                    "playerVolleys": player.volleys,
                    "playerVision": player.vision,
                    "playerCrossing": player.crossing,
                    "playerFkAcc": player.fkAcc,
                    "playerLongPass": player.longPass,
                    "playerShortPass": player.shortPass,
                    "playerCurve": player.curve,
                    "playerAgility": player.agility,
                    "playerBalance": player.balance,
                    "playerReactions": player.reactions,
                    "playerComposure": player.composure,
                    "playerBallControl": player.ballControl,
                    "playerDribbling": player.dribbling,
                    "playerInterceptions": player.interceptions,
                    "playerHeadingAcc": player.headingAcc,
                    "playerDefAwareness": player.defAwareness,
                    "playerStandTackle": player.standTackle,
                    "playerSlideTackle": player.slideTackle,
                    "playerJumping": player.jumping,
                    "playerStamina": player.stamina,
                    "playerStrength": player.strength,
                    "playerAggression": player.aggression,
                    "derryWins": clubs[9].wins,
                    "derryLosses": clubs[9].losses,
                    "derryDraws": clubs[9].draws,
                    "derryGA": clubs[9].ga,
                    "derryGF": clubs[9].gf,
                    "derryGD": clubs[9].gd,
                    "derryCleasnsheets": clubs[9].cleansheets,
                    "derryLeaguePosition": clubs[9].leaguePosition,
                    "derryPoints": clubs[9].points
                        }
                f.write(json.dumps(myDict))
                #f.write(startDate, player, clubs[9].wins, clubs[9].losses, clubs[9].draws, clubs[9].ga, clubs[9].gf, clubs[9].gd, clubs[9].cleansheets, clubs[9].leaguePosition, clubs[9].points)
                sys.exit()
            else:
                print("Not a valid option. To save, enter 'save', to quit without saving, enter 'quit without saving'.")
    elif advanceMenu == 'standings':
        #display league table
        print("This feature will be available soon.")
        input('Press Enter To Continue...')
    elif advanceMenu == 'stats':
        while True:
            stats = input(f'\n{player.firstName} {player.surname} STATS     TEAM STATS\n').lower()
            if stats == 'player stats':
                #print player goals, assists, cleansheets, appearances
                print(f"\nTotal Goals: {player.goalCount}\nTotal Assists: {player.assistCount}\nTotal Appearances: {player.appearances}\nTotal Cleansheets: {player.cleansheetCount}")
                input('Press Enter To Continue...')
                break
            elif stats == 'team stats':
                print(f"\n{clubs[9].name} STATS")
                print(f"Club  Overall Rating: {clubs[9].ovrRating}\nClub Attack Rating: {clubs[9].attRating}\nClub Midfield Rating: {clubs[9].midRating}\nClub Defence Rating: {clubs[9].defRating}\nClub League Position: {clubs[9].leaguePosition}\nPoints: {clubs[9].points}\nWins: {clubs[9].wins}\nDraws: {clubs[9].draws}\nLosses: {clubs[9].losses}\nGoal Difference: {clubs[9].gd}\nTotal Goals Scored: {clubs[9].gf}\nTotal Goals Conceded: {clubs[9].ga}")
                input('Press Enter To Continue...')
                break
            else:
                print(f"Invalid option. To view {player.firstName} {player.surname}'s stats, enter 'player stats', to view team stats, enter 'team stats'.")
