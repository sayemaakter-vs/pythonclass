scores = {
    "Amina": {"python": 82, "statistics": 76, "calculus": 88},
    "Maya": {"python": 58, "statistics": 64, "calculus": 61},
    "Disha": {"python": 91, "statistics": 89, "calculus": 94},
    "Nora": {"python": 45, "statistics": 52, "calculus": 56}
}

results = {}
highest_average = 0
highest_student = ""

for student, subjects in scores.items():
    total = 0

    for score in subjects.values():
        total += score

    average = total / len(subjects)

    if average >= 60:
        status = "Pass"
    else:
        status = "Fail"

    results[student] = {
        "average": round(average, 2),
        "status": status
    }

    if average > highest_average:
        highest_average = average
        highest_student = student

print("Results:", results)
print("Highest average:", highest_student, highest_average)