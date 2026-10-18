n, m = map(int, input().split())
arr = list(map(int, input().split()))

a = set(map(int, input().split()))
b = set(map(int, input().split()))

happiness = 0

for number in arr:
    if number in a:
        happiness += 1
    elif number in b:
        happiness -= 1

print(happiness)