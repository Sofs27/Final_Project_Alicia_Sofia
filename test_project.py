import pytest
from your_main_module_name import WordWizardryGame, load_categories, game_rules, play_game

# Assuming your CSV file for testing is named 'test_WW_Game.csv'
TEST_FILE_PATH = 'test_WW_Game.csv'

@pytest.fixture
def test_game():
    return WordWizardryGame(file_path=TEST_FILE_PATH)

def test_load_categories():
    categories, words_by_category = load_categories(TEST_FILE_PATH)
    assert categories is not None
    assert words_by_category is not None
    assert len(categories) > 0
    assert all(category.strip() for category in categories)
    assert all(len(words) > 0 for words in words_by_category.values())

def test_game_rules(capsys):
    game_rules()
    captured = capsys.readouterr()
    assert "Word Wizardry Game" in captured.out
    assert "The player starts the game by choosing a category" in captured.out

def test_choose_category(test_game, capsys):
    with pytest.raises(ValueError):
        test_game.choose_category()
    captured = capsys.readouterr()
    assert "Choose a category" in captured.out

def test_choose_word(test_game):
    category = 'TestCategory'  # replace with an actual category in your CSV file
    word = test_game.choose_word(category)
    assert word is not None
    assert word in test_game.words_by_category[category]

def test_display_word(test_game):
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

# Add more tests as needed

if __name__ == "__main__":
    pytest.main()
