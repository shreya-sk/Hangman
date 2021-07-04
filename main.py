import sys
from random_word import RandomWords
import threading as th
import HangmanVisuals


class HangmanGame:
    signal = True
    r = True
    lives = 7
    used = []

    def hangmanGame(self, word: str) -> None:
        print("Welcome to Hangman!\nPress enter to play the game or type 'exit' to quit.")
        answer = input()

        if answer.lower() == "exit":
            HangmanGame.gameExit()

        elif answer == "":

            print("~~~~~~~~~")
            print("Game is starting.")
            print("~~~~~~~~~")
            inp = input("Type 'help' to see the game rules or press 'enter' to begin game.\n")
            if inp.lower() == "help":
                HangmanGame.gameRules()

            timer = th.Timer(120, self.exit_time)
            timer.start()
            temp = list(word)
            st = ""
            for i in range(0, len(temp)):
                st += "_"
            blank = list(st)
            print("Guess the word: " + st)

            while True:

                b = ""
                if "_" not in "".join(blank):
                    print("Game over! You won.")
                    timer.cancel()
                    sys.exit()

                if self.lives > 0 and self.signal is True:
                    guess = input("Please guess a letter: ")
                    if guess.lower() == "exit":
                        HangmanGame.gameExit()
                        sys.exit()
                    else:
                        if guess.lower() in temp:
                            HangmanGame.letterPresent(temp, guess, blank, b)
                        else:
                            self.lives -= 1
                            self.letterNotPresent(self.lives, word)
                            if self.r is False:
                                timer.cancel()
                else:
                    sys.exit()

    def letterNotPresent(self, lives: int, word: str) -> None:
        if lives == 0 and self.signal is True:
            HangmanGame.visuals(self.lives)
            print("Game over! You have no lives remaining.")
            print("The word was " + word)
            self.r = False
            sys.exit()
        elif lives != 0 and self.signal is True:
            print()
            HangmanGame.visuals(self.lives)
            print("Incorrect! Try again.\nTotal lives remaining: " + str(lives))

        else:
            sys.exit()

    def exit_time(self):
        self.signal = False
        print("\nSorry your time is up!")
        HangmanGame.gameExit()

    @staticmethod
    def visuals(life) -> None:
        print(HangmanVisuals.lives_visual_dict.get(life))

    @staticmethod
    def gameExit() -> None:
        print("Bye-Bye.")
        print()
        sys.exit()

    @staticmethod
    def gameRules() -> None:
        print("--------RULES----------")
        print("1. You have to guess the word by entering letters.\n2. Each incorrect guess will decrease one life. "
              "There are only a total of 5 lives available.\n3. You only have 120 seconds to guess the word.\n4. To "
              "quit the game, type 'exit'.")
        print("-----------------------")

    @staticmethod
    def generateRandomWord() -> str:
        rw = RandomWords()
        rword = rw.get_random_word().lower()
        return rword

    @staticmethod
    def totalLetters(temp: list, guess: str) -> int:
        i = 0
        for j in temp:
            if j == guess:
                i += 1
        return i

    @staticmethod
    def letterPresent(temp: list, guess: str, blank: list, b: str) -> None:
        count = HangmanGame.totalLetters(temp, guess)
        if count == 1:
            indx = temp.index(guess, 0)
            blank[indx] = guess
        else:
            indx = temp.index(guess, 0)
            blank[indx] = guess
            for i in range(0, count - 1):
                indx = temp.index(guess, indx + 1)
                blank[indx] = guess

        for k in blank:
            b += k
        print(b)


if __name__ == "__main__":
    player = HangmanGame()
    obj = player.generateRandomWord()
    player.hangmanGame(obj)
