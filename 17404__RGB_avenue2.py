'''
원형리스트
인접한 애들은 색이 달라야함
현재꺼가 다다음꺼에 영향을 미치나..? nope
N+1개까지 만들고 [0]이랑 [N]은 같게 놓으면 되겠다

3칸뭉탱이로 한칸씩 전진?
첫칸 빨파초
두번째트 파초빨
3트 초파초

1. 3칸 뭉탱이는 어쩔래?
    가운데꺼 기준으로 양쪽에 같은게 잇음안됨
    맨왼쪽거가 이전꺼랑 달라야함
2. 이거 최적해 보장 맞는지 어케 알래?
그럼 최소비용이 어떻게 발생되는지부터 생각해봐야지
모든 경우 중 제일 값이 적은거인데...
모든 경우 =  3*2^(N-2)
'''