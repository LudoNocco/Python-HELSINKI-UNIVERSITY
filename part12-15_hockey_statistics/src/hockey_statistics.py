import json

def load_data(filename):
    with open(filename) as file:
        data = json.load(file)
    print(f"read the data of {len(data)} players")
    return data

def search_player(players, name):
    for player in players:
        if player['name'].lower() == name.lower():
            print_player_stats(player)
            return
    print(f"Player '{name}' not found.")

def list_teams(players):
    teams = sorted(set(player['team'] for player in players))
    for team in teams:
        print(team)

def list_countries(players):
    countries = sorted(set(player['nationality'] for player in players))
    for country in countries:
        print(country)

def players_in_team(players, team):
    team_players = [p for p in players if p['team'] == team]
    team_players = sorted(team_players, key=lambda p: (p['goals'] + p['assists']), reverse=True)
    for player in team_players:
        print_player_stats(player)

def players_from_country(players, country):
    country_players = [p for p in players if p['nationality'] == country]
    country_players = sorted(country_players, key=lambda p: (p['goals'] + p['assists']), reverse=True)
    for player in country_players:
        print_player_stats(player)

def most_points(players, n):
    sorted_players = sorted(
        players,
        key=lambda p: (p['goals'] + p['assists'], p['goals']),
        reverse=True
    )
    for player in sorted_players[:n]:
        print_player_stats(player)

def most_goals(players, n):
    sorted_players = sorted(
        players,
        key=lambda p: (p['goals'], -p['games']),
        reverse=True
    )
    for player in sorted_players[:n]:
        print_player_stats(player)

def print_player_stats(player):
    name = player['name']
    team = player['team']
    goals = player['goals']
    assists = player['assists']
    points = goals + assists
    print(f"{name:<21}{team:>3}{goals:>4} +{assists:>3} ={points:>4}")

# Remove the if __name__ == "__main__": guard
filename = input("file name: ")
players = load_data(filename)

while True:
    print("commands:")
    print("0 quit")
    print("1 search for player")
    print("2 teams")
    print("3 countries")
    print("4 players in team")
    print("5 players from country")
    print("6 most points")
    print("7 most goals")

    command = input("command: ")

    if command == "0":
        break
    elif command == "1":
        name = input("name: ")
        search_player(players, name)
    elif command == "2":
        list_teams(players)
    elif command == "3":
        list_countries(players)
    elif command == "4":
        team = input("team: ")
        players_in_team(players, team)
    elif command == "5":
        country = input("country: ")
        players_from_country(players, country)
    elif command == "6":
        n = int(input("how many: "))
        most_points(players, n)
    elif command == "7":
        n = int(input("how many: "))
        most_goals(players, n)
