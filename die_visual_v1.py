from die import Die

# create a D6
die = Die()

# Make some rolls, and sore the results
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze the results
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)


print(frequencies)
