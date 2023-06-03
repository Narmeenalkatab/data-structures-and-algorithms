class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name

class AnimalShelter:
    def __init__(self):
        self.dog_queue = []
        self.cat_queue = []
        self.counter = 0  # To track the order of enqueued animals

    def enqueue(self, animal):
        animal.order = self.counter
        self.counter += 1
        if animal.species == "dog":
            self.dog_queue.append(animal)
        elif animal.species == "cat":
            self.cat_queue.append(animal)

    def dequeue(self, pref):
        if pref == "dog":
            if self.dog_queue:
                return self.dog_queue.pop(0)
        elif pref == "cat":
            if self.cat_queue:
                return self.cat_queue.pop(0)
        else:
            if self.dog_queue and self.cat_queue:
                if self.dog_queue[0].order < self.cat_queue[0].order:
                    return self.dog_queue.pop(0)
                else:
                    return self.cat_queue.pop(0)
            elif self.dog_queue:
                return self.dog_queue.pop(0)
            elif self.cat_queue:
                return self.cat_queue.pop(0)

        return None


# I have added an order attribute to each enqueued
# animal to track the order and this is the (strech goal).