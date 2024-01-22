"""
    Day 21: Mini Project - Simple Text-Based Game
        Apply OOP principles to design game classes.
        Implement game logic using classes and methods.
"""

import random 

class RandomGuessingGame:
    
    # Initialise the class with lower, and upper bound, and initialise counter
    def __init__(self, lower_range, upper_range):
        self.random_number = None
        self.lower_range = lower_range  
        self.upper_range = upper_range
        self.attemps = 0

    # Generate a random number
    def generateRandomNumber(self):
        self.random_number = random.randint(self.lower_range, self.upper_range)

    # startGame
    def playGame(self):
        
        #Initialise Game
        GameOver = False
        self.generateRandomNumber()

        while (not GameOver):
            
            #Guess if it a random number
            try:
                userGuess = input("Guess the secret number: ")
            except Exception as e:
                return f"Unexpected error: {e}"

            #Check options
            if userGuess.lower() == 'q':
                return "You just quit the game"
            
            elif userGuess.lower() == 'ans':
                return f"The answer is {self.random_number}"
            
            elif int(userGuess) == self.random_number:
                return f"You guessed the number after {self.attemps}"
            else:
                self.attemps += 1
            

    
if __name__ == "__main__":
    game = RandomGuessingGame(0,10)
    result = game.playGame()
    print(result)
            
    

    