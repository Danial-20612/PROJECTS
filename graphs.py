import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("mental_health_wearable_dataset.csv")

# Display sample data
print("Sample Data:")
print(df.head())

print("------------------------------------------------------------------")

# Select intended columns
selected_columns = ["timestamp", "heart_rate", "stress_label", "session_duration"]
df_select = df[selected_columns].dropna()

# Display selected columns
print("Selected Columns:")
print(df_select.head())

# Data info
print("Data Info:")  # Check data types and missing values
print(df_select.info())

# --- Database storage (optional) ---
# Uncomment if you want to store in SQLite
# base = sqlite3.connect("mental_health_data.db")
# df_select.to_sql("user_activity", base, if_exists="replace", index=False)
# print("Data successfully stored in SQLite database")
# query_result = pd.read_sql("SELECT * FROM user_activity LIMIT 5;", base)
# print("Sample data from database:")
# print(query_result)

# --- Weekly calculation ---
print("Let's calculate the CSV file data based on weeks:")
df_selected = df[["timestamp"]].dropna()
print(df_selected)

# Generate a date range (7 days starting from 31 July 2024)
filtered_activity = pd.date_range(start="2024-07-31", periods=7, freq="D")
print(filtered_activity)

# Extract time-only column (if timestamp is datetime, convert first)
df["time_only"] = pd.to_datetime(df["timestamp"], errors="coerce").dt.time
print("The time column added:")
print(df.head())

# --- Summary function ---
def activity_summary(data):
    print("Average Heart Rate:", round(data["heart_rate"].mean(), 2))
    print("Average Session Duration (minutes):", round(data["session_duration"].mean(), 2))
    print("Stress Label Distribution:\n", data["stress_label"].value_counts())

# Call summary
activity_summary(df_select)

print("------------------------------------------------------------------------------------------")

# # --- Visualization ---
# plt.figure(figsize=(10, 5))
# sns.lineplot(x="timestamp", y="heart_rate", data=df_select.head(200))
# plt.title("Heart Rate Over Time")
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# plt.figure(figsize=(6,4))
# sns.countplot(x='stress_label', data=df_select)
# plt.title('Stress Level Distribution')
# plt.xlabel('Stress Label')
# plt.ylabel('Count')
# plt.show()


plt.figure(figsize=(5,4))
sns.heatmap(df_select.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title('Heat Map: Correlation Between Health Metrics')
plt.show()


# plt.figure(figsize=(6,4))
# sns.barplot(x='stress_label', y='heart_rate', data=df_select)
# plt.title('Average Heart Rate per Stress Level')
# plt.tight_layout()
# plt.savefig('avg_heart_rate_stress.png')
# plt.show()


# def activity_summary(data):
#     print("\nAverage Heart Rate:", round(data['heart_rate'].mean(), 2))
#     print("Average Session Duration (minutes):", 
#     round(data['session_duration'].mean(), 2))
#     print("Stress Label Distribution:\n", data['stress_label'].value_counts())
#     activity_summary(df_selected)
#     plt.show()


