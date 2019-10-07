"""Есть список"""

print("Task One\n")
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in a:
    if i > 5:
        print(i)

print("\nTask Two\n")
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for i in a:
    for n in b:
        if i == n:
            c.append(i)

print(c)

