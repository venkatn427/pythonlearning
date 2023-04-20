"""Write a function called make_tuples that takes two lists, equal lists, and 
combines them into a list of tuples. For example, if list a is [1,2,3,4] and 
list b is [5,6,7,8], your function should return [(1,5), (2,6), (3,7), (4,8)].
"""

def make_tuples(l1, l2):
    if len(l1) != len(l2):
        return "Invalid Input"
    return list(zip(l1, l2))

print(make_tuples([1,2,3,4],[5,6,7,8] ))

"""Extra Challenge: Even Number or Average
Write a function called even_or_average that ask a user to input five numbers. 
Once the user is done, the code should return the largest even number in the 
inputted numbers. If there is no even number in the list, the code should return 
the average of all the five numbers."""

def even_or_average(nums):
    """
    Asks user to input five numbers and then returns the largest even number,
    or if none are even, the average of all the numbers.
    """
    even_nums = [num for num in nums if num % 2 == 0]
    if even_nums:
        return max(even_nums)
    else:
        return sum(nums)/len(nums)

print(even_or_average([2, 5, 7, 9, 11]))


# Test the make_tuples function with two equal lists of integers.
def test_make_tuples_equal_lists():
    assert make_tuples([1, 2, 3], [4, 5, 6]) == [(1, 4), (2, 5), (3, 6)]

# Test the make_tuples function with two equal lists of strings.
def test_make_tuples_equal_lists_strings():
    assert make_tuples(['Hello', 'world'], ['Python', 'programming']) == [('Hello', 'Python'), ('world', 'programming')]

# Test the make_tuples function with two lists of different lengths.
def test_make_tuples_different_length_lists():
    assert make_tuples([1, 2, 3], [4, 5]) == "Invalid Input"

# Test the even_or_average function by providing five numbers, one of which is even.
def test_even_or_average_single_even_number(monkeypatch):
    input_values = [1, 3, 5, 8, 9]
    monkeypatch.setattr('builtins.input', lambda _: str(input_values.pop(0)))
    assert even_or_average() == 8

# Test the even_or_average function by providing five numbers, none of which are even.
def test_even_or_average_no_even_numbers(monkeypatch):
    input_values = [1, 3, 5, 7, 9]
    monkeypatch.setattr('builtins.input', lambda _: str(input_values.pop(0)))
    assert even_or_average() == 5.0

