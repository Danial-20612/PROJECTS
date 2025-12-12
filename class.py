import sqlite3
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_csv("mental_health_wearable_dataset.csv")

# displaying
print("Sample Data:")
print(df.head())


# display intended columns
print("------------------------------------------------------------------")

selected_columns = ["timestamp", "heart_rate" , "stress_label", "session_duration"]
df_select = df[selected_columns].dropna()

# displaying
print(selected_columns)
print(df_select.head())

print("Data Info:") # Check data types and missing values​
print(df_select.info())

# # database
# base = sqlite3.connect("mental_health_data.db")

# df_select.to_sql("user_activity" , base, if_exists="replace", index=False)

# # display
# print("Data successfully stored in SQLite database")

# # verify data storage
# query_result = pd.read_sql("SELECT * user_activity LIMIT 5;", base)

# print("Sample data base from database")

# print(query_result)

print("Lets calculate the CVS file data based on weeks: ")
# this will select and focus on the timestamp section 
column = ["timestamp"]
df_selected = df[column].dropna()
print(df_selected)
filtered_activity =pd.date_range(start="31/07/2024", periods=7, freq="D")
print(filtered_activity)

df["time_only"]  = df["timestamp"]
print("The time")
print(df)

def activity_summary(data):
    print("Average Heart Rate " , round(data["heart_rate"].mean(), 2))
    print("Average Session Duration (minutes)")
    round(data["session_duration"].mean(), 2)
    print("Stess Label Distribution: " , data["stress_label"].value_counts())
    activity_summary(df_select)

print("New class------------------------------------------------------------------------------------------")

plt.figure(figsize=(10,5))

sns.lineplot(x="timestamp", y="heart_rate", data= df_select.head(200))
plt.title("Heart Rate Over Time: ")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()