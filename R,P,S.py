import random

class AdaptiveAI:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.player_history = []
        self.ai_history = []
        self.wins = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}

    def get_choice(self):
        if len(self.player_history) < 3:
            return random.choice(self.choices)
        else:
            # Look for patterns in the player's last few moves
            last_three = self.player_history[-3:]
            if last_three.count(last_three[0]) == 3:
                # If player repeated the same move 3 times, choose the winning move
                return self.wins[self.wins[last_three[0]]]
            elif last_three[0] == last_three[1] and last_three[1] != last_three[2]:
                # If player changed after two same moves, predict they'll go back to first move
                return self.wins[last_three[0]]
            else:
                # Otherwise, choose based on what beats the player's most frequent recent move
                most_frequent = max(set(last_three), key=last_three.count)
                return self.wins[most_frequent]

    def learn(self, player_choice, ai_choice):
        self.player_history.append(player_choice)
        self.ai_history.append(ai_choice)

def play_game():
    ai = AdaptiveAI()
    player_score = 0
    ai_score = 0

    print("Welcome to Rock Paper Scissors!")
    print("Enter 'rock', 'paper', or 'scissors'. Type 'quit' to end the game.")

    while True:
        player_choice = input("\nYour choice: ").lower()
        if player_choice == 'quit':
            break
        if player_choice not in ai.choices:
            print("Invalid choice. Please try again.")
            continue

        ai_choice = ai.get_choice()
        print(f"AI chooses: {ai_choice}")

        if player_choice == ai_choice:
            print("It's a tie!")
        elif ai.wins[player_choice] == ai_choice:
            print("You win!")
            player_score += 1
        else:
            print("AI wins!")
            ai_score += 1

        ai.learn(player_choice, ai_choice)
        print(f"Score - You: {player_score}, AI: {ai_score}")

    print("\nFinal Score:")
    print(f"You: {player_score}")
    print(f"AI: {ai_score}")
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
    