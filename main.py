
from ui import ui
from game.game import Guess

def play():
    """Start and play the guessing game."""
    ui.print_welcome_message()  # Print welcome message
    ui.print_instructions()  # Print game instructions
    
    num_rounds = int(input("[?] How many rounds do you want to play? "))  # Ask user for the number of rounds
    game = Guess()  # Create a new game instance
    
    # Loop through each round
    for round_num in range(1, num_rounds + 1):
        game.reset()  # Reset the game for the new round
        ui.print_round_info(round_num, 0)  # Print information about the current round
        
        # Loop through each chance in the round
        for chance in range(5):
            try:
                number = int(input("(1 - 50) > "))  # Ask user to guess the number
                if game.match(number):  # Check if the guess is correct
                    ui.print_win(chance + 1)  # Print win message
                    break  # Exit the loop if the guess is correct
                else:
                    ui.print_hint(game.hint())  # Print hint for incorrect guess
            except ValueError:
                ui.print_invalid_input()  # Print message for invalid input
        
        else:
            ui.print_lose(game.answer())  # Print lose message if all chances are used
        
        ui.print_round_end()  # Print message at the end of each round

    ui.print_results(num_rounds, game.score())  # Print final results

if __name__ == '__main__':
    play()  # Start the game
