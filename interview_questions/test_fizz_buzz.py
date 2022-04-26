import pytest
import fizz_buzz as fb

def test_fizz_buzz_wrong_type():
    with pytest.raises(TypeError):
        result = fb.fizz_buzz("foobar")

def test_fizz_buzz_multiple_three():
    result1 = fb.fizz_buzz(3)
    result2 = fb.fizz_buzz(9)

    assert result1 == "Fizz"
    assert result2 == "Fizz"

def test_fizz_buzz_multiple_five():
    result1 = fb.fizz_buzz(5)
    result2 = fb.fizz_buzz(10)

    assert result1 == "Buzz"
    assert result2 == "Buzz"

def test_fizz_buzz_multiple_three_and_five():
    result1 = fb.fizz_buzz(15)
    result2 = fb.fizz_buzz(30)

    assert result1 == "FizzBuzz"
    assert result2 == "FizzBuzz"

def test_fizz_buzz_not_multiple():
    result1 = fb.fizz_buzz(1)
    result2 = fb.fizz_buzz(4)

    assert result1 == "1"
    assert result2 == "4"

def test_fizz_buzz_bulk_wrong_type():
    with pytest.raises(TypeError):
        result = fb.fizz_buzz_bulk("foobar")

def test_fizz_buzz_bulk():
    expected_outcome = [
        'FizzBuzz', '1', '2', 'Fizz', '4', 'Buzz', 
        'Fizz', '7', '8','Fizz', 'Buzz',
        '11', 'Fizz', '13', '14', 'FizzBuzz']
    results = fb.fizz_buzz_bulk(15)

    assert len(results) == 16
    assert ''.join(expected_outcome) == ''.join(results)

