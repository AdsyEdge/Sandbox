
def main():
    score = float(input("Enter score: "))
    print(score_check(score))


def score_check(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif 90 > score >= 50:
        return "Passable"
    else:
        return "Excellent"


main()
