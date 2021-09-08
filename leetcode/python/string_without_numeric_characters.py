"""
Given a string s, return the string without numeric characters

Example 1:
Input: s = "abb24ba2g6v9"
Output: "abbbagv"

Example 2:
Input: s = "one1two2"
Output: "onetwo"
"""

def strip_numeric(s):
    return "".join(c for c in s if not c.isnumeric())