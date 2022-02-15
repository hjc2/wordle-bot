
from wordle_bot.game import display
import pytest

#import game.runner

@pytest.mark.parametrize("test_grid, expected", [("ggggg", "🟩🟩🟩🟩🟩"), ("bbbbb", "⬛⬛⬛⬛⬛")])
def test_check(test_grid, expected):
    assert(display.displayGrid(test_grid) == expected)