#1
As a user
So that I can find my tasks among all my notes
I want to check if a line from my notes includes the string `#TODO`.

function plan

>>> includes_todo("#TODO buy milk")
True
>>> includes_todo("drink tea")
False
>>> includes_todo("learn to test-drive my code #TODO")
True

Tests

test that it actually returns true when #TODO is passed in argument string

test that it returns false when there is no #TODO in string

test for lowercase/uppercase

test for empty string

test for different data types passed as argument. 