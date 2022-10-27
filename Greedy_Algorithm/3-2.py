# 3-2. 큰 수의 법칙

## N, M, K를 공백으로 구분하여 입력받기
N, M, K = map(int, input().split())
## N 개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()   ## 입력받은 수 정렬
first = data[N-1]   ## 가장 큰 수
second = data[N-2]   ## 두 번째로 큰 수

## 가장 큰 수가 더해지는 횟수 계산
cnt = int(M / (K+1)) * K   ## int(M/(K+1)) = M//(K+1)
cnt += M % (K+1)

result = 0
result += cnt*first   ## 가장 큰 수 더하기
result += (M-cnt) * second   ## 두 번쨰로 큰 수 더하기

print(result)
