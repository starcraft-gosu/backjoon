squares = [list(map(int, input().split())) for _ in range(4)]

area = set()
for square in squares:
    for i in range(square[0], square[2]):
        for j in range(square[1], square[3]):
            area.add((i, j))
print(len(area))