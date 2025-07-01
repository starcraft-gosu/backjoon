N = int(input())

five_bag = N // 5
while five_bag >= 0:
    change = N - five_bag*5
    if change % 3 == 0:
        three_bag = change//3
        print(five_bag+three_bag)
        break
    five_bag -= 1
else:
    print(-1)