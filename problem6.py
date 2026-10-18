n = int(input())
heights = set(map(int, input().split()))
print(round(sum(heights) / len(heights), 3))