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


    for i in data:
        if i == "A X":
            score += 3+1
        elif i == "A Y":
            score += 6+2
        elif i == "A Z":
            score += 0+3
        elif i == "B X":
            score += 0+1
        elif i == "B Y":
            score += 3+2
        elif i == "B Z":
            score += 6+3
        elif i == "C X":
            score += 6+1
        elif i == "C Y":
            score += 0+2
        elif i == "C Z":
            score += 3+3

    print(score)