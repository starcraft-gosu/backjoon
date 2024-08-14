import math

start = (3,7)
end = (8,2)

a = abs(start[0] - end[0])
b = abs(start[1] - end[1])

r = math.sqrt(a ** 2 + b ** 2)

tna = math.atan(b/a)
cso = math.acos(a/r)
sni = math.asin(b/r)

print(math.degrees(tna), math.degrees(cso), math.degrees(sni))



hole = (0,0)
my_ball = (9,11)
target = (3, 5)