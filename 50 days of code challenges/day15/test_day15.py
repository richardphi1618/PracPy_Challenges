from day15 import same_in_reverse, your_age

def test_same_in_reverse()-> None:
    assert same_in_reverse('dad')

def test_your_age()-> None:
    assert your_age('Peter', 12) == 'Hi, Peter, you are 27 years old.'