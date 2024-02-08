print('Grades Calculator')

math = int(input('Math: '))
if math < 0 or math > 100:
    print('invalid input!')
else:
    pass

english = int(input('English: '))
if english < 0 or english > 100:
    print('invalid input!')
else:
    pass

physics = int(input('Physics: '))
if physics < 0 or physics > 100:
    print('invalid input')
else:
    pass

kiswahili = int(input('Kiswahili: '))
if kiswahili < 0 or kiswahili > 100:
    print('invalid input!')
else:
    pass

history = int(input('History: '))
if history < 0 or history > 100:
    print('invalid input!')
else:
    pass

total = math + english + physics + kiswahili + history

average = total / 5

print(f'Average: {average}')

if average == 0 or average < 40:
    print('Grade: E')
elif average == 40 or average < 51:
    print('Grade: D')
elif average == 51 or average < 61:
    print('Grade: C')
elif average == 61 or average < 71:
    print('Grade: B')
else:
    print('Grade: A')
