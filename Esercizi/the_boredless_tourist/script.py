destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

test_travel = ["Erik Wilkes", "Shanghai, China", ["historical site", "art"]]

def get_destination_index(dest):
  destination_index = destinations.index(dest)
  return destination_index

def get_traveler_location(traveler):
  trav_dest = traveler[1]
  trav_dest_index = get_destination_index(trav_dest)
  return trav_dest_index

test_dest_index = get_traveler_location(test_travel)

attractions = [[] for dest in destinations]

def add_attraction(dest, attr):
  dest_index = get_destination_index(dest)
  attr_for_dest = attractions[dest_index]
  attr_for_dest.append(attr)
  return

add_attraction("Los Angeles, USA",["Venice Beach", ["beach"]])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

def find_attraction(dest, interests):
  dest_index = get_destination_index(dest)
  attr_in_city = attractions[dest_index]
  attr_with_int = []
  for pos_attr in attr_in_city:
    attr_tag = pos_attr[1]
    for inter in interests:
      if(inter in attr_tag):
        attr_with_int.append(pos_attr[0])
  return attr_with_int

la_arts = find_attraction("Los Angeles, USA", ["art"])

def get_attractions_for_traveler(traveler):
  trav_dest = traveler[1]
  trav_int = traveler[2]
  trav_attr = find_attraction(trav_dest, trav_int)
  int_string = f"Hi {traveler[0]}, we think you'll like these places around {trav_dest}:"
  for attr in trav_attr:
    int_string = int_string + f" {attr}; "
  return int_string

smills_france = get_attractions_for_traveler(["Derek Smill", "Paris, France", ['monument']])

print(smills_france)