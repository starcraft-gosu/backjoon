N = int(input())
numbers = list(int(input()) for _ in range(N))
numbers.sort()
# print(numbers)

def freq(N):
    cnt = 1
    current_cnt = 1
    freq_num = [numbers[0]]
    for i in range(N-1):
        if numbers[i] == numbers[i+1]:  # 현재 숫자와 이전 숫자가 같으면
            current_cnt += 1
            # print('a')
        else:                           # 현재숫자가 이전 숫자와 다르면 초기화
            current_cnt = 1

        if current_cnt > cnt: #
            cnt = current_cnt # cnt를 current_cnt로 갱신
            freq_num = [numbers[i]] # 최빈값 리스트도 현재값으로 갱신
            # print('b')
        elif current_cnt == cnt:
            freq_num.append(numbers[i+1])
            # print('c')
        # print(current_cnt)

    freq_num.sort()
    # print(freq_num)
    if len(freq_num) >= 2:
        return freq_num[1]
    else:
        return freq_num[0]

avg = round(sum(numbers) / N)
print(avg)
mid = numbers[N//2]
print(mid)
frequent = freq(N)
print(frequent)
dif = max(numbers) - min(numbers)
print(dif)

'''
인덱스마다 다음 값을 비교해서 cnt로 중복횟수를 저장해놔
[1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 44, 44, 44, 44, 5, 5, 5, 5, 5]
'''
