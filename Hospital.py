
# Hospital Patient Data Analysis Project

import pandas as pd
import matplotlib.pyplot as plt
import os


# 1. LOAD DATASET

df = pd.read_csv("hospital_data_cleaned.csv")
print("✅ Dataset loaded successfully")

# 2. DATA CLEANING

df = df.drop_duplicates()

numeric_cols = ["age", "cost", "length_of_stay", "satisfaction"]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df["age"].fillna(df["age"].median(), inplace=True)
df["cost"].fillna(df["cost"].mean(), inplace=True)
df["length_of_stay"].fillna(df["length_of_stay"].median(), inplace=True)
df["satisfaction"].fillna(df["satisfaction"].mean(), inplace=True)

print("✅ Data cleaning completed")

# 3. CREATE FOLDER FOR SAVING GRAPHS

if not os.path.exists("graphs"):
    os.mkdir("graphs")

# 4. BASIC BAR CHART – Gender Distribution

plt.figure()
df["gender"].value_counts().plot(kind="bar")
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Number of Patients")
plt.tight_layout()
plt.savefig("graphs/gender_distribution.png")
plt.show()

# 5. GEO SCATTER – City-wise Patient Count

city_count = df["city"].value_counts()

plt.figure()
plt.scatter(city_count.index, city_count.values)
plt.title("City-wise Patient Distribution")
plt.xlabel("City")
plt.ylabel("Number of Patients")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("graphs/geo_scatter_city.png")
plt.show()


# 6. PIE CHART – Payment Mode

payment_mode = df["payment_mode"].value_counts()

plt.figure()
plt.pie(payment_mode, labels=payment_mode.index, autopct="%1.1f%%")
plt.title("Payment Mode Distribution")
plt.savefig("graphs/payment_mode_pie.png")
plt.show()


# 7. BAR CHART – Average Cost by Condition

avg_cost_condition = df.groupby("condition")["cost"].mean()

plt.figure()
avg_cost_condition.plot(kind="bar")
plt.title("Average Treatment Cost by Condition")
plt.xlabel("Condition")
plt.ylabel("Average Cost")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("graphs/avg_cost_condition.png")
plt.show()


# 8. HISTOGRAM – Patient Satisfaction Rating

plt.figure()
plt.hist(df["satisfaction"], bins=5)
plt.title("Patient Satisfaction Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Patients")
plt.tight_layout()
plt.savefig("graphs/satisfaction_histogram.png")
plt.show()



# 9. HORIZONTAL BAR – Top 10 Cities

top_cities = df["city"].value_counts().head(10)

plt.figure()
top_cities.plot(kind="barh")
plt.title("Top 10 Cities by Patient Count")
plt.xlabel("Number of Patients")
plt.ylabel("City")
plt.tight_layout()
plt.savefig("graphs/top_cities_horizontal.png")
plt.show()


# 10. STACKED BAR – Gender vs Readmission

gender_readmission = pd.crosstab(df["gender"], df["readmission"])

plt.figure()
gender_readmission.plot(kind="bar", stacked=True)
plt.title("Gender vs Readmission Analysis")
plt.xlabel("Gender")
plt.ylabel("Patient Count")
plt.tight_layout()
plt.savefig("graphs/gender_readmission_stacked.png")
plt.show()


# 11. BAR CHART – Top 5 Doctors by Patient Count

top_doctors = df["doctor_name"].value_counts().head(5)

plt.figure()
top_doctors.plot(kind="bar")
plt.title("Top 5 Doctors by Patient Load")
plt.xlabel("Doctor Name")
plt.ylabel("Number of Patients")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("graphs/top_doctors.png")
plt.show()


# 12. SCATTER – Age vs Treatment Cost

plt.figure()
plt.scatter(df["age"], df["cost"])
plt.title("Age vs Treatment Cost")
plt.xlabel("Age")
plt.ylabel("Treatment Cost")
plt.tight_layout()
plt.savefig("graphs/age_vs_cost_scatter.png")
plt.show()

