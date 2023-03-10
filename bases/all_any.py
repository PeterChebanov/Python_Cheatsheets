def true_x(a):
    return a == 'x'


X_O = ['x', 'x', 'o',
       'x', 'o', 'x',
       'x', 'x', 'x'
       ]

# check if the row of X_O consists only of X

row_1 = all(map(true_x, X_O[:3]))
row_2 = all(map(true_x, X_O[3:6]))
row_3 = all(map(true_x, X_O[6:]))

print(f"Row 1: {row_1}\nRow 2: {row_2}\nRow 3: {row_3}")

print("*" * 50)
# check if any of the row is 'X'
row_01 = any(map(true_x, X_O[:3]))
row_02 = any(map(true_x, X_O[3:6]))
row_03 = any(map(true_x, X_O[6:]))

print(f"Row 1: {row_01}\nRow 2: {row_02}\nRow 3: {row_03}")
