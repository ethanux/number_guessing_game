#!/usr/bin/env python
import random  # Import the random module to generate random numbers

# Define the Guess class for the number guessing game
class Guess:

    # Initialize the Guess class
    def __init__(self) -> None:
        self._score = 0  # Initialize the player's score
        self._plays = 0  # Initialize the number of plays
        self._chance = 0  # Initialize the number of chances taken
        self._number = None  # Initialize the target number

    # Method to check if the input number matches the target number
    def match(self, num: int) -> bool:
        if self._number == num:  # If the numbers match
            self._score += 1  # Increment the player's score
            return True  # Return True
        else:
            self._chance += 1  # Increment the number of chances taken
            return False  # Return False

    # Method to provide a hint based on the target number
    def hint(self) -> str:
        if self._number > 1 and self._number < 11:  # If the target number is between 1 and 10
            return "number between 1 and 10"  # Return hint
        elif self._number > 10 and self._number < 21:  # If the target number is between 11 and 20
            return "number between 11 and 20"  # Return hint
        elif self._number > 20 and self._number < 31:  # If the target number is between 21 and 30
            return "number between 21 and 30"  # Return hint
        elif self._number > 30 and self._number < 41:  # If the target number is between 31 and 40
            return "number between 31 and 40"  # Return hint
        else:
            return "number greater than 40"  # Otherwise, return hint

    # Method to return the number of plays
    def plays(self) -> int:
        return self._plays  # Return the number of plays

    # Method to return the target number
    def answer(self) -> int:
        return self._number  # Return the target number

    # Method to return the player's score
    def score(self) -> int:
        return self._score  # Return the player's score

    # Method to reset the game for a new play
    def reset(self) -> None:
        self._plays += 1  # Increment the number of plays
        self._chance = 0  # Reset the number of chances taken
        self._number = random.randint(1, 50)  # Generate a new random target number between 1 and 50

    # Method to return the number of chances taken
    def chance(self) -> int:
        return self._chance  # Return the number of chances taken
