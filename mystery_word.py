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
        # self.show_blanks(word)
        # return word
        show_blanks = (["_ "] * (len(word)))
        print(show_blanks)
        self.guess_letter(show_blanks, letters)

    def guess_letter(self, show_blanks, letters):
        while "_ " in show_blanks:
            playing = True
            print("What is your guess?")
            guess = input("guess a letter: ")
            if len(guess) == 1 and guess.isalpha():
                print(guess)
                if guess in show_blanks:
                    print("You have already guessed that. Please try again.")         
                elif guess in letters:
                # for char in letters:
                    index_pos = self.find_index_position(letters, guess)
                    self.show_correct_guess(index_pos, guess, show_blanks)
                    print(show_blanks)
                else:
                    print("I'm sorry, that is incorrect. Please try again.")
                    self.player.guesses += 1


    def find_index_position(self, letters, guess):
        index_position_list = []
        index_position = 0
        while True:
            try:
                index_position = letters.index(guess, index_position)
                index_position_list.append(index_position)
                index_position += 1
            except:
                break
        return index_position_list

        # for i in range(len(letters)):
        #     if letters[i] == guess:
        #         index_position_list.append(i)
        # return index_position_list

    def show_correct_guess(self, index_pos, guess, show_blanks):
        guess_in_word = len(index_pos) * [guess, ]
        for (index, guess) in zip(index_pos, guess_in_word):
            show_blanks[index] = guess

    def game_over(self, guesses):
        while guesses == 8:
            playing = False
            print("Game over")
# while self.guess > 0:

    # start game CHECK
    # generate random word CHECK
    # show blanks/# of letters
    # track and show remaining guesses
    # update blanks to show correct guesses
    # end game


class Player:
    def __init__(self, name):
        self.name = name
        self.guesses = 0


    # def choose_level(self):

    # set # of guesses to 8 - CHECK
    # choose difficulty
    # guess letters


game = Game()
