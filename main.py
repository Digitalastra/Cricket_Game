import random

team_1_boys = ["Avneesh", "Ranjit", "Vishal"]
team_2_girls = ["Shanara", "Khushi", "Vaishnavi"]

team_1 = team_1_boys
team_2 = team_2_girls

number_of_overs = 5
balls_per_over = 6

team_1_score = 0
team_2_score = 0
team_1_wickets = 0
team_2_wickets = 0


toss_winner = random.choice(["Team 1", "Team 2"])
if toss_winner == "Team 1":
    batting_first = "Team 1"
    batting_second = "Team 2"
else:
    batting_first = "Team 2"
    batting_second = "Team 1"

print(f"{toss_winner} won the toss and chose to bat first.")


for over in range(number_of_overs):
    for ball in range(balls_per_over):
        outcome = random.choice(["0", "1", "2", "3", "4", "6", "Wicket", "Wideball", "NoBall"])

        if outcome == "6":
            team_1_score += 6
        elif outcome == "4":
            team_1_score += 4
        elif outcome == "Wicket":
            team_1_wickets += 1
        elif outcome == "Wideball" or outcome == "NoBall":
            team_1_score += 1
            ball -= 1

for over in range(number_of_overs):
    for ball in range(balls_per_over):
        outcome = random.choice(["0", "1", "2", "3", "4", "6", "Wicket", "Wideball", "NoBall"])

        if outcome == "6":
            team_2_score += 6
        elif outcome == "4":
            team_2_score += 4
        elif outcome == "Wicket":
            team_2_wickets += 1
        elif outcome == "Wideball" or outcome == "NoBall":
            team_2_score += 1
            ball -= 1


if team_1_score > team_2_score:
    winner = "Team 1"
elif team_2_score > team_1_score:
    winner = "Team 2"
else:
    winner = "Draw"

print(f"Team 1 scored {team_1_score} runs.")
print(f"Team 2 scored {team_2_score} runs.")
print(f"Winner: {winner}")
