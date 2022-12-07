from main import register_check, lower_case

def test_register_check() -> None:
    register = {'Michael' : 'yes', 'John' : 'no' , 'Peter' : 'Yes', 'Mary': 'Yes'}
    assert register_check(register) == 3

def test_lower_case() -> None:
    names = ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]
    assert lower_case(names) == ('kerry', 'dickson', 'carol', 'adam')