
from wordle_bot.game import runner
import pytest

#import game.runner

@pytest.mark.parametrize("test_guess, test_correct, expected", [("aaaaa", "bbbbb", "bbbbb")])
def test_check(test_guess, test_correct, expected):
    assert(runner.check(test_guess, test_correct) == expected)