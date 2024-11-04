'''
괄호검사와 같은 유형 스택으로 풀어나가보자고
남은애들을 건사시켜야함 괄호검사는 어땟더라..
스택에 건덕지 잇는 애들만 집어넣어줫음
얘넨 같은방식으론 곤란할듯?
그럼 스택에 다 때려박고 마지막놈 나올때만 뒤로와보자
뒤로 오다가 삑나면 다음으로 넘어가고 아니면 len만큼 다 폭발 퍼펑
'''
# import sys
# sys.stdin = open('input.txt', 'r')
letters = input()
strings = input()
# print(strings)

stack = []
length = len(letters)

for i in range(length):
    letter = letters[i]
    stack.append(letter)
    if letter == strings[-1]:           # 폭발 문자열의 마지막 문자와 같으면
        if len(stack) < len(strings):          # 스택 길이가 len(string)보다 작을때는 제외
            continue
        else:
            for j in range(-1, -(len(strings)+1), -1):      # 음수 인덱스 쓸땐 뒤에 세번째 인자 -1을 꼭!
                if stack[j] == strings[j]:      # 스택과 string의 원소가 서로 같은지 뒤에서부터 확인
                    continue
                else:
                    break
            else:                               # 다 같을 시 else로 넘어감
                for _ in range(len(strings)):   # 문자열 길이만큼 스택 팝
                    stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')