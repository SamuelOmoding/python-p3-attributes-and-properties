#!/usr/bin/env python3
#List of approved dog breeds
APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

#Dog class definition
class Dog:
    #Class variable to store the list of approved breeds
    approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", "French Bulldog", "Pug", "Pointer"]
    
    #Constructor method
    def __init__(self, name="Ben", breed="Corgi"):
       #Instance variables initializing with default values
        self.name = name
        self.breed = breed
    #The name property getter and setter methods
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        #To check if the name is a string and its lenght is between 1 and 25 characters
        if not isinstance(value, str) or not (1 <= len(value) <= 25):
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = value

    #The breed property getter and setter methods
    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, breed):
        # Checking if the breed is in the list of approved breeds
        if breed not in self.approved_breeds:
            print("Breed must be in list of approved breeds.")
        else:
            self._breed = breed
pass