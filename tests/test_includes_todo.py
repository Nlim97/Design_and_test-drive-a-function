from lib.includes_todo import *


def test_true_when_todo_in_string():
    result = includes_todo("#TODO buy milk")
    assert result == True

def test_false_todo_not_in_string():
    assert includes_todo("buy milk") == False

def test_true_when_tofo_lowercase():
    result = includes_todo("#todo buy milk")
    assert result == True

