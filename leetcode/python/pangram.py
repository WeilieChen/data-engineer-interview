"""
Write a function that takes an input string and alphabet set, and returns the minimum substring which contains every letter of the alphabet at least once 
Note: it's substring and not subsequence

Input: "aaccbc"
Alphabet: "abc"
Output: "accb"
"""

def min_sub(s, alpha):
    pos_res = []

    for i in range(len(s)):
        seen = set()
        for j in range(i, len(s)):
            if s[j] in alpha:
                seen.add(s[j])

            if len(seen) == len(alpha):
                pos_res.append(s[i:j+1])

    return min(pos_res, key = lambda k: len(k))

assert min_sub("aaccbc", "abc") == "accb"
assert min_sub("aacacbc", "abc") == "acb"

def min_sub(s, alpha):
    for n in range(len(alpha), len(s)):
        for i in range(0, len(s)):
            window = s[i:i+n]

            if set(window) >= set(alpha):
                return window

    return None

assert min_sub("aaccbc", "abc") == "accb"
assert min_sub("aacacbc", "abc") == "acb"

def min_sub(s, alpha):
    seen = {}
    for i, c in enumerate(s):
        if c in alpha:
            seen[c] = i

        if len(seen) == len(alpha):
            start = min(seen.values())
            return s[start:i+1]
    
    return None

assert min_sub("aaccbc", "abc") == "accb"
assert min_sub("aacacbc", "abc") == "acb"
assert min_sub("aacacddbc", "abc") == "acddb"
assert min_sub("ababacdd", "abc") == "bac"

