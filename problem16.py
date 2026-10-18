from collections import Counter

x = int(input())
shoe_sizes = list(map(int, input().split()))
stock = Counter(shoe_sizes)

n = int(input())
money = 0

for _ in range(n):
    size, price = map(int, input().split())

    if stock[size] > 0:
        money += price
        stock[size] -= 1

print(money)