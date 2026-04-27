import matplotlib.pyplot as plt

# Step 1: CPU usage data (example values — you can change these)
hours = [1, 2, 3, 4, 5, 6, 7, 8]
cpu_usage = [25, 30, 85, 90, 40, 38, 75, 30]

# Step 2: Calculate statistics
avg_usage = sum(cpu_usage) / len(cpu_usage)
max_usage = max(cpu_usage)
min_usage = min(cpu_usage)

# Step 3: Print stats
print("CPU Usage Report")
print(f"Average Usage: {avg_usage:.2f}%")
print(f"Max Usage: {max_usage}%")
print(f"Min Usage: {min_usage}%")

# Step 4: Create a chart (choose ONE)

# ---- OPTION 1: BAR CHART ----
plt.bar(hours, cpu_usage)
plt.title("Hourly CPU Usage Report")
plt.xlabel("Hour")
plt.ylabel("Usage (%)")

# ---- OPTION 2: LINE GRAPH ----
# plt.plot(hours, cpu_usage, marker='o')
# plt.title("Hourly CPU Usage Report")
# plt.xlabel("Hour")
# plt.ylabel("Usage (%)")

# Show chart
plt.show()
plt.bar(hours, cpu_usage, color='skyblue')
plt.xticks(hours)  # ensures 1–8 show clearly
plt.grid(axis='y', linestyle='--', alpha=0.7)