from tests.flow.flo import Flo
import pytest

@pytest.mark.skip
def test_quitter():
    Flo.test('tests/flow/quitter.txt')

@pytest.mark.skip
def test_wanna_play_yes_then_quit():
    Flo.test('tests/flow/do_wanna_play_then_quit.txt')
