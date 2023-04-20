"""Write a function called capitalize. This function takes a string as an argument and capitalizes 
the first letter of each word. For example, ‘i like learning’ becomes ‘I Like Learning’."""

def capitaliz(s):
    final_s = ''
    for i, n in enumerate(s):
        if i == 0:
            final_s += n.upper()
        else:
            final_s += n
    return final_s

print(capitaliz('i like learning'))


"""You are given a string of words. Some of the words in the string contain uppercase letters.
Write a code that will return all the words that have an uppercase letter. 
Your code should return a list of the words. Each word in the list should be reversed. 
Here is how your output should look ['gninrAel', 'tUb', 'uoY', 'yLppa', 'flesRuoy', 'eVeihca'] """

def find_upper(s):
    final_s = []
    s1 = s.split(' ')
    for each in s1:
        for e1 in each:
            if e1.isupper():
                final_s.append(each[::-1])
            else:
                continue
    return final_s

print(find_upper('leArning is hard, bUt if You appLy youRself you can achieVe success'))
                

