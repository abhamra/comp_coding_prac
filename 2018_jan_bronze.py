# import sys

# sys.stdin = open("billboard.in" ,"r")
# sys.stdout = open("billboard.out", "w")

# ax1, ay1, ax2, ay2 = map(int, input().split()) #lawnmower billboard
# bx1, by1, bx2, by2 = map(int, input().split()) #cow feed billboard

# tarp = 0
# lawn_area = (ay2-ay1)*(ax2-ax1)
# #and ((bx1<ax1 and bx2>ax2) or (by1<ay1 and by2>ay2))
# #and (ax1 < min(bx1, bx2) < ax2)
# if(((by2>ay2) and (by1<ay1)) or ((bx2>ax2) and (bx1<ax1))):
#     tarp = lawn_area - (max(0, min(ay2, by2)-max(ay1, by1))*max(0, min(ax2, bx2)-max(ax1, bx1)))
# else:
#     tarp = lawn_area

# print(tarp)

import sys

sys.stdin = open("billboard.in", "r")
sys.stdout = open("billboard.out", "w")

b1 = [] #lawnmower
b2 = [] #cowfeed

b1.extend(map(int,input().split()))
b2.extend(map(int,input().split()))

def getArea(x1,y1,x2,y2):
	l = abs(x2-x1)
	w = abs(y2-y1)
	return l*w

b1area = getArea(*b1)
b2area = getArea(*b2)

x_dist = min(b1[2], b2[2]) - max(b1[0], b2[0])
y_dist = min(b1[3], b2[3]) - max(b1[1], b2[1])
areaI = max(0,x_dist) * max(0,y_dist) #overlap between b1 and b2

ans = b1area

#minimum area is less than the entire lawnmower billboard area if and only if the overlap's width or length is the same as billboard's length or width
if (x_dist == b1[2]-b1[0] or y_dist == b1[3]-b1[1]) and not (b1[1]<b2[1] and b2[3]<b1[3]) and not (b1[0]<b2[0] and b2[2]<b1[2]):
	ans-=areaI

print(ans)