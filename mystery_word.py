import random
file = "words.txt"
LETTERS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
           "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


class Game:
    def __init__(self):
        self.player = Player("PLAYER 1")
        self.word = self.generate_word(file)

    def generate_word(self, file):
        with open(file) as f:
            words_list = f.read().splitlines()
            print(words_list)
        word = random.choice(words_list)
        print(word)
        letters = [letter for letter in word]
        print(letters)
        word_length = len(letters)
        print(word_length)
        self.show_blanks(word)
        return word

    def show_blanks(self, word):
        print("_ " * (len(word)))







    # start game CHECK
    # generate random word CHECK
    # show blanks/# of letters
    # track and show remaining guesses
    # update blanks to show correct guesses
    # end game


class Player:
    def __init__(self, name):
        self.name = name
        self.guesses = 8

    def guess(self):
        while self.guess > 0:
            

    # def choose_level(self):

    # set # of guesses to 8 - CHECK
    # choose difficulty
    # guess letters


game = Game()