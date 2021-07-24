"""
Given an ip address as an input string, validate it and return True/False
"""


def solution(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        return False

    for p in parts:
        if not p.isdigit():
            return False

        i = int(p)
        if i < 0 and i > 255:
            return False

    return True


assert solution("172.16.254.1") == True
assert solution("172.16.254.1.1") == False
assert solution("172.16.254") == False
assert solution("a.16.254.1") == False
