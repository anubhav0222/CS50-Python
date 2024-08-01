# https://cs50.harvard.edu/python/2022/psets/2/twttr/
ans = []
s = input("Input: ")
vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']

for i in s:
    if i in vowels:
        continue
    elif i not in vowels:
        ans.append(i)

print("Output: ", "".join(ans))
