#numbers from 1 to 20
number_20 = [number for number in range(1,21)]
for numb in number_20:
    print(numb)

#numbers from 1 to 1_000_000
number_1_mil = [number for number in range(1,1_000_001)]
for numb in number_1_mil:
    print(numb)

#numbers multiple of 3
multiple_3 = [ value for value in range(3,31) if value % 3 == 0]
for value in multiple_3:
    print(value)

#cube
lstCube = [cube**3 for cube in range(1,11)]
for cube in lstCube:
    print(cube)

