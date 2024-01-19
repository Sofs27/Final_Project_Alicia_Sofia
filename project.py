import csv
import random

def main():
    game_rules()
    game = WordWizardryGame()
    play_game(game)

def load_categories(file_path): #loads categories and respective words from a csv file
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        categories = next(reader)
        words_by_category = {category: [] for category in categories}
        for row in reader:
            for i, word in enumerate(row):
                if word.strip() != "":
                    words_by_category[categories[i]].append(word.lower())
    return categories, words_by_category

def game_rules(): #Initial introduction of the game
    print("Welcome to the Word Wizardry Game!")
    print("\n This are the rules of the game!")
    print("      - The player starts the game by choosing a category")
    print("      - After choosing a category, the program will choose a random word from that category that the player has to guess.")
    print("      - To play the game, the player has to choose different letters from the english alphabet and input one letter at a time")
    print("      - The player has 10 lives that are represented by 10 emojis")
    print("      - In order to win the game, the word guessed by the player has to match the word chosen randomly by the program")

def play_game(game): #Core of Word Wizardry Game
    category = game.choose_category() #prompts the user to choose a category
    game.word_to_guess = game.choose_word(category) #randomizes a word from chosen category
    print("\nLet's start the game!\n")
    #Main game loop
    while game.lives > 0:
        print(category, '\n')
        print(f"Word: {game.display_word(game.word_to_guess)}")
        guess = input("\nEnter a letter or the entire word: ").lower()
        #Process the users input
        if len(guess) == 1 and guess.isalpha(): #for inputs with only one letter
            if guess in game.guesses:
                print("You already guessed that letter. Try again.")
            elif guess in game.word_to_guess:
                print("Good guess!")
            else:
                print("Incorrect guess!")
                game.lives -= 1
            game.guesses.add(guess)
        elif len(guess) > 1 and guess.isalpha(): #for inputs with more than one letter
            if guess.lower() == game.word_to_guess.lower():
                print("Congratulations! You guessed the word:", game.word_to_guess)
                break
            else:
                print("Incorrect guess!")
                game.lives -= 1
        else: #for inputs that are numbers or specials characters
            print("Invalid input. Please enter a single letter or the entire word.")
            continue
        
        print(f"Lives left: {game.lives} {game.emojis[game.lives - 1]}\n") #for each input the program keeps track of current lives
        
        if all(letter.lower() in game.guesses or letter == ' ' for letter in game.word_to_guess): #confirms if the word has been guessed completely by guessing all the letters
            print("Congratulations! You guessed the word:", game.word_to_guess)
            break

    if game.lives == 0: #if all lives run out it is game over
        print(f"Game over! The correct word was: {game.word_to_guess}")

class WordWizardryGame:
    def __init__(self, file_path='WW_Game.csv'):
        self.categories, self.words_by_category = load_categories(file_path) #loads categories and words from the csv file
        self.guesses = set() #stores guessed letters
        self.lives = 10 #initial number os lives
        self.emojis = ["😱", "🤣", "😂", "😅", "😆", "😁", "😄", "😃", "😀", "🧙"] #emojis to use with number of lives

    def choose_category(self): #prompt for the user to choose a category
        print("\nChoose a category (select only the number):")
        for i, category in enumerate(self.categories):
            print(f"{i + 1}. {category}")
        choice = int(input("Enter the number of your choice: ")) - 1
        return self.categories[choice]

    def choose_word(self, category): #choose word randomly from certain category
        words = self.words_by_category[category]
        return random.choice(words)

    def display_word(self, word_to_guess): #displays the word by replacing each letter with "_"
        displayed_word = ""
        for letter in word_to_guess:
            if letter in self.guesses or letter == ' ':
                displayed_word += letter + " "
            else:
                displayed_word += "_ "
        return displayed_word.strip()

if __name__ == "__main__":
    main()
