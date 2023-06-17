"""Write two functions. The first function is called count_words which takes a 
string of words and counts how many words are in the string."""


def count_words(s1):
    return len(s1.split(' '))


def count_elements(s1):
    s = s1.replace(' ', '')
    return len(s)


print(count_words('I love learning'))
print(count_elements('I love learning'))
