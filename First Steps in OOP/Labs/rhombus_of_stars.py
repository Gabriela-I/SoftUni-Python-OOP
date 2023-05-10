def create_rhombus(i, rows):
    space = abs(rows - i - 1)
    stars = rows - space
    print(f'{" " * space}{"* " * stars} ')


rows = int(input())
for i in range(rows * 2 - 1):
    create_rhombus(i, rows)
