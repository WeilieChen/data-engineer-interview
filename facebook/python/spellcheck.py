# def setUp(word, input_list):
#     word = word.strip()
#     temp_list = []
#     Ismatch = False

#     if word in input_list:
#         Ismatch = True
#     elif word is None or len(word) == 0:
#         Ismatch = False
#     else:
#         for w in input_list:
#             if len(w) == len(word):
#                 temp_list.append(w)
#         for j in range(len(temp_list)):
#             count=0

#             for i in range(len(word)):
#                 if word[i] == temp_list[j][i] or word[i] == '.':
#                     count += 1
#                 else:
#                     break
#         if count == len(word):
#             Ismatch = True

#     print(Ismatch)

# def isMatch(word, input_list):
#     return setUp(word, input_list)


# isMatch('c.t', ['cat', 'bte', 'art', 'drat', 'dart', 'drab'])

def set_up(dictionary):
    max_len = max(len(word) for word in dictionary)
    char_pos = [[None] * len(dictionary) for _ in range(max_len)]

    for i, word in enumerate(dictionary):
        for j, char in enumerate(word):
            char_pos[j][i] = char 
    
    return dictionary, char_pos

dictionary, char_pos = set_up(['cat', 'bte', 'art', 'drat', 'dart', 'drab'])

def is_match(word):
    if word not in dictionary:
        pass 
    return True