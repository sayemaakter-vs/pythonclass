import pandas as pd

df = pd.read_excel(r"C:\Users\ASUS\Downloads\employee_data.xlsx")

print("First five rows:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())

df["Department"] = df["Department"].fillna("Unknown")

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
df["Experience"] = df["Experience"].fillna(df["Experience"].mean())

def salary_level(salary):

    if salary >= 60000:
        return "High"
    elif salary >= 40000:
        return "Medium"
    else:
        return "Low"


df["Salary_Level"] = df["Salary"].apply(salary_level)

df = df.drop_duplicates()

print("\nCleaned Data:")
print(df)

df.to_excel("cleaned_employee_data.xlsx", index=False)

print("Cleaned data exported successfully")