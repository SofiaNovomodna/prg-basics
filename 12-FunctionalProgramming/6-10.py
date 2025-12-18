import matplotlib.pyplot as plt

# Dictionary with cities and their recorded temperatures
temp = {"Krakow": 7, "Warszawa": -2, "Sopot": 4, "Koszalin": -1, "Opole": 3}

# Use map to separate the city names and their corresponding temperatures
cities = list(map(lambda x: x[0], temp.items()))  # List of city names
temperatures = list(map(lambda x: x[1], temp.items()))  # List of temperatures

# Create a bar chart
plt.bar(cities, temperatures, color='skyblue')

# Add title and labels
plt.title('Temperatures Recorded in Cities')
plt.xlabel('City')
plt.ylabel('Temperature (°C)')

# Show the plot
plt.show()