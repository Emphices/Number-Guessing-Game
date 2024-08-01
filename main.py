import random

def number_guessing_game():
    number_to_guess = random.randint(1,100)
    attempts = 0

    while True:
        try:
            user_guess = int(input("Guess A number between 1 to 100"))
            attempts += 1

            if user_guess < number_to_guess:
                print("To low")
            elif user_guess > number_to_guess:
                print("Too High")
            else:
                print(f"Congrats, You Guessed The Right Number!")
                break
        except ValueError:
            print("Please Enter A Valid Number.")
    
if __name__ == "__main__":
    number_guessing_game()
