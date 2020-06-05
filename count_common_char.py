# count common char in 2 strings 
from collections import Counter

s2 = 'abdc' 
s1 = 'bd'

common_letters = Counter(s1) & Counter(s2)  # => {'q': 2, 'r': 1}
print(sum(common_letters.values())) 
