from scripts.animal import Animal,AnimalShelter
import pytest

def test_animal_shelter():
    shelter = AnimalShelter()

    # Enqueue some animals
    shelter.enqueue(Animal("dog", "Buddy"))
    shelter.enqueue(Animal("cat", "Whiskers"))
    shelter.enqueue(Animal("dog", "Max"))
    shelter.enqueue(Animal("cat", "Oliver"))

    # Dequeue a dog
    dog = shelter.dequeue("dog")
    assert dog.name == "Buddy"

    # Dequeue a cat
    cat = shelter.dequeue("cat")
    assert cat.name == "Whiskers"

    # Dequeue a dog again
    dog = shelter.dequeue("dog")
    assert dog.name == "Max"

    # Dequeue a cat again
    cat = shelter.dequeue("cat")
    assert cat.name == "Oliver"

    # Dequeue with invalid preference
    invalid_pref = shelter.dequeue("bird")
    assert invalid_pref is None