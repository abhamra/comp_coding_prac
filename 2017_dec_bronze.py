import sys

max_pos = 2000

def main():
    sys.stdin = open("billboard.in", "r")
    sys.stdout = open("billboard.out", "w")

    visible = [[False for i in range(0, max_pos)] for j in range(0, max_pos)]

    for i in range(3): #for each of the rectangles (first 2 billboards and then the truck)
        x1, y1, x2, y2 = map(int, input().split())
        # x1 += max_pos // 2
        # y1 += max_pos // 2
        # x2 += max_pos // 2
        # y2 += max_pos // 2

        for x in range(x1, x2):
            for y in range(y1, y2):
                visible[x][y] = i < 2 #this is a truth statement, so it checks if it is < 2, and when 3 !< 2, this is the case
                #of the truck, which is the last input. Because of this trick, we don't need to use an if statement

    total = 0

    for x in range(max_pos):
        for y in range(max_pos):
            total+= visible[x][y]
    print(total)

main()