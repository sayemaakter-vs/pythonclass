temperatures = [29.5, 31.0, None, 33.5, 34.0, 32.0, 35.5,
                36.0, None, 30.5, 28.0, 37.0, 38.0, 34.5]

clean_temperatures = []
missing_indices = []

for index in range(len(temperatures)):
    temperature = temperatures[index]

    if temperature is None:
        missing_indices.append(index)
        continue

    clean_temperatures.append(temperature)

mean_temperature = sum(clean_temperatures) / len(clean_temperatures)
minimum_temperature = min(clean_temperatures)
maximum_temperature = max(clean_temperatures)

above_mean = []
hot_day_count = 0
current_hot_run = 0
longest_hot_run = 0

for temperature in temperatures:
    if temperature is None:
        current_hot_run = 0
        continue

    if temperature > mean_temperature:
        above_mean.append(temperature)

    if temperature >= 35:
        hot_day_count += 1
        current_hot_run += 1

        if current_hot_run > longest_hot_run:
            longest_hot_run = current_hot_run
    else:
        current_hot_run = 0

print("Clean temperatures:", clean_temperatures)
print(f"Mean: {mean_temperature:.2f}")
print(f"Minimum: {minimum_temperature:.2f}")
print(f"Maximum: {maximum_temperature:.2f}")
print("Above mean:", above_mean)
print("Hot days:", hot_day_count)
print("Longest consecutive hot run:", longest_hot_run)
print("Missing indices:", missing_indices)