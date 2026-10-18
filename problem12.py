s = input()

words = s.split(" ")
result = " ".join(
    word[0].upper() + word[1:] if word else ""
    for word in words
)

print(result)