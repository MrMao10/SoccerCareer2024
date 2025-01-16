class club:
    def __init__(self, name, ovrRating, defRating, attRating, midRating, established, gf, ga, gd, leaguePosition, points, budget, country, league, wins, draws, losses, cleansheets):
        self.name = name
        self.ovrRating = ovrRating
        self.defRating = defRating
        self.attRating = attRating
        self.midRating = midRating
        self.established = established
        self.gf = gf
        self.ga = ga
        self.gd = gd
        self.leaguePosition = leaguePosition
        self.points = points
        self.budget = budget
        self.country = country
        self.league = league
        self.wins = wins
        self.draws = draws
        self.losses = losses
        self.cleansheets = cleansheets

clubs = []

clubs.append(club('Bohemians', 60, 59, 59, 60, 1890, '', '', '', '', '', 42870, 'Ireland', 'Irish Premier Division', '', '', '', ''))
clubs.append(club('Dundalk', 58, 58, 60, 58, 1903, '', '', '', '', '', 42870, 'Ireland', 'Irish Premier Division', '', '', '', ''))
clubs.append(club('Drogheda United', 57, 57, 58, 56, 1919, '', '', '', '', '', 8570, 'Ireland', 'Irish Premier Division', '', '', '', ''))
clubs.append(club('UCD', 55, 55, 54, 54, 1895, '', '', '', '', '', 4290, 'Ireland', 'Irish Premier Division', '', '', '', ''))
clubs.append(club('Sligo Rovers', 59, 59, 57, 58, 1928, '', '', '', '', '', 42870, 'Ireland', 'Irish Premier Division', '', '', '', ''))
clubs.append(club('Shamrock Rovers', 63, 63, 64, 62, 1899, '', '', '', '', '', 60020, 'Ireland', 'Irish Premier Division', '', '', '', ''))
clubs.append(club('St Patricks Athletic', 62, 61, 62, 63, 1929, '', '', '', '', '', 42870, 'Ireland', 'Irish Premier Division', '', '', '', ''))
clubs.append(club('Galway United', 56, 56, 58, 56, 1984, '', '', '', '', '', 0, 'Ireland', 'Irish Premier Division', '', '', '', ''))
clubs.append(club('Shelbourne', 60, 61, 61, 59, 1895, '', '', '', '', '', 21440, 'Ireland', 'Irish Premier Division', '', '', '', ''))
clubs.append(club('Derry City', 61, 60, 64, 62, 1928, '', '', '', '', '', 100000, 'Ireland', 'Irish Premier Division', '', '', '', ''))

def display_league_table():
    pass    
