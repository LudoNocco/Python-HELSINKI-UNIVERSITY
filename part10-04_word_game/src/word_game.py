import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds + 1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            result = self.round_winner(answer1, answer2)
            if result == 1:
                self.wins1 += 1
                print("player 1 won")
            elif result == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                print("Round not counted due to invalid input.")

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player1_word) < len(player2_word):
            return 2
        else:
            pass

class MostVowels(WordGame):
    def round_winner(self, player1_word: str, player2_word: str):
        if sum(c.lower() in "aeiou" for c in player1_word) > sum(c.lower() in "aeiou" for c in player2_word):
            return 1
        elif sum(c.lower() in "aeiou" for c in player1_word) < sum(c.lower() in "aeiou" for c in player2_word):
            return 2
        else:
            pass

class RockPaperScissors(WordGame):
    def round_winner(self, player1_word: str, player2_word: str):
        valid_moves = {"rock", "paper", "scissors"}
        
        if player1_word in valid_moves and player2_word in valid_moves:
            if player1_word == "rock" and player2_word == "scissors":
                return 1
            elif player1_word == "scissors" and player2_word == "rock":
                return 2
            elif player1_word == "paper" and player2_word == "rock":
                return 1
            elif player1_word == "rock" and player2_word == "paper":
                return 2
            elif player1_word == "scissors" and player2_word == "paper":
                return 1
            elif player1_word == "paper" and player2_word == "scissors":
                return 2
            else:
                return None
        elif player1_word in valid_moves and player2_word not in valid_moves:
            return 1
        elif player1_word not in valid_moves and player2_word in valid_moves:
            return 2
        else:
            return 3
