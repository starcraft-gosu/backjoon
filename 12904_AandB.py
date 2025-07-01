S = input()
T = input()

p_index = 0
n_index = -1

def detect(S, T, p, n):
    current_index = n
    if T[current_index] == 'B':
        # 현재 인덱스 더하고
        n -= 1
        # 반대 인덱스로 전환

        # 반대 인덱스로 검사

    elif T[n] == 'A':
        # 현재 인덱스 더하고
        p += 1
        # 현재 인덱스 검사
        detect(S, T, p, n)
