grid = [
    [".", ".", ".", ".", ".", "."],
    [".", "O", "O", ".", ".", "."],
    ["O", "O", "O", "O", ".", "."],
    ["O", "O", "O", "O", "O", "."],
    [".", "O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O", "."],
    ["O", "O", "O", "O", ".", "."],
    [".", "O", "O", ".", ".", "."],
    [".", ".", ".", ".", ".", "."],
]

for i in range(len(grid[0])):
    for j in range(len(grid)):
        print(grid[j][i], end="")
    print()


# prints the heart the wrong way around
for h in range(len(grid)):
    for k in range(len(grid[0])):
        print(grid[h][k], end="")
    print()
