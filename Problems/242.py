# Valid  anagram 
from collections import Counter
def va(x,y):
    
    return Counter(x)==Counter(y)
    """freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1"""
    
    
s="anagram"
t="nagaram"
print(va(s,t))
print(s,t)
