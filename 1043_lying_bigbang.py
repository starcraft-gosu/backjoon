import sys
input = sys.stdin.readline

def lie(parties, truth, M):
    truth = set(truth)

    # truth를 업데이트하며 truth와 교집합인 파티를 제외
    while True:
        start = len(parties)
        for party in parties:
            if not truth.isdisjoint(party):
                # party에서 truth의 여집합만 set로
                truth.update(party-truth)   # set는 빼기가 된다 list는 안되고
                parties.remove(party)
        end = len(parties)

        # parties의 업뎃이 없을때 종료
        if start == end:
            break
    return len(parties)

def main():
    N, M = map(int, input().split())
    _, *truth = map(int, input().split())

    parties = []
    for _ in range(M):
        _, *party = map(int, input().split())  # unpacking. gpt야 고마워!
        party = set(party)
        parties.append(party)

    if not truth:
        return M

    return(lie(parties, truth, M))

print(main())
