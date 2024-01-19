import pytest
from project import WordWizardryGame, load_categories, game_rules, play_game

TEST_FILE_PATH = 'WW_Game.csv'
#Available categories - Names, Cities, Countries, Animals, Objects, Colors, Foods, Brands, Jobs, Sports

@pytest.fixture
def test_game():
    return WordWizardryGame(file_path=TEST_FILE_PATH)

def test_load_categories(): #ensures that the load_categories function loads categories and words successfully
    categories, words_by_category = load_categories(TEST_FILE_PATH)
    assert categories is not None
    assert words_by_category is not None
    assert len(categories) > 0
    assert all(category.strip() for category in categories)
    assert all(len(words) > 0 for words in words_by_category.values())

def test_choose_category(test_game, capsys, monkeypatch): #test uses monkeypatch to simulate user input during the test
    monkeypatch.setattr('builtins.input', lambda _: '1\n') #
    category = test_game.choose_category()
    assert category in test_game.categories
    captured = capsys.readouterr()
    assert "Choose a category (select only the number):" in captured.out

def test_choose_word(test_game): #tests if the choose_word function returns a valid word from the specified category
    category = 'Foods' # replace with an actual category from the game
    word = test_game.choose_word(category)
    assert word is not None
    assert word in test_game.words_by_category[category]

def test_display_word(test_game): #test checks if the display_word function formats the displayed word correctly based on the guesses
    test_game.guesses = {'a', 'b', 'c'}  # replace with some guesses
    displayed_word = test_game.display_word('abc')
    assert displayed_word == 'a b c'

def test_play_game(test_game, capsys, monkeypatch):
    # You can use monkeypatch to simulate user input during the test
    monkeypatch.setattr('builtins.input', lambda _: 'a')  # replace 'a' with the desired input
    test_game.word_to_guess = 'testword'
    test_game.lives = 3
    play_game(test_game)
    captured = capsys.readouterr()
    assert "Let's start the game!" in captured.out

if __name__ == "__main__":
    pytest.main()
