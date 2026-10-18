s = input()
k = int(input())

for i in range(0, len(s), k):
    part = s[i:i + k]
    result = ""

    for char in part:
        if char not in result:
            result += char

    print(result)