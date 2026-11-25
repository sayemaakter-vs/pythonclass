import pandas as pd

data = {
    "Name": ["Amina", "Maya", "Lina", "Nora", "Sara"],
    "Quiz": [18, 12, 16, 9, 15],
    "Midterm": [25, 19, 28, 15, 22],
    "Final": [45, 31, 40, 25, 38]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

df["Total"] = df["Quiz"] + df["Midterm"] + df["Final"]

df["Average"] = df["Total"] / 3

df["Status"] = df["Total"].apply(
    lambda x: "Pass" if x >= 50 else "Fail"
)

print("\nCompleted DataFrame:")
print(df)

passed_students = df[df["Status"] == "Pass"]

print("\nStudents who passed:")
print(passed_students)

df = df.sort_values(by="Total", ascending=False)

print("\nSorted DataFrame:")
print(df)

df.to_excel("student_results.xlsx", index=False)

print("Data exported successfully")