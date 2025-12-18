import matplotlib.pyplot as plt

# Dictionary with cities and their recorded temperatures
medals = [{"country":"Denmark","gold":2,"silver":4,"bronze":6},
{"country":"Finland","gold":5,"silver":0,"bronze":4},
{"country":"USA","gold":12,"silver":5,"bronze":11},
{"country":"Peru","gold":0,"silver":1,"bronze":7}]

# Use map to separate the city names and their corresponding temperatures
countries = list(map(lambda country: country['country'], medals))  # List of city names
medal = list(map(lambda country: country['gold']+country['silver']+country['bronze'], medals))  # List of temperatures

# Create a bar chart
plt.bar(countries, medal, color='gold')

# Add title and labels
plt.title('the total number of medals won by each country')
plt.xlabel('country')
plt.ylabel('medals')

# Show the plot
plt.show()