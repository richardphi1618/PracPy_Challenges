from day16 import sum_list

def test_sum_list()-> None:
    example_list = [[2, 4, 5, 6], [2, 3, 5, 6]]
    assert sum_list(example_list) == 33