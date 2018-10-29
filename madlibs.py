noun_list = list()
adjective_list = list()
verb_list = list()
place_list = list()
food_list = list()

print("Enter 3 nouns")
for i in range(3):
    nouns = input()
    noun_list.append(nouns)

print("Enter 3 adjectives")
for i in range(3):
    adjectives = input()
    adjective_list.append(adjectives)

print("Enter a place")
place = input()
place_list.append(place)

print("Enter a food")
food = input()
food_list.append(food)

print('The {} is {}, the {} is {}, the {} is {}. Lets eat {} in {}.'.format(
      noun_list[0], adjective_list[0], noun_list[1], adjective_list[1],
      noun_list[2], adjective_list[2], food_list[0], place_list[0]))
