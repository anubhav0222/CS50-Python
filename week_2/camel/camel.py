# https://cs50.harvard.edu/python/2022/psets/2/camel/

ans = []
camelCase = input("camelCase: ")

for i in camelCase:
    if i.islower():
        ans.append(i)

    elif i.isupper():
        ans.append('_')
        ans.append(i.lower())

snake_case = ''.join(ans)
print("snake_case: ", snake_case)
