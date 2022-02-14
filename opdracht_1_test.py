import opdracht_1

def test_get_string_length():
    input1 = "1234567890"
    input2 = "0"
    input3 = ""
    input4 = { "test": 1 }
    input5 = range(6)
    assert opdracht_1.get_string_length(input1) == 10
    assert opdracht_1.get_string_length(input2) == 1
    assert opdracht_1.get_string_length(input3) == 0
    assert opdracht_1.get_string_length(input4) == -1
    assert opdracht_1.get_string_length(input5) == -1

def test_get_highest_number():
    input1 = [ 1, 2, 3, 4 ]
    input2 = [ 9, 4, 2 ]
    input3 = [ 1, 1 ]
    input4 = [ "10", 5, 1 ]
    input5 = ["tien", 5, 1]
    input6 = [ 5, 5.1 ]
    assert opdracht_1.get_highest_number(input1) == 4
    assert opdracht_1.get_highest_number(input2) == 9
    assert opdracht_1.get_highest_number(input3) == 1
    assert opdracht_1.get_highest_number(input4) == 10
    assert opdracht_1.get_highest_number(input5) == 5
    assert opdracht_1.get_highest_number(input6) == 5.1

def test_convert_string_to_number():
    input1 = "0"
    input2 = "10"
    input3 = "5.5"
    input4 = "-1"
    assert opdracht_1.convert_string_to_number(input1) == int(0)
    assert opdracht_1.convert_string_to_number(input2) == int(10)
    assert opdracht_1.convert_string_to_number(input3) == float(5.5)
    assert opdracht_1.convert_string_to_number(input4) == int(-1)

def test_get_type_count():
    input1 = [ 1, 2.2, "str", (1,"2"), {"one": 1, "two":2}, [1,2], range(2) ]
    input2 = [ 1, 2 ]
    input3 = [ "1", "", range(10) ]
    input4 = [ ("1"), (2,2), { "three": 3.3 } ]
    assert opdracht_1.get_type_count(input1) == { "int": 1, "str": 1, "float": 1, "tuple":1, "dict": 1, "list": 1, "range": 1 }
    assert opdracht_1.get_type_count(input2) == { "int": 2 }
    assert opdracht_1.get_type_count(input3) == { "str": 2, "range": 1 }
    assert opdracht_1.get_type_count(input4) == { "tuple": 2, "dict": 1 }