import random

class Drawer:
    def __init__(self):
        self.names = []
        self.team_size = 0
        self.teams = []

    def read_names(self, names):
        self.add_names_to_array(names)
    
    def add_names_to_array(self, names):
        self.names = names.split(',')

    def read_teams_size(self, team_size):
        self.team_size = int(team_size)

    def create_teams(self):
        count_names = len(self.names)
        team_size = self.team_size
        while count_names > 0:
            new_team = ()
            if count_names >= team_size * 2:
                for i in range (team_size):
                    random.shuffle(self.names)
                    name_drawn = self.names.pop()
                    new_team += (name_drawn,)
                    count_names -= 1
            else:
                while count_names > 0:
                    name_drawn = self.names.pop()
                    new_team += (name_drawn,)
                    count_names -= 1
            self.teams.append(new_team)

    def show_teams(self):
        for team in self.teams:
            print(", ".join(team))