#COUNTRY  POPULATION
#Poland   38000000

countries = [
{"name":"Poland", "population":38000000},
{"name": "China", "population": 1410000000},
{"name": "India", "population": 1420000000},
{"name": "United States", "population": 334000000},
{"name": "Indonesia", "population": 276000000},
{"name": "Pakistan", "population": 240000000},
{"name": "Brazil", "population": 213000000}
]


print("COUNTRY         POPULATION")
for country in countries:
    print(f"{country['name']:<15} {country['population']}")