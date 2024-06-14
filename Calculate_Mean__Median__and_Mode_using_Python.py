import statistics

# Sample list of numbers
data = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9, 9]

# Calculate mean
mean = statistics.mean(data)
print(f"Mean: {mean}")

# Calculate median
median = statistics.median(data)
print(f"Median: {median}")

# Calculate mode
mode = statistics.mode(data)
print(f"Mode: {mode}")

