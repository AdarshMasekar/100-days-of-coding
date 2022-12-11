travel_log = [
    {
        "country" : "India",
        "visits" :  24,
        "cities" : ['Goa','Mirzapur','hyderabad']
    },
    {
        "country" : "Nepal",
        "visits" :  12,
        "cities" : ['Pokhara','Thimpu']
    },
    {
        "country" : "Bangladesh",
        "visits" :  12,
        "cities" : ['Dhaka','Sirla']
    },
   
]
def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

add_new_country("Russia", 2, ['Moscow','Saint', 'Petersburg'])

for i in range(0,len(travel_log)):
    for j in range(0,len(travel_log[i])):
        print(f"You Have visited {travel_log[i]['country']} {travel_log[i]['visits']}  times")
