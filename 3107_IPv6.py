addr = str(input())
print(addr)

# 1. :: 수정하기
cnt = 0
if addr.find('\:\:'):
    for s in addr:
        if s == "\:":
           cnt += 1
    print(1)

    new_addr = ':0000:'
    diff = 7-cnt
    for _ in range(diff):
        new_addr += '0000:'
    print(new_addr)
    addr = addr.replace('\:\:', new_addr)

print(addr)
