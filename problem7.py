n = int(input())
a = set(map(int, input().split()))

m = int(input())
b = set(map(int, input().split()))

for x in sorted(a.symmetric_difference(b)):
    print(x)