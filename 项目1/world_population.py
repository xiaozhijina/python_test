# coding:utf8

import json

with open('world_population.json') as w_population:
    pop_data = json.load(w_population)

for pop_dict in pop_data:
    if pop_dict['Year'] == '1970-08-25':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        print(country_name + ' : ' + str(population))

