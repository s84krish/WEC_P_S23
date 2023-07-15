import json

file = open('./json/distance.json',mode='r')
 
# read all lines at once
data = file.read()
 
# close the file
file.close()

file = open('./json/input.json',mode='r')
 
# read all lines at once
data = file.read()
 
# close the file
file.close()
input = json.loads(data)

cities = ['Tilbury', 'Mississauga', 'Cornwall', 'London', 'Windsor', 'Niagara_Falls', 'Barrie', 'Kingston', 'Huntsville', 'North_Bay']