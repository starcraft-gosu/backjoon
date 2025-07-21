lines = [[2, 4, 6, 7, 9], [2, 4, 6, 7, 8, 9], [0, 1, 7], [4, 6, 7, 8, 9], [0, 1, 3, 6, 7, 9], [6, 7, 8, 9], [0, 1, 3, 4, 5, 7, 9], [0, 1, 2, 3, 4, 5, 6], [1, 3, 5, 9], [0, 1, 3, 4, 5, 6, 8]]

print(max(enumerate(lines), key=lambda item: len(item[1])))
max_meet_cable = max(enumerate(lines), key=lambda item: len(item[1]))[0]
print(max_meet_cable)