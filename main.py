if __name__ == '__main__':
    score = 0

    with open('input.txt') as file:
        data = file.read().split("\n")

    # a = rock_enemy
    # b = paper_enemy
    # c = scissors_enemy

    # x = rock              1 point(s)
    # y = paper             2 point(s)
    # z = scissor           3 point(s)

    # lose = 0 points
    # draw = 3 points
    # win  = 6 points

    rounds = {
        "A X":4, "A Y":8, "A Z":3, "B X":1, "B Y":5, "B Z":9, "C X": 7, "C Y":2,"C Z":6
    }

    for i in data:
        score += rounds[i]

    print(score)

# part 2

# x = lose
# y = draw
# z = win
    score2 = 0

    part2_rounds = {
        "A X":3, "A Y":4, "A Z":8, "B X":1, "B Y":5, "B Z":9, "C X":2, "C Y":6, "C Z":7
    }

    for i in data:
        score2 += part2_rounds[i]

    print(score2)
