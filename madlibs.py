noun_list = list()
adjective_list = list()
verb_list = list()
place_list = list()
food_list = list()


def nouns(amount):
    '''asks user for nouns'''
    print("Enter {} nouns".format(amount))
    for i in range(amount):
        nouns = input()
        noun_list.append(nouns)


def adject(amount):
    '''asks user for adjectives'''
    print("Enter {} adjectives".format(amount))
    for i in range(amount):
        adjectives = input()
        adjective_list.append(adjectives)


def place():
    '''asks user for a place'''
    print("Enter a place")
    place = input()
    place_list.append(place)


def name():
    '''asks user for a place'''
    print("Enter a name")
    name = input()
    place_list.append(name)


def food():
    '''asks user for a food'''
    print("Enter a food")
    food = input()
    food_list.append(food)


def story1():
    nouns(2)
    adject(2)
    print("The {} is {}, the {} is {}".format(noun_list[0], adjective_list[0],
          noun_list[1], adjective_list[1]))


def story2():
    nouns(2)
    adject(2)
    food()
    place()
    print("The {} {} and the {} {} love eating {} in {}".format(adjective_list[0], noun_list[0], 
          adjective_list[1], noun_list[1], food_list[0], place_list[0]))


def select(): 
    print("Choose your story! 1, 2")
    choice = input()

    if choice is '1':
        story1()
    elif choice is '2':
        story2()


select()
