"""Write a function called sort_words that takes a string of words as an argument, removes 
the whitespaces, and returns a list of letters sorted in alphabetical order. Letters will 
be separated by commas. All letters should appear once in the list. This means that you sort 
and remove duplicates. For example ‘love life’ should return as ['e,f,i,l,o,v']."""

def sort_words(str):
    s = str.replace(" ", "")
    return [r for r in s[::-1]]

print(sort_words('love life'))


"""s = 'Hi my name is Richard'
Write a function called string_length that takes a string of words (words and spaces) 
as argument. This function should return the length of all the words in the string. 
Return the results in a form of a dictionary. The string above should return:
{'Hi': 2, 'my': 2, 'name': 4, 'is': 2, 'Richard': 7}"""

s = 'Hi my name is Richard'

def string_length(s):
    d = {}
    for each in s.split(' '):
        if each in d:
            d[each] += len(each)
        else:
            d[each] = len(each)
        
    return d

print(string_length(s))