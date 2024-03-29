# List
s = [0] * 3
s[0] += 1
print(s)

s = [''] * 3
s[0] += 'a'
print(s)

s = [[]] * 3
s[0] += [1]
print(s)

s = [[]] * 3
s[0] = s[0] + [1]
print(s)

# Tuples
def gcd(a, b):
    while b:
        a, b = b, a % b
    return print(a)

gcd(10, 25)  # => 5
gcd(14, 15)  # => 1
gcd(3, 9)  # => 3
gcd(1, 1)  # => 1

# Dictionaries
my_map = {"CA": "US", "NY": "US", "ON": "CA"}

def flip_dict(my_dict):
    inv_map = {}
    for key, value in my_dict.items():
        inv_map[value] = inv_map.get(value, [])
        inv_map[value].append(key)
    print(inv_map)

flip_dict(my_map)

# Comprehensions
print('1', [x for x in [1, 2, 3, 4]])
print('2', [n - 2 for n in range(10)])
print('3', [k % 10 for k in range(41) if k % 3 == 0])
print('4', [s.lower() for s in ['PythOn', 'iS', 'cOoL'] if s[0] < s[-1]])
arr = [[3, 2, 1], ['a', 'b', 'c'], [('do',), ['re'], 'mi']]
print(arr)
print('5',[el.append(el[0] * 4) for el in arr] )
print('6', [letter for letter in "pYthON" if letter.isupper()])
print('7', {len(w) for w in ["its", "the", "remix", "to", "ignition"]})

#Write a comprehension to transform the input data structure into the output data structure
print([x*2+1 for x in [0, 1, 2, 3]])
print([x % 3 == 0 for x in [3, 5, 9, 8]])
print([x.split('_')[1] for x in ["TA_sam", "TA_guido", "student_poohbear", "student_htiek"]if x.startswith('TA')])
print([x.upper()[0] for x in['apple', 'orange', 'pear']])
print([x for x in['apple', 'orange', 'pear'] if x != 'orange'])
print([(x, x.__len__()) for x in['apple', 'orange', 'pear']])
print({x: x.__len__() for x in['apple', 'orange', 'pear']})

# Cyclone Phrases (challenge)
def is_cyclone_word(word):
    word = word.upper()
    letters = [None] * len(word)
    half = (len(word) + 1) // 2
    letters[::2] = word[:half]
    letters[1::2] = word[:half - 1:-1]
    return all([left <= right for left, right in zip(letters, letters[1:])])

def is_cyclone_phrase(phrase):
    return all([is_cyclone_word(word) for word in phrase.split()])

print(is_cyclone_phrase("adjourned"))
print(is_cyclone_phrase("settled"))
print(is_cyclone_phrase("all alone at noon"))
print(is_cyclone_phrase("by myself at twelve pm"))
print(is_cyclone_phrase("acb"))
print(is_cyclone_phrase(""))

# Pascal’s Triangle
def generate_pascal_row(row):
    if not row:
        return [1]
    return [left + right for left, right in zip([0] + row, row + [0])]