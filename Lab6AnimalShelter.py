# Setting the shelter capacity as a constant
CAPACITY = 5

# Creating a list to store shelter animals
shelter_animals = []

"""Adds an animal to the list of animals, as long capacity is not reached.
Returns a message if the animal is added or if the shelter is at capacity."""
def add_animal(name, species):
    if get_animal_count() >= CAPACITY:
        return "Can't add " + name + " the " + species + ". The shelter is at capacity."
    shelter_animals.append({"name": name, "species": species})
    return name + " the " + species + " has been added to the shelter."

"""Removes an animal from the shelter animals list and
returns a message saying the animal is adopted."""
def adopt_animal(name):
    for animal in shelter_animals:
        if animal["name"] == name:
            shelter_animals.remove(animal)
            return name + " has been adopted!"

"""Returns the current number of animals in the shelter."""
def get_animal_count():
    return len(shelter_animals)

# Animals in the shelter.
print(add_animal("Kirby", "Dog"))
print(add_animal("Sammy", "Dog"))
print(add_animal("Franklin", "Cat"))
print(add_animal("Whiskers", "Hamster"))
print(add_animal("Waffles", "Cat"))
print(add_animal("Scooter", "Dog"))

#Animal count before adoption.
print("Animal count: " + str(get_animal_count()))

print(adopt_animal("Franklin"))

# Animal count after adoption
print("Animal count: " + str(get_animal_count()))


