import json

number_of_countries = 5
list_of_neighbors_for_each_country = []
map = {}

#this loop creats default neighbors as [0] 
for i in range(number_of_countries-1): #-1 because every country has at most n-1 neighbors
    list_of_neighbors_for_each_country.append(0)


#creats a dictionary with n keys and neighbors' list as values
for i in range(1, number_of_countries+1):
    map[i] = list_of_neighbors_for_each_country


#serializing our dictionary to json file
with open("map.json", "w") as write_file:
    json.dump(map, write_file, indent=4)


    
#--------------------------------------
with open("map.json", "r") as read_file:
    new_map = json.load(read_file)
new_map = dict(new_map)
for i in new_map:                           #this block reads from a json file and return a dictionary then set all keys' values 
    set_of_neighbors = set(new_map[i])
    new_map[i] = set_of_neighbors
#--------------------------------------
print(new_map)
    