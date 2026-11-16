import random


# Dictionary to hold all teams and their stats
teams = {}


# Add a new team to the league

def add_team(name):
    name = name.strip()

    if name == "":
        print("Team name cannot be empty.")
        return

    if name in teams:
        print("This team already exists.")
        return

    teams[name] = {
        "played": 0,
        "wins": 0,
        "draws": 0,
        "losses": 0,
        "goals_for": 0,
        "goals_against": 0,
        "goal_difference": 0,
        "points": 0,
    }

    print(name, "added to the league.")


# Update one team's stats after a match

def update_team(team_name, goals_for, goals_against):
    team = teams[team_name]
    team["played"] += 1
    team["goals_for"] += goals_for
    team["goals_against"] += goals_against
    team["goal_difference"] = team["goals_for"] - team["goals_against"]

    if goals_for > goals_against:
        team["wins"] += 1
        team["points"] += 3
    elif goals_for < goals_against:
        team["losses"] += 1
    else:
        team["draws"] += 1
        team["points"] += 1


# Record a match result manually

def play_match(home_team, away_team, home_goals, away_goals):
    if home_team == away_team:
        print("A team cannot play itself.")
        return

    if home_team not in teams or away_team not in teams:
        print("Both teams must already exist in the league.")
        return

    if home_goals < 0 or away_goals < 0:
        print("Goals cannot be negative.")
        return

    update_team(home_team, home_goals, away_goals)
    update_team(away_team, away_goals, home_goals)
    print(home_team, home_goals, "-", away_goals, away_team)


# Create a random score for a match

def simulate_match(home_team, away_team):
    home_goals = random.randint(0, 5)
    away_goals = random.randint(0, 5)
    play_match(home_team, away_team, home_goals, away_goals)


# Sort teams by points, goal difference, and goals scored

def get_standings():
    standings = []

    for team_name in teams:
        standings.append(team_name)

    standings.sort(
        key=lambda name: (
            teams[name]["points"],
            teams[name]["goal_difference"],
            teams[name]["goals_for"],
        ),
        reverse=True,
    )

    return standings


# Display the league table

def show_standings():
    if len(teams) == 0:
        print("No teams have been added yet.")
        return

    print("\nTeam            P  W  D  L  GF  GA  GD  PTS")

    for position, team_name in enumerate(get_standings(), start=1):
        team = teams[team_name]
        print(
            f"{position}. {team_name:<15} {team['played']:>2} {team['wins']:>2} "
            f"{team['draws']:>2} {team['losses']:>2} {team['goals_for']:>3} "
            f"{team['goals_against']:>3} {team['goal_difference']:>3} {team['points']:>4}"
        )


# Main menu

def main():
    while True:
        print("\nFootball League Manager")
        print("1. Add team")
        print("2. Record match")
        print("3. Show standings")
        print("4. Simulate match")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter team name: ")
            add_team(name)

        elif choice == "2":
            if len(teams) < 2:
                print("Add at least two teams first.")
                continue

            home = input("Home team: ")
            away = input("Away team: ")
            home_goals = int(input("Home goals: "))
            away_goals = int(input("Away goals: "))
            play_match(home, away, home_goals, away_goals)

        elif choice == "3":
            show_standings()

        elif choice == "4":
            if len(teams) < 2:
                print("Add at least two teams first.")
                continue

            home = input("Home team: ")
            away = input("Away team: ")
            simulate_match(home, away)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the program only when this file is executed directly
if __name__ == "__main__":
    main()
