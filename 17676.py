#python3.7

# input:
# 2016-09-15 20:59:57.421 0.351s,
# 2016-09-15 20:59:58.233 1.181s,
# 2016-09-15 20:59:58.299 0.8s,
# 2016-09-15 20:59:58.688 1.041s,
# 2016-09-15 20:59:59.591 1.412s,
# 2016-09-15 21:00:00.464 1.466s,
# 2016-09-15 21:00:00.741 1.581s,
# 2016-09-15 21:00:00.748 2.31s,
# 2016-09-15 21:00:00.966 0.381s,
# 2016-09-15 21:00:02.066 2.62s

# output:
# 7

# 초당 처리량 구하기 문제

#
def dequote(s):
    """
    If a string has single or double quotes around it, remove them.
    Make sure the pair of quotes match.
    If a matching pair of quotes is not found, return the string unchanged.
    """
    if (s[0] == s[-1]) and s.startswith(("'", '"')):
        return s[1:-1]
    return s

with open("17676.txt", "r") as file_open:
    lines = file_open.read().splitlines()

for i in range(0, len(lines), 10):
    chunk = lines[i:i + 1]
    print(chunk)
