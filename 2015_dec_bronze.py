import sys

sys.stdin = open("paint.in", "r")

sys.stdout = open("paint.out", "w")

a, b = map(int, input().split())

c, d = map(int, input().split())

painted_array = [False for i in range (0, 101)]
for i in range(a, b):
    painted_array[i]=True
for i in range(c, d):
    painted_array[i]=True

print(sum(painted_array))
