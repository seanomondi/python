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

if average >= 0 and average < 40:
    print('Grade: E')
elif average >= 40 and average < 51:
    print('Grade: D')
elif average >= 51 and average < 61:
    print('Grade: C')
elif average >= 61 and average < 71:
    print('Grade: B')
else:
    print('Grade: A')

# if 91 <= average <= 100:
#     print('Grade: A1')
# elif 81 <= average < 91:
#     print('Grade: A2')
# elif 71 <= average < 81:
#     print('Grade: B1')
# elif 61 <= average < 71:
#     print('Grade: B2')
# elif 51 <= average < 61:
#     print('Grade: C1')
# elif 41 <= average < 51:
#     print('Grade: C2')
# elif 31 <= average < 41:
#     print('Grade: D1')
# elif 21 <= average < 31:
#     print('Grade: D2')
# elif 0 <= average < 21:
#     print('Grade: E')
# else:
#     print('invalid input!')
