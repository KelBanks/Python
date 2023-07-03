import random

attempts_array = []


def score():
    if not attempts_array:
        print("Excellent!")
    else:
        print(f"The current high score is "
              f"{min(attempts_array)} attempts")
        
def start_game():
    attempts = 0
    random_num = random.randint(1,50)
    print("Greetings, Welcome to Magic Guess!")
    player_name = input("Enter your name: ")
    question_player = input(
        f"Hello, {player_name}, how about a game?"
        f"(Enter Yes/No): ")
    
    if question_player.lower() != "yes":
       print("Sad to see you go. Have a wonderful day!")
       exit()

    else:
        score()

    while question_player.lower() == "yes":
        try:
            guess = int(input("Pick a number between 1 and 50: "))
            if guess < 1 or guess > 50:
                raise ValueError("Guess a number between given range")
            
            attempts += 1
            attempts_array.append(attempts)

            if guess == random_num:
                print("Great job!")
                print(f"It took you {attempts} trys!")
                question_player = input("Would you like to play again? (Yes/No): ")
                if question_player.lower() != "yes":
                    print("Hope you had fun, take care now!")
                    break
                else:
                    attempts = 0
                    random_num = random.randint(1, 50)
                    score()
                    continue
            else:
                if guess > random_num:
                    print("Number is lower")
                elif guess < random_num:
                    print("Number is higher")

        except ValueError as error_count:
            print("Not a value, try again")
            print(error_count)

if __name__ == "__main__":
    start_game()

