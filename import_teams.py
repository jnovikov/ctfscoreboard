from scoreboard import models

if __name__ == '__main__':
    with open("teams.txt") as team_file:
        teams = []
        team_names = team_file.readlines()
        for team_name in team_names:
            teams.append(models.Team.create(team_name.strip().encode()))
        models.commit()
