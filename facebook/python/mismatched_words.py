def mismatched_words(str1, str2):
    set1=set(str1.split())
    set2=set(str2.split())
    return set1.symmetric_difference(set2)

assert mismatched_words(
    "Firstly this is the first string", 
    "Next is the second string"
) == {'Firstly', 'this', 'first', 'Next', 'second'}