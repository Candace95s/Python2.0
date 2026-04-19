import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("server_log.csv", comment='#')

# Fill missing values with column mean
df = df.fillna(df.mean())

# Calculate mean response time for each column
means = df.mean()

print(means)

# Plot (PIE CHART)
means.plot(kind='pie', autopct='%1.1f%%')
plt.title("Average Response Time by Service")

# Save image
plt.savefig("log_analysis_pie.png")

plt.show()