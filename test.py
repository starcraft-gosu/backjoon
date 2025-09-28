with open("input.txt", "w") as f:
    f.write("50000\n")
    for _ in range(49999):
        f.write("1\n")
    f.write("999900000")