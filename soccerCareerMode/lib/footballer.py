class Footballer:
    def __init__(self, firstName, surname, age, ovr, pot, skills, weakFoot, club, league, nationality, price, wage, position, finishing, vision, defending):
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
        self.finishing = finishing
        self.vision = vision
        self.defending = defending

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
            self.defending = 45
            self.vision = 33
            self.finishing = 20
        elif self.position == 'Midfielder':
            self.defending = 30
            self.vision = 38
            self.finishing = 30
        elif self.position == 'Attacker':
            self.defending = 20
            self.vision = 33
            self.finishing = 45
        