import random

team1_players = ["Avneesh", "Ranjit", "Vishal"]
team2_players = ["Shanara", "Khushi", "Vaishnavi"]

overs_per_team = 5
balls_per_over = 6


def play_inning(players, overs):
    total_runs = 0
    total_wickets = 0
    player_scores = {player: 0 for player in players}

    for over in range(overs):
        for ball in range(balls_per_over):
            outcome = random.choices(["run", "out", "no_run"], [0.33, 0.33, 0.33])[0]
            if outcome == "run":
                runs = random.choice([1, 2,  4, 6])
                total_runs += runs
                current_batsman = players[total_wickets % len(players)]
                player_scores[current_batsman] += runs
                print(f"{current_batsman} scores {runs} runs.")

            elif outcome == "out":
                total_wickets += 1
                print(f"Wicket! {players[total_wickets % len(players)]} is out.")
                if total_wickets >= len(players):
                    break

            elif outcome == "no_run":
                print("No run.")

        if total_wickets >= len(players):
            break

    return total_runs, total_wickets, player_scores


toss_winner = random.choice(["Team 1", "Team 2"])
choice = random.choice(["bat", "bowl"])

print(f"{toss_winner} won the toss and chose to {choice} first.")

if toss_winner == "Team 1" and choice == "bat" or toss_winner == "Team 2" and choice == "bowl":
    print("Team 1 is batting first.")
    team1_score, team1_wickets, team1_player_scores = play_inning(team1_players, overs_per_team)
    print("\nTeam 2 is batting:")
    team2_score, team2_wickets, team2_player_scores = play_inning(team2_players, overs_per_team)
else:
    print("Team 2 is batting first.")
    team2_score, team2_wickets, team2_player_scores = play_inning(team2_players, overs_per_team)
    print("\nTeam 1 is batting:")
    team1_score, team1_wickets, team1_player_scores = play_inning(team1_players, overs_per_team)

if team1_score > team2_score:
    winner = "Team 1"
elif team2_score > team1_score:
    winner = "Team 2"
else:
    winner = "Draw"

print("\nGame Summary")
print(f"Team 1 Score: {team1_score}/{team1_wickets}")
for player, score in team1_player_scores.items():
    print(f"{player}: {score} runs")

print(f"Team 2 Score: {team2_score}/{team2_wickets}")
for player, score in team2_player_scores.items():
    print(f"{player}: {score} runs")

print(f"Winner: {winner}")
