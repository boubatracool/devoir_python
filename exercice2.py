
# Porgramme similaire avec les boucles et les condtions
lst1 = list(range(1200, 2000, 135))  # (1)
lst2 = []

for i in lst1:
    if i % 2 == 0:
        lst2.append(i * 2)

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
o = list()
e = list()

for number in numbers:
    if number % 2 == 0:
        o.append(number)
    else:
        e.append(number)    

print(lst1)
print(lst2)
print(o)
print(e)
