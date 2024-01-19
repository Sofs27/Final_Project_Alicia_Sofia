# Final Project - Word Wizardry
## Program developed by Alícia Gouveia and Sofia Rodrigues

Word Wizardry is a game between the user (the player) and the program. 
The player is introduced to the game with a welcoming phrase: "Welcome to the Word Wizardry Game!" and is then followed by the game rules:

   1) The player starts the game by choosing a category
   2) After choosing a category, the program will choose a random word from that category that the player has to guess.
   3) To play the game, the player has to choose different letters from the english alphabet and input one letter at a time
   4) The player has 10 "lives"/tries that are represented by 10 different emojis
   5) In order to win the game, the word guessed by the player has to match the word chosen randomly by the program

Besides the rules, the program will ask you to select a category by using it's corresponding number.
   The available categories are:
      1. Names
      2. Cities
      3. Countries
      4. Animals
      5. Objects
      6. Colors
      7. Foods
      8. Brands
      9. Jobs
      10. Sports

The program will choose the random word from a csv file named WW_Game. In this file the categories names are in the first row of cells and the words are distributed by columns. The words are in alphabetical order, and for each letter of the alphabet, if possible, there is a minimum of 10 words.

As you play the game, if the letter you chose is in the random chosen word, the program will tell you "Good guess!", if the letter you chose is not in the word the program will tell you "Incorrect guess!"
If you repeat a letter it will print "You already guessed that letter. Try again"
If you input a number or a character it will print "Invalid input. Please enter a single letter or the entire word" and no lives will be reduced. 
The program will recognize upper and lower case letters and words equally
Everytime you play, your lives will be displayed with the following statement "Lives left:" and at each play a life will be reduced and the corresponding emoji will appear. 
If you loose, the program will print out that 0 lives are left and "You loose!"
If you win the program will print out "Congratulations! You guessed the word: correctword"

This game can be altered in a way that gives the user the freedom to add or remove categories, depending on how the user wants to play.
   
### Structure
- def main()
- def load_categories()
- def game_rules()
- def play_game()
- class WordWizardry
    - def __init__()
    - def choose_category()
    - def choose_word()
    - def display_word()
