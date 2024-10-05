# score.py

def save_high_score(score):
    high_scores = load_high_scores()
    high_scores.append(score)
    high_scores.sort(reverse=True)
    high_scores = high_scores[:5]

    with open("high_scores.txt", "w") as file:
        for score in high_scores:
            file.write(str(score) + "\n")

def load_high_scores():
    try:
        with open("high_scores.txt", "r") as file:
            high_scores = [int(line.strip()) for line in file.readlines()]
    except FileNotFoundError:
        high_scores = []
    return high_scores
