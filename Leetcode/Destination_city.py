# Destination city

def destination():
    paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
    outgoing_city = {}
    for path in paths:
        city_a, city_b = path
        outgoing_city[city_a] = outgoing_city.get(city_a, 0) + 1
        outgoing_city[city_b] = outgoing_city.get(city_b, 0)

    for city in outgoing_city:
        if outgoing_city[city] == 0:
            return city
print(destination())  # o/p Sao Paulo