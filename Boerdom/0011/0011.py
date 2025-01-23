names = []

while True:
    try:
        names.append(input("Name: "))
    except EOFError:
        break

res = "Adieu, adieu, to "

if len(names) == 1:
    res += names[0]
elif len(names) == 2:
    res += names[0] + " and " + names[1]
else:
    for i in range(len(names) - 1):
        res += names[i] + ", "
    res += "and " + names[-1]

print(res)