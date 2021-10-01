def only_dupe(l):
    res = []
    count = {}

    for e in l:
        if e in count and count[e] == 1:
            res.append(e)
        count[e] = count.get(e, 0) + 1

    return res

assert only_dupe([10,20,30,20,20,30,40,50,-20,60,60,-20,-20]) == [20, 30, 60,-20]

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

assert is_prime(0) == False 
assert is_prime(1) == False 
assert is_prime(2) == True 
assert is_prime(3) == True 
assert is_prime(9) == False
assert is_prime(10) == False 
assert is_prime(13) == True

def convert_24(time):
    time_part = time.split(" ")[0]
    denote_part = time.split(" ")[1]
    
    hr = time_part.split(":")[0]
    mins = time_part.split(":")[1]
    secs = time_part.split(":")[2]

    if denote_part == "PM":
        hr = int(hr) + 12
        hr = 0 if hr == 24 else hr

    return f"{hr}:{mins}:{secs}"

assert convert_24("03:44:14 PM") == "15:44:14"
