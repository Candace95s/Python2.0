import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the CSV file
# comment="#" ignores any lines in the file that start with #
df = pd.read_csv("server_log.csv", comment="#")

# Step 2: Convert all columns to numeric values
# Any invalid value will become NaN
df = df.apply(pd.to_numeric, errors="coerce")

# Step 3: Fill missing values in each column with that column's mean
for column in df.columns:
    column_mean = df[column].mean()
    df[column] = df[column].fillna(column_mean)

# Step 4: Remove any columns that are still completely empty
df = df.dropna(axis=1, how="all")

# Step 5: Calculate the mean response time for each service
mean_response_times = df.mean()

# Step 6: Remove any remaining NaN values before plotting
mean_response_times = mean_response_times.dropna()

# Step 7: Print cleaned data
print("Cleaned Server Log Data:")
print(df)

print("\nAverage Response Time Per Service:")
print(mean_response_times)

# Step 8: Create pie chart
plt.figure(figsize=(8, 6))
plt.pie(
    mean_response_times,
    labels=mean_response_times.index,
    autopct="%1.1f%%",
    startangle=140
)

plt.title("Server Response Time Distribution")
plt.savefig("log_analysis_pie.png")
plt.show()