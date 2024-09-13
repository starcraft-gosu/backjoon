N, K = map(int, input().split())
tem = list(map(int, input().split()))

# print(tem)
haps = []
hap = 0
for i in range(K):
    hap += tem[i]
haps.append(hap)
for i in range(0, N - K):
    hap -= tem[i]
    hap += tem[i+K]
    haps.append(hap)

# print(hap)
# print(max(hap))
maxim = -9999999
for x in haps:
    if maxim < x:
        maxim = x
print(maxim)

# print(hap)

# for x in hap:
#     if maxim < x:
#         maxim = x

# print(maxim)