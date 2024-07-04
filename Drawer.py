import random

class Drawer:
    def __init__(self):
        self.names = []
        self.team_size = 0
        self.teams = []

    def set_names(self, names):
        self.add_names_to_array(names)
    
    def add_names_to_array(self, names):
        self.names = names.split(',')

    def set_teams_size(self, team_size):
        self.team_size = int(team_size)

    def create_normal_team(self):
        team = ()
        for _ in range(self.team_size):
            random.shuffle(self.names)
            name_drawn = self.names.pop()
            team += (name_drawn,)
        return team
    
    def create_anormal_team(self):
        return tuple(self.names)

    def create_teams(self):
        count_names = len(self.names)
        team_size = self.team_size
        while count_names > 0:
            new_team = ()
            if count_names >= team_size * 2:
                new_team = self.create_normal_team()
                count_names -= self.team_size
            else:
                while count_names > 0:
                    new_team = self.create_anormal_team()
                    count_names = 0
                    self.names = []
            self.teams.append(new_team)

    def show_teams(self):
        for team in self.teams:
            print(", ".join(team))