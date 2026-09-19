temperaturas:list[int] = [65, 72, 81, 78, 90, 60, 85, 95, 70, 88]
contador = 0

for temperatura in temperaturas:
    if temperatura > 80:
        contador+=1
print(f'A temperatura ultrapassou os 80° {contador} vezes')