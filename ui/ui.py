
import time

def print_welcome_message():
    """Print a welcome message to the user."""
    print("Welcome to my guessing game")

def print_round_info(plays, chance):
    """Print information about the current round."""
    print("====================================================================")
    print(f"[!] Round {plays} | Chances remaining: {5 - chance}")
    print("[!] Guess a number between 1 and 50")
    print("====================================================================")

def print_results(plays, score):
    """Print the final results of the game."""
    print("OKAY...")
    time.sleep(1)
    print("Results")
    print("Played    Win    Lost")
    print('----------------------')
    print(f"{plays}        {score}        {plays - score}")

def print_instructions():
    """Print instructions for the game."""
    print("Instructions:")
    print("1. You have 5 rounds to guess the correct number.")
    print("2. Each round, you have 5 chances to guess the number.")
    print("3. The number to guess is between 1 and 50.")
    print("4. Good luck!")

def print_invalid_input():
    """Print a message for invalid user input."""
    print("[-] Invalid input! Please enter a valid number.")

def print_hint(hint):
    """Print a hint based on the target number."""
    print(f"[!] Hint: {hint}")

def print_win(attempts):
    """Print a message for winning the game."""
    print(f"[+] Congratulations! You won with {attempts} attempts.")

def print_lose(answer):
    """Print a message for losing the game."""
    print(f"[-] You lose! The correct answer was {answer}.")

def print_round_end():
    """Print a message at the end of each round."""
    print("====================================================================")
