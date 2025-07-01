
addr = str(input())
# print(addr)

### 1. :: 수정하기
if '::' in addr:
    cnt = 0     # 콜론 개수

    for s in addr:  # 콜론 개수 세기
        if s == ":":
           cnt += 1
    # print(1)

    new_addr = ':0000:'
    diff = 7-cnt

    for _ in range(diff):
        new_addr += '0000:'
    if addr.startswith('::'):   # ::이 맨 앞에 있을때
        new_addr = '0000' + new_addr
    elif addr.endswith('::'):   # ::이 맨 뒤에 있을때
        new_addr = new_addr + '0000'
    # else:       # ::이 가운데 있을때
    #     new_addr += ':' + new_addr + ':'
    # print(new_addr)

    # new_addr = 0000:0000.....
    addr = addr.replace('::', new_addr) # ::을 0채워서 교체
# print(addr)

### 2. 콜론 사이사이 주소 길이 확인
addr_pieces = []
piece = '' # 콜론 사이 뭉탱이

for s in addr:
    if s == ':':    # :이 나올때마다 리스트에 추가
        addr_pieces.append(piece)
        piece = ''
    else:
        piece += s
else:
    addr_pieces.append(piece) # 마지막 요소 append
    # print(addr_pieces)
# print(addr_pieces)

for i in range(len(addr_pieces)):
    addr_piece = addr_pieces[i]
    zeros = 4 - len(addr_piece) # 부족한 0 개수

    for _ in range(zeros):
        addr_piece = '0' + addr_piece
        # print(addr_piece)
    addr_pieces[i] = addr_piece

for j in range(len(addr_pieces)-1):
    print(addr_pieces[j], end=':')
print(addr_pieces[-1])