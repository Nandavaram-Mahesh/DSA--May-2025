# scores = [100, 90, 80, 70]
#  Update the score of player_id = 2


def updateLeaderboard(scores, player_id, score):
    scores[player_id - 1] = score

scores = [100, 90, 80, 70]
player_id = 2
score = 55
updateLeaderboard(scores, player_id, score)