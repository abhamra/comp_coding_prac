#Problem 1: mixing milk
import sys

#read write values
sys.stdin = open("mixmilk.in", "r")

sys.stdout = open("mixmilk.out", "w")

#getting values

#note: map takes in a function and passes the inputs it receives through said function, before outputting them
c1, m1 = map(int, input().split())
c2, m2 = map(int, input().split())
c3, m3 = map(int, input().split())

pours = 100

amts = [m1, m2, m3]
capacity = [c1, c2, c3]
amt=0


#when pouring from bucket to bucket:
#1. check curr index and next index
#2. if m1+m2>c2, then fill up to capacity and m1-=(c2-m2)
#3. if m1+m2<=c2, then m2+=m1, and m1-=m1
#4. find min of #2 and #3, then subtract from m1 and add to m2
#5. iterate through and repeat for all cases

for i in range(0, pours):
    amt = min(capacity[(i+1)%3]-amts[(i+1)%3], amts[i%3])
    amts[(i+1)%3]+=amt
    amts[i%3]-=amt
    #print(amts)

print(amts[0])
print(amts[1])
print(amts[2])